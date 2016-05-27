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
	lis= list(pal)
	lol= len(lis)
	longi= ((lon - lol)//2)
	res= ("*" * (longi) + pal + "*" * (longi))
	return res


