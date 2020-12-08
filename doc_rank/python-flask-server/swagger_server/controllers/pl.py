from os import path
from pathlib import Path
import numpy as np
from .parser import parser
from .lexer import lexer

class pl_entry:
	def __init__(self, entity_id, tf):
		self.entity_id = entity_id
		self.tf = tf

	def __str__(self):
		return self.entity_id + ", " + str(self.tf)


class pl:
	def __init__(self, data_dir, debug=False):
		self.wf_path = data_dir + "wf.npy"
		Path(data_dir).mkdir(parents=True, exist_ok=True)
		self.word_to_entries = np.load(self.wf_path, allow_pickle='TRUE').item() if path.exists(self.wf_path) else {}
		self.parser = parser(debug=debug)
		self.lexer = lexer(debug=debug)
		self.debug = debug
		#self.auth_controller = auth_controller()

	def log(self, *arg):
		if self.debug:
			print(arg)

	def add_entry(self, word, entity_id, tf):
		wple = self.word_to_entries[word] if word in self.word_to_entries else {}
		wple[entity_id] = pl_entry(entity_id, tf)
		self.word_to_entries[word] = wple

	def process(self, entity_id, words):
		wm = {}
		for word in words:
			if word not in wm:
				wm[word] = 0
			wm[word] += 1
		for word in wm:
			self.log("adding entry ", word, ", ", wm[word])
			self.add_entry(word, entity_id, wm[word])

	def process_doc(self, url):
		text = self.parser.get_wiki(url)
		words = self.lexer.get_all_words(text)
		self.process(url, words)

	def set_cookie(self, cookie):
		self.log("setting cookie")
		self.parser.set_cookie(cookie)

	def process_msg(self, msg_id, text):
		self.process(msg_id, self.lexer.get_all_words(text))

	def __str__(self):
		str = ""
		for word in self.word_to_entries:
			str = str + word + ":["
			for entry in self.word_to_entries[word]:
				str += ("{" + entry + "},")
			str += "]"
			str += "\n"
		return str

	def close(self):
		np.save(self.wf_path, self.word_to_entries)

	def rank(self, keywords, limit):
		doc_to_score = {}
		for keyword in keywords:
			keyword = self.lexer.is_valid_word(keyword)[1]
			if keyword in self.word_to_entries:
				for (_, entry) in self.word_to_entries[keyword].items():
					doc = entry.entity_id
					score = entry.tf
					if doc not in doc_to_score:
						doc_to_score[doc] = 0
					doc_to_score[doc] += score
		doc_score_tups = [(word, score) for (word, score) in doc_to_score.items()]
		doc_score_tups = sorted(doc_score_tups, key = lambda x : x[1])
		top = doc_score_tups[-limit:] if limit <= len(doc_score_tups) else doc_score_tups
		return top


def test():
	pli = pl('./data/',debug=True)
	pli.process_doc("http://www.youtube.com")
	pli.process_doc("http://www.google.com")
	top2 = pli.rank(['new', 'map'], 2)
	for url in ["http://www.youtube.com", "http://www.google.com"]:
		present = False
		for entry in top2:
			if url in entry[0]:
				present = True
		if not present:
			print("Failed")
			return -1
	print("Passed")
	pli.close()

def test2():
	pli = pl('./data/', debug=True)
	pli.process_doc("http://www.youtube.com")
	pli.process_doc("http://www.google.com")
	pli.process_msg("m1", "news map news")
	top = pli.rank(['news', 'map'], 2)[-1]
	if top[0] != "m1":
		print("Failed: expected m1 was ", top[0])
		return -1
	print("Passed")	
	pli.close()

if __name__ == '__main__':
	test()
	test2()
