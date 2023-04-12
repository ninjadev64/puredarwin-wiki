import os

from in_place import InPlace
from re import sub, finditer
import requests

regex = "\[!\[.*]\(.*\/rsrc\/\d*(?P<url>.+?)(?:%3F|\)).*?\]\(.*?\)"

def fixfile(contents):
    for x in finditer(regex, contents):
        path = "./static/img" + x["url"]
        os.makedirs(os.path.dirname(path), exist_ok = True)
        img_data = requests.get("https://sites.google.com/a/puredarwin.org/puredarwin" + x["url"]).content
        with open(path, "wb") as file:
            file.write(img_data)
    contents = sub(regex, r"![](/img\g<url>)", contents)
    return contents

def loop(path):
    for file in os.scandir(path):
        if file.is_dir():
            loop(file.path)
        else:
            with InPlace(file) as f:
                text = fixfile(f.read())
                f.write(text)

loop("docs/")