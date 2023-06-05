#!/usr/bin/env python3
import sys
f_path = sys.argv[1]
ID = sys.argv[2]
i = 0
l1,l2 = '',''
for line in open(f_path):
    i+=1
    if i%4 == 3:
                if line.split('.')[1].split(':')[0] == ID:
                    print(l1)
                    print(l2)
                    print(line)

    else:
        if i%4 == 1:
            l1 = line.rstrip()
        elif i%4 == 2:
            l2 = line.rstrip()
        else:
            continue 
    