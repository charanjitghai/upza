import html2text
import nltk
import re
import requests


class parser:

    def __init__(self, debug=False):
        self.parser = html2text.HTML2Text()
        self.parser.ignore_links = True
        self.debug = debug

    def log(self, *arg):
        if self.debug:
            print(arg)

    def get_text(self, url):
        self.log("attempting to parse html")
        text = requests.get(url).text
        parsed = self.parser.handle(text)
        self.log("exiting with " + parsed)
        return parsed

if __name__ == '__main__':
    html_parser = parser(input("url? "))
    html_parser.get_all_words()

