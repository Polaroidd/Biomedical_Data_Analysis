#!/usr/bin/env python3

import sys

f_path = sys.argv[1]
min_len = int(sys.argv[2])
chr_num = sys.argv[3]
for line in open(f_path):
	if len(line)<2:
		continue
	elif line[0]=='>':
		seq_name = line.rstrip()
		flag2 = 0
	else:
		if flag2 == 1:
			print(line.rstrip())
			flag2 = 0
			continue
		start = line.rstrip()[:-2].split(':')[1].split('-')[0]
		end = line.rstrip()[:-2].split(':')[1].split('-')[1]
		div = int(end)-int(start)
		if div>min_len and line[14:19]=='chr'+chr_num:
			print(seq_name)
			print(line.rstrip())
			flag2 = 1
			
