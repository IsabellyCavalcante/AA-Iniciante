# -*- coding: utf-8 -*-
# Isabelly Cavalcante
# UFCG
 
import math
 
nc = int(raw_input())
 
for i in xrange(nc):
    g = int(raw_input())
     
    delta = 1 + 8 * g
    linha = int((-1 + math.sqrt(delta))/2)
 
    print linha
