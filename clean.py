import os

from bs4 import BeautifulSoup
from in_place import InPlace
from re import sub

def fixfile(contents):
    soup = BeautifulSoup(contents, "html.parser")

    contents = contents.replace("""<div class="sites-embed-align-left-wrapping-off">""", "")
    contents = contents.replace("""<div class="sites-embed-content sites-embed-type-toc">""", "")
    contents = sub("""<div class="sites-embed-border-off sites-embed" style="width:333px;">""", "", contents)
    contents = sub("""<div class="goog-toc sites-embed-toc-maxdepth-6">""", "", contents)

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