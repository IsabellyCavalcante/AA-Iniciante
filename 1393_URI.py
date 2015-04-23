# -*- coding: utf-8 -*-
# Isabelly Cavalcante
# UFCG
 
while True:
    n = int(raw_input())
     
    if(n == 0):
        break
         
    nc = [0] * (n+1)
     
    nc[n] = 1;
    nc[n-1] = 1;
 
    k = n-2
 
    while (k >= 0):
        nc[k] = nc[k+1] + nc[k+2]
        k -= 1
 
    print nc[0]
