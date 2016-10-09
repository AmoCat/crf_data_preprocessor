#!usr/bin/env python
#coding:utf8

import os
import sys
from pyltp import Segmentor,Postagger,NamedEntityRecognizer

MODELDIR = '../ltp_data/'

def ltp():
	segmentor = Segmentor()
	segmentor.load(os.path.join(MODELDIR,"cws.model"))

	postagger = Postagger()
	postagger.load(os.path.join(MODELDIR,"pos.model"))

	recognizer = NamedEntityRecognizer()
	recognizer.load(os.path.join(MODELDIR,"ner.model"))

	for data in datas:
		words = segmentor.segment(data)
		postags = postagger.postag(words)
		netags = recognizer.recognize(words,postags)
		for i in range(0,len(words)):
			line = words[i]+'\t'+postags[i]+'\t'+netags[i]+'\n'
			out.write(line)
		out.write('\n')
	segmentor.release()
	postagger.release()
	recognizer.release()

if __name__ == '__main__':
	datas = open(sys.argv[1]).read().strip().split()
	out = open(sys.argv[2],'w')
	ltp()
