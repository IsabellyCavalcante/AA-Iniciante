# -*- coding: utf-8 -*-
 
while True:
    a,b = map(int,raw_input().split())
     
    if a == b == 0:
        break
     
    if a == 0 and b == 1:
        print 1
        continue
    elif a == 1 and b == 2:
        print 2
        continue
    elif a == b == 1:
        print 1
        continue
     
    fib = [1,2]
    k = 2
     
    if ( a > 2):
        count = 0
    elif (a == 2):
        count = 1
    else:
        count = 2
     
    while (fib[-1] < b):
        if (fib[k-1] + fib[k-2] <= b):
            fib.append(fib[k-1] + fib[k-2])
        else:
            break
        if a <= fib[-1]:
            count += 1
        k +=1
 
    print count
