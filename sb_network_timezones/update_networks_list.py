import sys
import os
import re
import codecs
import json

import requests
from bs4 import BeautifulSoup
from pytz import country_timezones

SCRIPT_PATH = ''
QUIET = False  # set to True to disable listing the preformed actions, or run with -q
PURGE = False  # set to True purge old/invalid networks, or run with -p


def main():
    # Load data from TVDB network select box
    new_list = {}
    url = 'http://thetvdb.com/?tab=series&id=80379&lid=7'  # the big bang theory
    data = requests.get(url).content
    networks = BeautifulSoup(data, 'html.parser').select('select[name="changenetwork"] > option')
    for current in networks[1:]:  # skip first empty option
        new_list[current['value']] = current.text

    # Load data from latest TVDB database dump
    # https://forums.thetvdb.com/viewtopic.php?f=3&t=7550
    # Dumped unique, not null Network values from `tvseries` table on 28/Feb/2017
    dump_list = {}
    file_path = os.path.join(SCRIPT_PATH, 'json_data', 'tvseries-table-networks.json')
    with codecs.open(file_path, 'r', 'utf-8') as dump_file:
        for item in json.load(dump_file):
            item = item['Network']
            if item not in dump_list and item not in new_list:
                dump_list[item] = item

    # Load data from current list
    file_path = os.path.join(SCRIPT_PATH, 'network_timezones.txt')
    old_list = []
    if os.path.isfile(file_path):
        with codecs.open(file_path, 'r', 'utf-8') as tz_file:
            for current in tz_file.readlines():
                name, time_zone = current.strip('\n').rsplit(':', 1)
                old_list.append({
                    'name': name,
                    'time_zone': time_zone
                })

    new_count = auto_new_count = duplicate_count = 0
    new_data = []
    invalid_data = []

    def is_name_in_list(name, lst):
        for item in lst:
            if item.startswith(name + ':'):
                return True
        return False

    if not QUIET:
        print(u'\x1b[1m--- Listing valid old networks + time zones ---\x1b[0m'.center(89))
        print(u'\x1b[1m\x1b[4;30;47m' + u'Action'.center(16) + u'Network Name'.center(35) +
              u' - ' + u'Time Zone'.center(35) + u'\x1b[0m')

    while old_list:
        current = old_list.pop(0)

        line_format = u'{name}:{time_zone}\n'.format(name=current['name'], time_zone=current['time_zone'])

        is_duplicate = is_name_in_list(current['name'], new_data + invalid_data)
        if is_duplicate:
            duplicate_count += 1
            if not QUIET:
                print(u'\x1b[1m\x1b[5;30;41m{action: ^16}\x1b[0m{name: ^35} - {time_zone: ^35}'.format(
                    action='Duplicate:', name=current['name'], time_zone=current['time_zone']))
            continue

        found_in_new = current['name'] in new_list
        found_in_dump = current['name'] in dump_list
        if not (found_in_new or found_in_dump):
            invalid_data.append(line_format)
            if not QUIET:
                print(u'\x1b[1m{color}{action: ^16}\x1b[0m{name: ^35} - {time_zone: ^35}'.format(
                    color=(u'\x1b[5;30;43m', u'\x1b[5;30;41m')[PURGE], action='Invalid:',
                    name=current['name'], time_zone=current['time_zone']))
            continue

        if not current['time_zone']:  # treat as new network
            continue

        # ensure that no duplicates are added
        if found_in_new:
            del new_list[current['name']]
        if found_in_dump:
            del dump_list[current['name']]

        new_data.append(line_format)
        if not QUIET:
            print(u'\x1b[1m\x1b[0;30;42m{action: ^16}\x1b[0m{name: ^35} - {time_zone: ^35}'.format(
                action='Re-adding:', name=current['name'], time_zone=current['time_zone']))
    if not QUIET:
        print('')

    country_code = CountryCode()
    match_country = re.compile(r'\(([a-z\s]+)\)$', re.I)
    data_to_append = []
    if not QUIET:
        print(u'\x1b[1m--- Adding new networks ---\x1b[0m'.center(127))
        print(u'\x1b[1m\x1b[4;30;47m' + u'Action'.center(17) + u'Network Name'.center(35) +
              u' - ' + u'Country'.center(35) + u' - ' + u'Guessed Time Zone'.center(35) + u'\x1b[0m')
    for key, value in new_list.items():
        # try to determine time zone by country name in display name
        tz_guess = ''
        country = re.findall(match_country, value)
        if country:
            code = country_code[country[0]]
            if len(code) <= 2:
                tz_guess = country_timezones(code)[0]

        if tz_guess:
            auto_new_count += 1
            if not QUIET:
                print(u'\x1b[1m\x1b[0;30;46m{0: ^16}\x1b[0m {1: ^35} - {2: ^35} - {3: ^35}'.format(
                    'New network:', key, country[0], tz_guess))
            new_data.append(u'{name}:{time_zone}\n'.format(name=key, time_zone=tz_guess))
        else:
            new_count += 1
            if not QUIET:
                print(u'\x1b[1m\x1b[0;30;43m{0: ^16} {1: ^35} - {2: ^35} - {3: ^35}\x1b[0m'.format(
                    'New network:', key, re.sub(re.escape(key) + r'(?:.*\((.*)\))?$', r'\1', value), 'Unknown'))
            data_to_append.append(u'{name}:{time_zone}\n'.format(name=key, time_zone=tz_guess))

    for key, value_ in dump_list.items():
        # try to determine time zone by country name in display name
        tz_guess = ''
        country = re.findall(match_country, key)
        if country:
            code = country_code[country[0]]
            if len(code) <= 2:
                tz_guess = country_timezones(code)[0]

        if tz_guess:
            auto_new_count += 1
            if not QUIET:
                print(u'\x1b[1m\x1b[0;30;46m{0: ^16}\x1b[0m {1: ^35} - {2: ^35} - {3: ^35}'.format(
                    'New network:', key, country[0], tz_guess))
            new_data.append(u'{name}:{time_zone}\n'.format(name=key, time_zone=tz_guess))
        elif country:
            new_count += 1
            if not QUIET:
                print(u'\x1b[1m\x1b[0;30;43m{0: ^16} {1: ^35} - {2: ^35} - {3: ^35}\x1b[0m'.format(
                    'New network:', key, country[0], 'Unknown'))
            data_to_append.append(u'{name}:{time_zone}\n'.format(name=key, time_zone=tz_guess))
        else:
            new_count += 1
            if not QUIET:
                print(u'\x1b[1m\x1b[0;30;43m{0: ^16} {1: ^35} - {2: ^35} - {3: ^35}\x1b[0m'.format(
                    'New network:', key, 'Unknown', 'Unknown'))
            data_to_append.append(u'{name}:{time_zone}\n'.format(name=key, time_zone=tz_guess))

    if not QUIET:
        print('')

    discarded_file_path = ''  # Suppresses warnings
    if PURGE:
        discarded_file_path = os.path.join(SCRIPT_PATH, 'DISCARDED_network_timezones.txt')

    with codecs.open(file_path, 'w', 'utf-8') as tz_file:
        if PURGE:
            if new_data:
                new_data.sort()
                tz_file.writelines(new_data)
        else:
            if new_data or invalid_data:
                joined_data = new_data + invalid_data
                joined_data.sort()
                tz_file.writelines(joined_data)
        if data_to_append:
            data_to_append.sort()
            tz_file.writelines(data_to_append)

    if PURGE and invalid_data:
        with codecs.open(discarded_file_path, 'w', 'utf-8') as tz_file:
            tz_file.writelines(invalid_data)

    print('--- Done ---\n')
    print('New file created [{0}]'.format(os.path.basename(file_path)))
    print('\t{0: <28}: {1}'.format('Total', len(new_data)))
    print('\t{0: <28}: {1}'.format('New with time zone', auto_new_count))
    print('\t{0: <28}: {1}'.format('New without time zone', new_count))
    print('\t{0: <28}: {1}'.format('Duplicates:', duplicate_count))
    if invalid_data:
        if not PURGE:
            print('\t{0: <28}: {1}'.format('Invalid networks added', len(invalid_data)))
        else:
            print('')
            print('New file created [{0}]'.format(os.path.basename(discarded_file_path)))
            print('\t{0: <28}: {1}'.format('Total discarded', len(invalid_data)))


class CountryCode:
    def __init__(self):
        """ Load countries data from json file """
        self.countries = None
        with codecs.open(os.path.join(SCRIPT_PATH, 'json_data', 'countries.json'), 'r', 'utf-8') as countries_file:
            self.countries = json.load(countries_file)

        self.exceptions = {
            u'UK': u'GB'
        }

    def __getitem__(self, country):
        """ Get country two-letter code from name """
        return self.countries.get(country, self.exceptions.get(country, country))


def fix_utf8_output():
    # try a workaround to fix utf-8 output on terminals
    utf8_writer = codecs.getwriter('UTF-8')
    if sys.version_info.major < 3:
        sys.stdout = utf8_writer(sys.stdout, errors='replace')
    else:
        sys.stdout = utf8_writer(sys.stdout.buffer, errors='replace')


if __name__ == '__main__':

    SCRIPT_PATH = os.path.dirname(__file__)
    if len(sys.argv) > 1:
        if '-q' in sys.argv[1:]:
            QUIET = True
        if '-p' in sys.argv[1:]:
            PURGE = True
    fix_utf8_output()
    main()
