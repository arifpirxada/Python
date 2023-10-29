def greatest(a,b,c):
	if a>b and c:
		return a
	elif b>a and c:
		return b
	elif c>b and a:
		return c

#Using our function

e=input("Enter first number : ")
n=input("Enter second number : ")
m=input("Enter third number : ")
h=greatest(e,n,m)
print(h)

#Again using it
print("You can find the greatest of three numbers again!")

p=input("Enter first number : ")
q=input("Enter second number : ")
r=input("Enter third number : ")
s=greatest(p,q,r)
print(s)
