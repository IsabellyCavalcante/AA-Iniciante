# -*- coding: utf-8 -*-
# Isabelly Cavalcante
# UFCG
 
def mdc(a,b):
  if (b == 0):
      return a
  else:
      return mdc(b,a % b)
 
n = int(raw_input())
 
for i in range(n):
    f1,f2 = map(int,raw_input().split())
    print mdc(f1,f2)
