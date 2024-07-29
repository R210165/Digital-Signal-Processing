#moving average system
x=[1,2,3,4,5,6]
y=[]
n=int(input("enter the order of the signal"))
le=len(x)
l=le-n
for i in range(0,le):
	d=0
	if(i<=l):
		d=n+i
		a=0
		for j in range(i,d):
			a+=x[j]
		y.append(a/n)
	else:
		a=0
		for j in range(i,le):
			a+=x[j]
		y.append(a/n)
print(list(y))

