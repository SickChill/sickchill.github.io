import sys
import os
import re
import codecs

import requests
from bs4 import BeautifulSoup
from countrycode import countrycode
from pytz import country_timezones

if __name__ == '__main__':

    override_map = {  # add entries to override countries unmatched by country-code
        u'South Korea': u'KR',
    }

    quiet = False  # set to True to disable listing the preformed actions, or run with -q
    purge = False  # set to True purge old/invalid networks, or run with -p
    if len(sys.argv) > 1:
        if '-q' in sys.argv[1:]:
            quiet = True
        if '-p' in sys.argv[1:]:
            purge = True

    # try a workaround to fix utf-8 output on terminals
    utf8_writer = codecs.getwriter('UTF-8')
    if sys.version_info.major < 3:
        sys.stdout = utf8_writer(sys.stdout, errors='replace')
    else:
        sys.stdout = utf8_writer(sys.stdout.buffer, errors='replace')

    url = 'http://thetvdb.com/?tab=series&id=80379&lid=7'  # the big bang theory
    data = requests.get(url).content
    soup = BeautifulSoup(data, 'html.parser')
    networks = soup.select('select[name="changenetwork"] > option')

    new_list = {}
    for current in networks[1:]:  # skip first empty option
        new_list[current['value']] = current.text

    file_path = os.path.join(os.path.dirname(__file__), 'network_timezones.txt')
    old_list = []
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

    if not quiet:
        print(u'\x1b[1m--- Listing valid old networks + time zones ---\x1b[0m'.center(89))
        print(u'\x1b[1m\x1b[4;30;47m' + u'Action'.center(16) + u'Network Name'.center(35) +
              u' - ' + u'Time Zone'.center(35) + u'\x1b[0m')
    while old_list:
        current = old_list.pop(0)

        line_format = u'{name}:{time_zone}\n'.format(name=current['name'], time_zone=current['time_zone'])

        found = new_list.get(current['name'], None)
        if not found:
            is_duplicate = is_name_in_list(current['name'], new_data + invalid_data)

            if is_duplicate:
                duplicate_count += 1
            else:
                invalid_data.append(line_format)

            if quiet:
                continue

            if is_duplicate:
                print(u'\x1b[1m\x1b[5;30;41m{action: ^16}\x1b[0m{name: ^35} - {time_zone: ^35}'.format(
                    action='Duplicate:', name=current['name'], time_zone=current['time_zone']))
            else:
                print(u'\x1b[1m{color}{action: ^16}\x1b[0m{name: ^35} - {time_zone: ^35}'.format(
                    color=(u'\x1b[5;30;43m', u'\x1b[5;30;41m')[purge], action='Invalid:',
                    name=current['name'], time_zone=current['time_zone']))
            continue

        if not current['time_zone']:  # treat as new network
            continue

        del new_list[current['name']]  # ensures that no duplicates are added

        if not quiet:
            print(u'\x1b[1m\x1b[0;30;42m{action: ^16}\x1b[0m{name: ^35} - {time_zone: ^35}'.format(
                action='Re-adding:', name=current['name'], time_zone=current['time_zone']))
        new_data.append(line_format)
    if not quiet:
        print('')

    match_country = re.compile(r'\(([a-z\s]+)\)$', re.I)
    data_to_append = []
    if not quiet:
        print(u'\x1b[1m--- Adding new networks ---\x1b[0m'.center(127))
        print(u'\x1b[1m\x1b[4;30;47m' + u'Action'.center(17) + u'Network Name'.center(35) +
              u' - ' + u'Country'.center(35) + u' - ' + u'Guessed Time Zone'.center(35) + u'\x1b[0m')
    for key, value in new_list.items():
        # try to determine time zone by country name in display name
        tz_guess = ''
        country = re.findall(match_country, value)
        if country:
            code = countrycode(codes=country, origin='country_name', target='iso2c')[0]
            if len(code) > 2:
                code = override_map.get(code, code)
            if len(code) <= 2:
                tz_guess = country_timezones(code)[0]

        if tz_guess:
            auto_new_count += 1
            if not quiet:
                print(u'\x1b[1m\x1b[0;30;46m{0: ^16}\x1b[0m {1: ^35} - {2: ^35} - {3: ^35}'.format(
                    'New network:', key, country[0], tz_guess))
            new_data.append(u'{name}:{time_zone}\n'.format(name=key, time_zone=tz_guess))
        else:
            new_count += 1
            if not quiet:
                print(u'\x1b[1m\x1b[0;30;43m{0: ^16} {1: ^35} - {2: ^35} - {3: ^35}\x1b[0m'.format(
                    'New network:', key, re.sub(re.escape(key) + r'(?:.*\((.*)\))?$', r'\1', value), 'Unknown'))
            data_to_append.append(u'{name}:{time_zone}\n'.format(name=key, time_zone=tz_guess))

    if not quiet:
        print('')

    discarded_file_path = ''  # Suppresses warnings
    if purge:
        discarded_file_path = os.path.join(os.path.dirname(__file__), 'DISCARDED_network_timezones.txt')

    with codecs.open(file_path, 'w', 'utf-8') as tz_file:
        if purge:
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

    if purge and invalid_data:
        with codecs.open(discarded_file_path, 'w', 'utf-8') as tz_file:
            tz_file.writelines(invalid_data)

    print('--- Done ---\n')
    print('New file created [{0}]'.format(os.path.basename(file_path)))
    print('\t{0: <28}: {1}'.format('Total', len(new_data)))
    print('\t{0: <28}: {1}'.format('New with time zone', auto_new_count))
    print('\t{0: <28}: {1}'.format('New without time zone', new_count))
    print('\t{0: <28}: {1}'.format('Duplicates:', duplicate_count))
    if invalid_data:
        if not purge:
            print('\t{0: <28}: {1}'.format('Invalid networks added', len(invalid_data)))
        else:
            print('')
            print('New file created [{0}]'.format(os.path.basename(discarded_file_path)))
            print('\t{0: <28}: {1}'.format('Total discarded', len(invalid_data)))
