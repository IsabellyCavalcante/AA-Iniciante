# -*- coding: utf-8 -*-
# Isabelly Cavalcante
# UFCG
 
def funcao(s):
    inteiro = 0
    s = s[::-1]
    for i in range(len(s)):
        if s[i] == "1":
            inteiro += 2**i 
    return inteiro 
 
def mdc(a,b):
  if (b == 0):
      return a
  else:
      return mdc(b,a % b)
 
nc = int(raw_input())
 
for i in range(nc): 
    s1 = raw_input()
    s2 = raw_input()
    r1 = funcao(s1)
    r2 = funcao(s2)
     
    L = mdc(r1,r2)
     
    if (L>1):
        print "Pair #%s: All you need is love!" %str(i+1)
    else:
        print "Pair #%s: Love is not all you need!" %str(i+1)
