import re


def main(text):
    num = re.compile('new[ |\n](\\w+) ?:= ?(\\w+).')
    return re.findall(num, text)
