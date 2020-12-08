import html2text

import requests

class parser:

    def __init__(self, debug=False):
        self.parser = html2text.HTML2Text()
        self.parser.ignore_links = True
        self.debug = debug
        self.cookie = ""

    def log(self, *arg):
        if self.debug:
            print(arg)

    def set_cookie(self, cookie):
        self.cookie = cookie
        self.log("new cookie = " + self.cookie)
        return self.cookie

    def get_wiki(self, url):
        self.log("attempting to fetch wikis")
        session = requests.Session()
        cookie = self.cookie
        if bool(cookie and cookie.strip()):
            req = session.get(url, cookies={'cookie': cookie})
            text = req.text
            parsed = self.parser.handle(text)
            return parsed
        else:
            self.log("""cookie is empty. please set cookie first by calling "actions/set/cookie""""")
            return ""

    def get_text(self, url):
        self.log("attempting to parse html")
        text = requests.get(url).text
        parsed = self.parser.handle(text)
        self.log("exiting with " + parsed)
        return parsed




if __name__ == '__main__':
    html_parser = parser()
    text = html_parser.get_wiki(input("url? "))
    print(text)

