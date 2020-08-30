

# global variable
sched = [(6, 8), (6, 12), (6, 7), (7, 8), (7, 10), (8, 9), (8, 10), (9, 12),
            (9, 10), (10, 11), (10, 12), (11, 12)]
################################################################################
def bestTimeToParty(schedule):
    start = schedule[0][0]
    end = schedule[0][1]
    for c in schedule:
        start = min(c[0],start)
        end = max(c[1],end)
        #print('starting time is',start) 6
        #print('end time is',end) 12
    
    #compute count of celebrities at each time
    count = celebrityDensity(sched, start, end)
    #print(count)
    
    maxcount = 0
    for i in range(start, end + 1): # i = 6,7,8,9,..,12
        if count[i] > maxcount: # eg. count[6] the num of celebrity at 6 
            maxcount = count[i]
            time = i # think about why we can not print the i as time directly  i final get
                    #update as 12
                     #time keep track of the timing when maximum number of celebrity around
            
    print('Best time to attend the party is at', time,\
          'o\'clock',':',maxcount,'celebrities will be attending!')
        
    
################################################################################

  #compute count of celebrities at each time
def celebrityDensity(schedule, start, end):
    #print(start)
    #print(end)
    count = [0]*(end + 1)
    # count = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    for i in range(start, end + 1): # i = 6,7,8...12
        count[i] = 0
        for c in sched:
            if c[0] <= i and c[1] > i:
                count[i] += 1
                
    return count
    
################################################################################                
# the  entrance (main) function
bestTimeToParty(sched)  
