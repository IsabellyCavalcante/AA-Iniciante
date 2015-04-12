# -*- coding: utf-8 -*-
# Isabelly Santos Cavalcante
# UFCG
 
totalDupla = raw_input().split(" ")
 
while(int(totalDupla[0]) != 0 and int(totalDupla[1]) != 0):
     
    pessoa1 = set(raw_input().split(" "))
    pessoa2 = set(raw_input().split(" "))
 
    dif1 = pessoa1 - pessoa2
    dif2 = pessoa2 - pessoa1
 
    if (len(dif1) < len(dif2)):
        print len(dif1)
    else:
        print len(dif2)
    totalDupla = raw_input().split(" ")
