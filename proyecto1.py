def prob_1(n):
	return n%2 == 0

def prob_2(f):
	return (f-32)* (5/9)

def prob_3(b,p):
	cont= 0
	while cont > p :
		res= b * b
		cont= cont + 1 
	return res 	

def prob_4(pal,lon):
	list(pal)
	lol= len(pal)
	longi= lon - lol
	res= ("*" * (longi/2), pal , "*" * (longi/2))
	return res


