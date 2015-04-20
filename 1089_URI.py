# -*- coding: utf-8 -*-
# Isabelly Cavalcante
# UFCG
 
while True:
    n = int(raw_input())
    if n == 0:
        break
         
    sequencia = map(int,raw_input().split())
    baixo = False
    alto = False
    pico = 1
     
    if (sequencia[0] > sequencia[1]):
        baixo = True
        alto = False
    else:
        baixo = False
        alto = True
     
    for i in range(len(sequencia)-1):
         
        if (sequencia[i] < sequencia[i+1]):
            if (baixo):
                pico += 1
            alto = True
            baixo = False
        else:
            if (alto):
                pico += 1
            baixo = True
            alto = False
     
    if (alto):
        if (sequencia[0] < sequencia[1]):
            pico += 1
    elif (baixo):
        if (sequencia[0] > sequencia[1]):
            pico += 1
     
    print pico
