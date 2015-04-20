# -*- coding: utf-8 -*-
# Isabelly Cavalcante
# UFCG
 
while True:
    b,n = map(int, raw_input().split())
     
    if (b == 0 and n == 0):
        break
     
    credit = map(int, raw_input().split())
     
    pagar = [0] * b
    recebido = [0] * b
     
    for i in range(n):
        d,c,v = map(int, raw_input().split())
        pagar[d-1] += v
        recebido[c-1] += v
     
    cond = True
    for i in range(b):
        if (credit[i] + recebido[i]) < pagar[i]:
            cond = False
            break
         
    if (cond):
        print "S"
    else:
        print "N"
