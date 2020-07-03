def income(n):

    y=np.array([20,1,1,1,10,8,4,2,12,12,15,29,28,28,30,29,28,25,36,30,24,25,35,26,26])
    y=y*168.37
    y1=y/60
    y_r=[]

    np.random.seed(2)
    random.seed(1)
    #the number of passengers arriving per unit time obeys Poisson distribution
    for i in y1:
        for j in range(60):
            y_r.append(poisson(i))

    y_r=np.array(y_r)
    y_r=y_r/1.5
    #from 0：00 to 17：00
    y1=y_r[0:1080]
    #from 17：00 to 24：00
    y2=y_r[1080:1500]

    y1=list(y1*0.4)
    y2=list(y2*0.7)
    y_r=y1+y2
    y_r=np.array(y_r)

    line=0
    #line_summary: queing length at different time
    line_summary=[]
    need=0
    people=0
    random.seed(3)
    for i in range(1500):
        #every minute 8.5 taxis are going to line up 
        #every minute the need of taxis increases by y_r[i]
        line+=poisson(8.5)
        need+=y_r[i]
        #If there are enough passengers, reduce the queing length at the speed of nu
        if need>n*4:
            need=need-n*4
            line=line-n*4
        #If there are not enough passengers, the queing length is reduced according to 
        #the speed at which the passengers arrive. Meanwhile, the number of passengers becomes 0
        else:
            line=line-need
            need=0
        #queing length is greater than or equal to 0
        if line<0:
            line=0
        line_summary.append(line)

    time_summary=[]
    need1=0
    for i in range(1500):
        time=0
        need1+=y_r[i]
        need=need1

        #update the need of taxis
        if need1>n*4:
            need1=need1-n*4
        else:
            need1=0

        current_line=line_summary[i]

        while current_line>0:
            j=i
            #If there are enough passengers, reduce the queue length at the speed of nu
            if need>n*4:
                current_line-=n*4
                need-=n*4
                time+=1
                while (j<1499)&(current_line>0):
                    if need>3*4:
                            j+=1
                            need+=y_r[j]
                            need-=n*4
                            current_line-=n*4
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
                    if need>n*4:
                            j+=1
                            need+=y_r[j]
                            need-=n*4
                            current_line-=n*4
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
        
    out=interval(89,time_summary)
    out=np.array(out)
    out[np.isnan(out)] = 1500
    out=list(out)
    out1=out[0]
    out2=out[1]
    print(out)
    time_interval=out1+1500-out2
    income_year=time_interval*8.5*365*0.3*(64-12.5-5)
    return income_year

def pay(n):
    width=n*1.875
    pay_year=130000*width+400*(width**2)
    return pay_year

result=[]
for i in range(1,43):
    result.append(income(i)-pay(i))
    
x=np.linspace(1,42,42)
plt.plot(x,result,'.',c='#800080')
