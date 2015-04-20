# -*- coding: utf-8 -*-
# Isabelly Cavalcante
# UFCG
 
while True:
    a,c = map(int,raw_input().split())
    if (a == 0 and c == 0):
        break
     
    seq = map(int,raw_input().split())
     
    count = a - seq[0];
     
    for i in range(1,c):
        if (seq[i-1] > seq[i]):
            count += abs(seq[i-1] - seq[i])
    print count
