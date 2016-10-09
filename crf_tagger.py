#coding:utf-8
import CRFPP
import os
import sys

MODEL_PATH = os.path.join(os.path.dirname(__file__),'hotel.model')
tagger = CRFPP.Tagger("-m %s"%(MODEL_PATH))

def crftagger():
	for data in datas:
		lines = data.split('\n');
		tagger.clear()
		for line in lines:
			tagger.add(line)
		tagger.parse()
		size = tagger.size()
		xsize = tagger.xsize()
		for i in range(0, size):
			w = []
			for j in range(0, xsize):
				w.append(tagger.x(i, j))
			w.append(tagger.y2(i))
			l = '\t'.join(w)+'\n'
			out.write(l)
		out.write('\n')

if __name__ == '__main__':
	datas = open(sys.argv[1]).read().strip().split('\n\n')
	out = open(sys.argv[2],'w')
	crftagger()