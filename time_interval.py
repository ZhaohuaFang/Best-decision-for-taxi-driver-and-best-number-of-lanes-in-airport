def interval(time,time_summary):
    a=[]
    b=[]
    result=[]
    for i in range(5,len(time_summary)-5):
        if (time_summary[i-5]<time)&(time_summary[i+5]>time):
            a.append(i)
        if (time_summary[i-5]>time)&(time_summary[i+5]<time):
            b.append(i)
    result.append(round(np.mean(a)))
    result.append(round(np.mean(b)))
    return result
