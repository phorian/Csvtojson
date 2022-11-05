import json, hashlib
from typing import Dict, Any

f = open("./Output.json")

data = json.load(f)


def dict_hash(dictionary: Dict[str, Any]) -> str:
    """MD5 hash of a dictionary."""
    dhash = hashlib.sha256()
    encoded = json.dumps(dictionary, sort_keys=True).encode()
    dhash.update(encoded)
    return dhash.hexdigest()


for x in data:
    print("Fetching entry...")

    print("Hashing entry...")
    x_hash = dict_hash(x)

    print("Pushing hash to object...")
    x["HASH"] = x_hash

    print("Creating new object...")
    new_x = x
    serial = new_x["Series Number"]

    print("Attempting file creation with new data...")
    try:
        with open("docs/{}.json".format(serial), "w") as f:
            f.write(json.dumps(new_x))
    except FileNotFoundError:
        print("The 'docs' directory does not exist")
    print("Done!")
