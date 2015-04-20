# -*- coding: utf-8 -*-
# Isabelly Cavalcante
#UFCG
 
def funcao(n, k):
    p = list(range(1,n+1))
    i = 0
    seq = []
     
    while p:
        i = (i+k-1) % len(p)
        seq.append(p.pop(i))
    return seq[-1]
 
NC = int(raw_input())
 
for i in range(NC):
    n,k = map(int, raw_input().split())
     
    print "Case %s: %i" % (i+1, funcao(n,k))
