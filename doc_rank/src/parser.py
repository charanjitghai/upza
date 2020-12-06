import html2text
import nltk
import re
import requests

        
class HtmlParser:

    def __init__(self,  url, stem=True, ignore_stop_word=True):
        self.url = url
        self.ignore_stop_word = ignore_stop_word
        self.parser = html2text.HTML2Text()
        self.stop_word_list = {'i':'1', 'me':'1', 'my':'1', 'myself':'1', 'we':'1', 'or':'1', 'ors':'1', 'orselves':'1', 'yo':'1', 'yor':'1', 'yors':'1', 'yorself':'1', 'yorselves':'1', 'he':'1', 'him':'1', 'his':'1', 'himself':'1', 'she':'1', 'her':'1', 'hers':'1', 'herself':'1', 'it':'1', 'its':'1', 'itself':'1', 'they':'1', 'them':'1', 'their':'1', 'theirs':'1', 'themselves':'1', 'what':'1', 'which':'1', 'who':'1', 'whom':'1', 'this':'1', 'that':'1', 'these':'1', 'those':'1', 'am':'1', 'is':'1', 'are':'1', 'was':'1', 'were':'1', 'be':'1', 'been':'1', 'being':'1', 'have':'1', 'has':'1', 'had':'1', 'having':'1', 'do':'1', 'does':'1', 'did':'1', 'doing':'1', 'a':'1', 'an':'1', 'the':'1', 'and':'1', 'bt':'1', 'if':'1', 'or':'1', 'becase':'1', 'as':'1', 'ntil':'1', 'while':'1', 'of':'1', 'at':'1', 'by':'1', 'for':'1', 'with':'1', 'abot':'1', 'against':'1', 'between':'1', 'into':'1', 'throgh':'1', 'dring':'1', 'before':'1', 'after':'1', 'above':'1', 'below':'1', 'to':'1', 'from':'1', 'p':'1', 'down':'1', 'in':'1', 'ot':'1', 'on':'1', 'off':'1', 'over':'1', 'nder':'1', 'again':'1', 'frther':'1', 'then':'1', 'once':'1', 'here':'1', 'there':'1', 'when':'1', 'where':'1', 'why':'1', 'how':'1', 'all':'1', 'any':'1', 'both':'1', 'each':'1', 'few':'1', 'more':'1', 'most':'1', 'other':'1', 'some':'1', 'sch':'1', 'no':'1', 'nor':'1', 'not':'1', 'only':'1', 'own':'1', 'same':'1', 'so':'1', 'than':'1', 'too':'1', 'very':'1', 's':'1', 't':'1', 'can':'1', 'will':'1', 'jst':'1', 'don':'1', 'shold':'1', 'now':'1'}
        self.stem = stem
        self.word_stemmer = nltk.stem.porter.PorterStemmer()

    
    def is_valid_word(self, word):
        if self.stem:
            word = self.word_stemmer.stem(word)
        if word.isalpha():
            if self.ignore_stop_word and (word in self.stop_word_list):
                return False, ""
            return True, word
        return False, ""

    def parse_html(self):
        print("attempting to parse html")
        self.parser.ignore_links = True
        text = requests.get(self.url).text
        parsed = self.parser.handle(text)
        print("exiting with " + parsed)
        return parsed

    def get_all_words(self):
        print("attempting to get words from " + self.url)
        words = self.parse_html().split()
        final_words = [] 
        for word in words:
            (valid, final_word) = self.is_valid_word(word)
            if valid:
                final_words.append(final_word)
        print("exiting with ", final_words)
        return final_words

if __name__ == '__main__':
    html_parser = HtmlParser(input("url? "))
    html_parser.get_all_words()

