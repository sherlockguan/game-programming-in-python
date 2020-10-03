
# global variable
sched = [(6.0, 8.3), (6.5, 12.0), (6.5, 7.0), (7.5, 8.0), (7.0, 10.5), (8.0, 9.0),
          (7.2, 10.0), (9.0, 12.0),(11.0, 12.0)]
################################################################################
def bestTimeToParty(schedule):
   times = []
   for c in schedule:
       times.append((c[0],'start'))
       times.append((c[1], 'end'))
   
    #sortlist(times)#sort the list in ascending order
   print(times)
   print('')
   times.sort(key = lambda x : x[0])
   print(times)
   maxcount, time = chooseTime(times)
   
   print('Best time to attend a party is ',time,\
          'o\'clock',':',maxcount,'celebrities will be attending!')
    
################################################################################

def chooseTime(times):
    rcount  = 0
    maxcount = 0
    time = 0
    
    # Range through the times computing a running count of celebritis
    for t in times:
        if t[1] == 'start':
            rcount += 1
            #print(' recount = ',rcount)
        elif t[1] == 'end':
            rcount -= 1
            #print(' this recount is  ',rcount)
        if rcount > maxcount:
            maxcount = rcount
            
            
            time = t[0]
            #print("maxcount is ",maxcount,'corresponding time is',time)
    return maxcount, time
    
################################################################################                
# the  entrance (main) function
bestTimeToParty(sched)       
 
                
            
        
