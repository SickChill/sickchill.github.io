import json
from pathlib import Path

def test_loads():
    scene_exceptions_file = Path(__file__).parent.with_name("scene_exceptions.json")
    print(scene_exceptions_file.exists())
    with open(scene_exceptions_file) as fp:
        print("Reading exceptions in")
        scene_exceptions_dict = json.load(fp)

    with open(scene_exceptions_file, "w") as fp:
        print("Dumping exceptions back, formatted")
        json.dump(scene_exceptions_dict, fp, indent=2, sort_keys=True)

    assert scene_exceptions_dict

test_loads()