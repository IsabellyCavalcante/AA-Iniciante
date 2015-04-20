# -*- coding: utf-8 -*-
# Isabelly Cavalcante
# UFCG
 
while True:
    k = int(raw_input())
    if (k == 0):
        break
    n,m = map(int,raw_input().split())
     
    for i in range(k):
        x,y = map(int,raw_input().split())
         
        if (x == n or y == m):
            print "divisa"
        else:
            if (x > n and y > m):
                print "NE"
            elif (x > n and y < m):
                print "SE"
            elif (x < n and y > m):
                print "NO"
            elif (x < n and y<m):
                print "SO"
