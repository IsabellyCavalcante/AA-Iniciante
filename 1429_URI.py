# -*- coding: utf-8 -*-
# Isabelly Cavalcante
# UFCG
  
def fatorial(x):
    fat = 1
    for i in xrange(1,x+1):
        fat *= i
    return fat
      
while True:
    n = raw_input()[::-1]
    if int(n) == 0:
        break
      
    decimal = 0
    for i in xrange(len(n)):
        decimal = decimal + (int(n[i]) * fatorial(i+1))
      
    print decimal
