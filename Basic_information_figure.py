#Run on Jupyter Notebook
import numpy as np
import random
import math
from scipy import interpolate
import matplotlib.pyplot as plt
plt.style.use('ggplot')
plt.rcParams['font.sans-serif']=['SimHei']  
plt.rcParams['axes.unicode_minus']=False   

#Define negative exponential distribution and return random number
def expntl(L):
    #L is the mean value
    u = random.random()
    return -L * math.log(u)
#Define Poisson distribution and return random number
def poisson(L):
    
    p = 1.0
    k = 0
    e = math.exp(-L)
    while p >= e:
        u = random.random()
        p *= u
        k += 1
    return k-1
#Define normal distribution
def N(mu):
    s = np.random.normal(mu,3)
    return s

#figure 1 (first cell)
y=np.array([20,1,1,1,10,8,4,2,12,12,15,29,28,28,30,29,28,25,36,30,24,25,35,26,26])
y=y*168.37
x=np.linspace(0,24,25)
xnew=np.linspace(0,24,101)

plt.plot(x,y,"ro")
for kind in ["zero","slinear","quadratic"]:
    f=interpolate.interp1d(x,y,kind=kind)
    ynew=f(xnew)
    plt.plot(xnew,ynew,label=str(kind))
plt.legend(loc="lower right")
plt.xlabel("time/h")
plt.ylabel("number of passengers arriving")
plt.legend(loc=4) 
plt.title("time-varying passenger arrivals at Beijing Capital International Airport")
plt.savefig('time-varying passenger arrivals at Beijing Capital International Airport.png',dpi=500,bbox_inches='tight')
plt.show()

#figure 2 (second cell)
y=np.array([20,1,1,1,10,8,4,2,12,12,15,29,28,28,30,29,28,25,36,30,24,25,35,26,26])
y=y*168.37
y1=y/60
y_r=[]

np.random.seed(2)
random.seed(1)
#The number of passengers arriving per unit time obeys Poisson distribution
for i in y1:
    for j in range(60):
        y_r.append(poisson(i))

x=np.linspace(0,1499,1500)
plt.plot(x,y_r,'.')

plt.xlabel("time/min")
plt.ylabel("number of passengers arriving")
plt.legend(loc=4) 
plt.title("time-varying passenger arrivals at Beijing Capital International Airport",fontsize=12)
plt.savefig('time-varying passenger arrivals at Beijing Capital International Airport.png',dpi=500,bbox_inches='tight')
plt.show()

#figure 3 (third cell, the second cell should be run before this cell)
y_r=np.array(y_r)
y_r=y_r/1.5

y1=y_r[0:1080]

y2=y_r[1080:1500]

y1=list(y1*0.4)
y2=list(y2*0.7)
y_r=y1+y2
y_r=np.array(y_r)

plt.plot(x,y_r,".",c='g')

plt.xlabel("time/min")
plt.ylabel("number of taxis needed")
plt.legend(loc=4) 
plt.title("time-varying number of taxis needed at Beijing Capital International Airport")
plt.savefig('time-varying number of taxis needed at Beijing Capital International Airport.png',dpi=500,bbox_inches='tight')
plt.show()

#figure 4 (fourth cell, the third cell should be run before this cell)
#Queue length should be greater than or equal to 0
#u=4/min，lamda_enter=10.42/min，
line=0
#line_summary: the length of the queue at each time
line_summary=[]
need=0
people=0
random.seed(3)
for i in range(1500):
    
    line+=poisson(8.5)
    need+=y_r[i]
    
    if need>3*4:
        need=need-3*4
        line=line-3*4
    
    else:
        line=line-need
        need=0
    
    if line<0:
        line=0
    line_summary.append(line)

x=np.linspace(0,1499,1500)
plt.plot(x,line_summary,'.')

plt.xlabel("time/min")
plt.ylabel("length of the queue")
plt.legend(loc=4) 
plt.title("time-varying length of the queue")
plt.savefig('time-varying length of the queue.png',dpi=500,bbox_inches='tight')
plt.show()

# figure 5 (fifth cell,, the third cell and the fourth cell should be run before this cell)
time_summary=[]
need1=0
for i in range(1500):
    time=0
    need1+=y_r[i]
    need=need1
    
    #update the number of taxis needed
    if need1>3*4:
        need1=need1-3*4
    else:
        need1=0
        
    current_line=line_summary[i]
    
    while current_line>0:
        j=i
        #If there are enough passengers, reduce the queue length at the speed of 3u
        if need>3*4:
            current_line-=3*4
            need-=3*4
            time+=1
            while (j<1499)&(current_line>0):
                if need>3*4:
                        j+=1
                        need+=y_r[j]
                        need-=3*4
                        current_line-=3*4
                        time+=1
                    
                else:
                    j+=1
                    current_line-=need
                    need=y_r[j]
                    time+=1
        else:
            current_line-=need
            need=0
            time+=1
            while (j<1499)&(current_line>0):
                if need>3*4:
                        j+=1
                        need+=y_r[j]
                        need-=3*4
                        current_line-=3*4
                        time+=1
                    
                else:
                    j+=1
                    current_line-=need
                    need=y_r[j]
                    time+=1
    if current_line>0:
        time+=1
        need=0
        
    time_summary.append(time)
    
x=np.linspace(0,1499,1500)
#print(time_summary)
plt.plot(x,time_summary)
tb=np.ones([1500])*89
plt.plot(x,tb,label="tb")


plt.xlabel("time/min")
plt.ylabel("actual waiting time/min")
plt.legend(loc=4) 
plt.title("time-varying actual waiting time")
plt.savefig('time-varying actual waiting time.png',dpi=500,bbox_inches='tight')
plt.show()
