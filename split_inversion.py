#!/usr/bin/env python3

import sys

f_path = sys.argv[1]

LLL = input("N : ").split()
L=[]
for i in LLL:
    if int(i) < 0:
        L.append(i)

D = {}
num = ''
j = 1
for line in open(f_path):
    if j%4 == 1:
        numm = '-'+line.rstrip()[1:]
        if numm in L:
            num = numm
        else:
            num = ''
    if j%4 == 2:
        if num != '':
            D[num] = line.rstrip().split(":")[1].split(' ')[0].split('-')

    j+=1
LL = []
startsite = ''
for i in range(len(L)):
    if i==0:
        startsite = L[i][1:]
        print(D)
        start = D[L[i]][0]
        
        end = D[L[i]][1]
    else:
        if int(L[i])+1 == int(L[i-1]):
            end = D[L[i]][1]
        else:#다음꺼가 아님
            LL.append((startsite+'-'+L[i-1][1:],start+'-'+end))
            startsite = L[i][1:]
            start = D[L[i]][0]
            end = D[L[i]][1]
            
LL.append((startsite+'-'+L[-1][1:],start+'-'+end))
for a in LL:
    print(a[1])