#!/usr/bin/env python3
import sys

f_path = sys.argv[1]
p=0
strr = ''
c = 18
L = []
D = {}
seq_L = []
K = []
flag = 0
chr_n = ''
for line in open(f_path):
    if len(line)<2:
        continue
    elif line[0] == '>':
        line.rstrip()
        if p==0:
            p=1
        else:
            p=0
    elif p==1:#chr site
        if line[0] == '#':
            chr_n = line.rstrip()
        if line[0] != '#':
            if chr_n != '# chr22':
                L.append(int(line.rstrip()[:-2].split()[-1])+1)
            
        print(line.rstrip())
    else:
        if line[0] == '#':
            temp = line.rstrip()
        else:
            if len(line.rstrip()[:-2].split(' '))>1:
                K.append((temp,line.rstrip()))
                
            else:
                if line[0] == '-':
                    if int(line[1:-2]) in L:
                        seq_L.append('#chr'+str(c))
                        D['#chr'+str(c)] = strr
                        c+=1
                        strr = ''
                        strr += line[0:-2] + ' '

                    else:
                        strr += line[0:-2]+' '
                else:
                    
                    if int(line[0:-2]) in L:
                        seq_L.append('#chr'+str(c))
                        D['#chr'+str(c)] = strr
                        c+=1
                        strr = ''
                        strr += line[0:-2] + ' '

                    else:
                        strr += line[0:-2]+' '

seq_L.append('#chr'+str(c))
D['#chr'+str(c)] = strr
print(L)
print("\nSingle sequence per Synteny")
for a in seq_L:
    print(a)
    print(D[a])

print("\nMultiple sequences per Synteny")
for a in K:
    print(a[0])
    print(a[1])
    print()