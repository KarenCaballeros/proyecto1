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

def prob_5(v1, v2):
	a= ((v1[1] * v2[2]) - (v1[2] * v2[1]))
	b= ((v1[2] * v2[0]) - (v1[0] * v2[2]))
	c= ((v1[0] * v2[1]) - (v1[1] * v2[0]))
	return (a  , b  ,  c) 

def prob_6(lista):
	n= len(lista)	
