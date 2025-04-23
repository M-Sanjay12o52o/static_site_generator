import re


def extract_title(markdown):
    lines = markdown.split("\n")

    for line in lines:
        match = re.match(r"^#(?!#)\s*(.+)", line)
        if match:
            return match.group(1).strip()
    raise Exception("no h1 present")
