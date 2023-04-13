import os

from bs4 import BeautifulSoup
from in_place import InPlace
from re import sub

removal = [
    """<div class="sites-embed-align-left-wrapping-off">""",
    """<div class="sites-embed-content sites-embed-type-toc">""",
    """<div class="sites-embed-content sites-embed-type-trog-gadget">""",
    """<div style="display:block">""",
    """<div style="direction:ltr">""",
    """<div style="text-align:left;display:block;margin-right:auto;margin-left:auto">""",
    """<div class="sites-embed-border-off sites-embed" style="width:.*?px;">""",
    """<div class="goog-toc sites-embed-toc-maxdepth-.*?">""",
    """<div style="font-family:arial,sans-serif">""",
    """<div style="color:rgb\(\d*,\d*,\d*\)">""",
    """<div style="background-color:transparent">"""
]

def fixfile(contents):
    soup = BeautifulSoup(contents, "html.parser")

    for string in removal:
        contents = sub(string, "", contents)

    for span in soup.find_all("span"):
        style = span.get("style")
        opening = ""
        closing = ""

        if style is not None:
            if ("font-weight:bold" in style):
                opening = opening + "**"
                closing = "**" + closing
            
            if ("text-decoration:underline" in style):
                opening = opening + "__"
                closing = "__" + closing
            
            if ("font-style:italic" in style):
                opening = opening + "*"
                closing = "*" + closing

            if ("font-family:courier new,monospace" in style):
                opening = opening + "`"
                closing = "`" + closing
            
            if ("text-decoration:line-through" in style):
                opening = opening + "~~"
                closing = "~~" + closing

        contents = contents.replace(str(span), opening + (span.string or "") + closing)

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