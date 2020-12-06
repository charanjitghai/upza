from os import path
from pathlib import Path
import numpy as np
from parser import HtmlParser

class pl_entry:
	def __init__(self, entity_id, tf):
		self.entity_id = entity_id
		self.tf = tf

	def __str__(self):
		return self.entity_id + ", " + str(self.tf)


class pl:
	def __init__(self, data_dir):
		self.wf_path = data_dir + "wf.npy"
		Path(data_dir).mkdir(parents=True, exist_ok=True)
		self.word_to_entries = np.load(self.wf_path, allow_pickle='TRUE').item() if path.exists(self.wf_path) else {}

	def add_entry(self, word, entity_id, tf):
		wple = self.word_to_entries[word] if word in self.word_to_entries else []
		wple.append(pl_entry(entity_id, tf))
		self.word_to_entries[word] = wple

	def process(self, entity_id, words):
		wm = {}
		for word in words:
			if word not in wm:
				wm[word] = 0
			wm[word] += 1
		for word in wm:
			self.add_entry(word, entity_id, wm[word])

	def process_doc(self, url):
		parser = HtmlParser(url)
		words = parser.get_all_words()
		self.process(url, words)

	def __str__(self):
		str = ""
		for word in self.word_to_entries:
			str = str + word + ":["
			for entry in self.word_to_entries[word]:
				str += ("{" + entry.__str__() + "},")
			str += "]"
			str += "\n"
		return str

	def close(self):
		np.save(self.wf_path, self.word_to_entries)


pli = pl('./data/')
pli.process_doc("http://www.google.com")
print("pli from memory")
print(pli)
pli.close()
pli = pl('./data/')
pli.process_doc("http://www.youtube.com")
print("pli after reading")
print(pli)