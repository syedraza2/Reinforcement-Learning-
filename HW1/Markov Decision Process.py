
# coding: utf-8

# In[29]:




import random as rm

#G_t = sum R_t+k+1 for k=0 to inf for MRP return
#assuming equal probability 0.5 for both actions which makes problem much simpler


def MRP(st, rd):
    state = st
    reward = rd
    action = "study"
    
#using Pub as the only state action node. Two possible actions 'study' and 'relax'
    
    if state is 'Sleep':
        print(state)
        print("Total reward weighted by action is:")
        print(reward)
    elif state is 'C1':
        print(state)
        action = "study"
        reward = reward -2*0.5
        
        print(reward)
        
        if rm.uniform(0, 1) < 0.5: 
            state = "C2"
            action = "study"
        else:
            state = "FB"
            action = "relax"
            
        MRP(state, reward)
        
    elif state is 'C2':
        print(state) 
        action = "study"
        reward = reward -2*0.5
        print(action)
        print(reward)
        if rm.uniform(0,1) <0.8:
            state = "C3"           
        else:
            state = "Sleep"            
        MRP(state, reward)
    elif state is 'C3':
        print(state)
        action = "study"
        reward = reward -2*0.5
        print(action)
        print(reward)
        if rm.uniform(0,1) <0.6:
            state = "Pass"            
        else:
            state = "Pub"  
            action = "relax"
        MRP(state, reward)
    elif state is 'Pass':
        print(state)
        reward = reward +10*0.5
        print(action)
        print(reward)
        state = "Sleep" 
        
        MRP(state, reward)
    elif state is 'FB':
        print(state)
        action = "relax"
        print(action)
        reward = reward -1*0.5
        print(reward)
        if rm.uniform(0,1) <0.9:
            state = "FB"
            action = "relax"
        else:
            state = "C1" 
            action = "study"
        MRP(state, reward)
    elif state is 'Pub':
        action = "relax"
        print(state)
        print(action)
        reward = reward +1*0.5
        print(reward)
        print(action)
        rand = rm.uniform(0,1)
        if rand <0.2:
            state = "C1" 
            action = "study"
        elif rand<0.6 and rand>=0.2:
            state = "C2" 
            action = "study"
        else:
            state ="C3"  
            action = "study"
        MRP(state, reward)   
       
"""
Trial 1
C1
-1.0
C2
study
-2.0
C3
study
-3.0
Pub
relax
-2.5
relax
C3
study
-3.5
Pass
study
1.5
Sleep
Total reward weighted by action is:
1.5

Trial 2 
C1
-1.0
FB
relax
-1.5
FB
relax
-2.0
FB
relax
-2.5
C1
-3.5
FB
relax
-4.0
C1
-5.0
C2
study
-6.0
C3
study
-7.0
Pub
relax
-6.5
relax
C3
study
-7.5
Pass
study
-2.5
Sleep
Total reward weighted by action is:
-2.5

Trial 3
C1
-1.0
FB
relax
-1.5
FB
relax
-2.0
FB
relax
-2.5
FB
relax
-3.0
C1
-4.0
FB
relax
-4.5
FB
relax
-5.0
FB
relax
-5.5
FB
relax
-6.0
FB
relax
-6.5
FB
relax
-7.0
FB
relax
-7.5
FB
relax
-8.0
FB
relax
-8.5
FB
relax
-9.0
FB
relax
-9.5
FB
relax
-10.0
C1
-11.0
FB
relax
-11.5
FB
relax
-12.0
C1
-13.0
C2
study
-14.0
C3
study
-15.0
Pass
study
-10.0
Sleep
Total reward weighted by action is:
-10.0
"""    
    
    
MRP("C1",0)   
        


       
   
    
        
 

