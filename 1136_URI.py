# -*- coding: utf-8 -*-
# Isabelly Cavalcante
# UFCG

while True:
 
    n,b = map(int, raw_input().split())
    if (n==0 and b==0):
        break
 
    seq = map(int, raw_input().split())
 
    if (0 not in seq or n not in seq):
        print "N"
        continue
     
    arr = [ 0 for i in xrange(n+1) ]
     
    for i in xrange(b):
        for j in xrange(i, b):
            val = abs(seq[i] - seq[j])
            arr[val] += 1
     
    if 0 in arr:
        print "N"
    else:
        print "Y"
