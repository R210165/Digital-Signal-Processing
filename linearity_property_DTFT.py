import numpy as np
import matplotlib.pyplot as plt
def DTFT(x):
	X=[]
	N=len(x)
	w=np.arange(-1*np.pi,np.pi,0.001*np.pi)
	for i in range(0,len(x)):
	    X.append(x[i]*np.exp(-1j*w*i))
	return X
#linearity
x1=[1,2,3,4]
x2=[4,3,2,1]
x3=[]
for i in range(len(x1)):
   x3.append(x1[i]+x2[i])
f1=DTFT(x1)
f2=DTFT(x2)
f3=DTFT(x3)
s1=sum(f1)+sum(f2)
s2=sum(f3)
if(s1.all()==s2.all()):
	print("Linear",s1,s2)
else:
	print("Non Linear")
plt.subplot(2,2,1)
plt.title("")
plt.plot(s1)
plt.subplot(2,2,2)
plt.plot(s2)
plt.show()
