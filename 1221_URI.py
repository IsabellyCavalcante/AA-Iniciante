# -*- coding: utf-8 -*-
# Isabelly Cavalcante
# UFCG
 
import math
 
n = int(raw_input())
 
for i in range(n):
    x = int(raw_input())
    raiz = int(math.ceil(math.sqrt(x)))
    result = "Prime"
 
    for j in range(2, raiz):
        if (x % j == 0):
            result = "Not Prime"
            break
     
    print result
