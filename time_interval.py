#This function is used for calculating the time interval when driving to "storage pool" could have higher profit.
def interval(time,time_summary):
    a=[]
    b=[]
    result=[]
    #Here is the essence of this piece of code.Although it is easy to find from resulting figures that 
    #there are only two intersections between the straight line and the curve,
    #due to randomness of Poisson flow, some points may coincide. Therefore, we are not able
    #to get the intersection just by judging if time_summary[i] is equal to time. Instead, I collect all 
    #i which satisfy the condition——(time_summary[i-5]<time)&(time_summary[i+5]>time) and all i that satisfy
    #the condition——(time_summary[i-5]>time)&(time_summary[i+5]<time), and calculate the mean of these i respectively.
    #Hence, this thorny problem is solved easily!
    for i in range(5,len(time_summary)-5):
        if (time_summary[i-5]<time)&(time_summary[i+5]>time):
            a.append(i)
        if (time_summary[i-5]>time)&(time_summary[i+5]<time):
            b.append(i)
    result.append(round(np.mean(a)))
    result.append(round(np.mean(b)))
    return result
