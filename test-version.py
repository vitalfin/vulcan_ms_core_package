from pep440 import is_canonical
import re
import datetime
from pytz import timezone
import hashlib


main = "main"
branch2 = "feature-branch"
tag2 = "0.0.0"


def generate_datetime_with_timezone():
    format = "{dt.year}.{dt.month}.{dt.day}.{dt.hour}.{dt.minute}"
    return format.format(dt=datetime.datetime.now(timezone("America/Sao_Paulo")))


# def isTag(name):
#     return re.match("^v[0-9]+\.[0-9]+\.[0-9]+$", name)


def generate_version(name: str):
    print("Generating version for: " + name)
    date = generate_datetime_with_timezone()
    if name == "main":
        return date + "rc1"
    elif name.startswith("feature-"):
        return date + ".dev1"
    else:
        return name


def hash_branch_name(branch_name):
    return hashlib.md5(branch_name.encode("utf-8")).hexdigest()


def test_version(version):
    print("Testing version: " + version)
    if is_canonical(version):
        print("Canonical")
    else:
        raise ValueError("Not canonical: " + version)


test_version(generate_version(main))
test_version(generate_version(branch2))

test_version(generate_version(tag2))
