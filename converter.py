#!/usr/bin/env python3
import sys

f_path = sys.argv[1]

L = ["A","T","G","C","N"]
for line in open(f_path):
	if line[0]==">":
		seq_len = line.rstrip()
		print(seq_len)
		continue
	str = ''
	for a in line.rstrip():
		
		if a.upper() not in L:
			str+='N'
		else:
			str+=a
	print(str)
