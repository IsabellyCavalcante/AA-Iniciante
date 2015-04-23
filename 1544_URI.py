def fatorial(x, y):
    fat = 1
    r2 = 1
    for i in xrange(2,x+1):
		fat *= i
		if (i == y):
			r2 = fat
			
    return fat, r2

while True:
	try:
		n, m = map(int,raw_input().split())
		v,w = fatorial(n, n-m) 
		p = v/w
		while (p%10 == 0):
			p = p/10

		print str(p)[-1]
	except EOFError:
		break
