#改变p——每辆出租车每个订单的平均载客量
def yy(p):
    y=np.array([20,1,1,1,10,8,4,2,12,12,15,29,28,28,30,29,28,25,36,30,24,25,35,26,26])
    y=y*168.37
    y1=y/60
    y_r=[]

    np.random.seed(2)
    random.seed(1)
    #单位时间内乘客到达的数量服从泊松分布
    for i in y1:
        for j in range(60):
            y_r.append(poisson(i))

    y_r=np.array(y_r)
    y_r=y_r/p
    #0：00到17：00
    y1=y_r[0:1080]
    #17：00到24：00
    y2=y_r[1080:1500]

    y1=list(y1*0.4)
    y2=list(y2*0.7)
    y_r=y1+y2
    y_r=np.array(y_r)

    line=0
    #line_summary是每个时间的排队长度
    line_summary=[]
    need=0
    people=0
    random.seed(3)
    for i in range(1500):
        #每分钟增加8.5辆出租车排队
        #增加y_r[i]个出租车需求量
        line+=poisson(8.5)
        need+=y_r[i]
        #如果乘客充足，则按照3u的速度减少排队长度
        if need>3*4:
            need=need-3*4
            line=line-3*4
        #如果乘客不足，则按照乘客到达的速度减少排队长度，然后乘客变为0
        else:
            line=line-need
            need=0
        #排队长度大于等于0
        if line<0:
            line=0
        line_summary.append(line)

    time_summary=[]
    need1=0
    for i in range(1500):
        time=0
        need1+=y_r[i]
        need=need1

        #更新出租车需求量
        if need1>3*4:
            need1=need1-3*4
        else:
            need1=0

        current_line=line_summary[i]

        while current_line>0:
            j=i
            #如果乘客充足，则按照3u的速度减少排队长度
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
    return time_summary

time_summary1=yy(1.35)
time_summary2=yy(1.5)
time_summary3=yy(1.65)
