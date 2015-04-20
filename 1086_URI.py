# -*- coding: utf-8 -*-
# Isabelly Cavalcante
# UFCG
  
def funcao(comprimento, larg2, t, l):
    larg = larg2*100
    i = 0
    j = len(t) - 1
      
    if (i == j and larg == l):
        return 1
  
    count = 0
  
    while True:
        if (larg == 0):
            return count
        elif (j < i):
            return 0
  
        if (t[i] == comprimento):
            if larg - l >= 0:
                count += 1
                larg -= l
            else:
                return 0
        elif (t[i] < comprimento):
            aux = t[i]
            while True:
                if (j == i):
                    break
                if (aux + t[j] == comprimento):
                    if (larg - l >= 0):
                        count += 2
                        larg -= l
                        j -= 1
                    else:
                        return 0
                    break
                elif (aux + t[j] < comprimento):
                    j -= 1
                else:
                    break
        i += 1
  
while True:
    n,m = map(int, raw_input().split())
    if n == 0 or m == 0:
        break
  
    l = int(raw_input())
    numT = int(raw_input())
    tabuas = map(int, raw_input().split())
  
    tabuas.sort(reverse=True)
  
    vertical = funcao(n,m, tabuas, l)
    horizontal = funcao(m,n, tabuas, l)
  
    if (horizontal == 0 and vertical == 0):
        print "impossivel"
    elif (horizontal == 0):
        print vertical
    elif (vertical == 0):
        print horizontal
    else:
        print min(horizontal,vertical)
