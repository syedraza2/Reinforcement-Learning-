
# coding: utf-8

# In[16]:




import random as rm


def MRP(st, rd):
  state = st
  reward = rd
  
  if state is 'Sleep':
      print(state)
      print("Total reward is:")
      print(reward)
  elif state is 'C1':
      print(state)
      reward = reward -2
      print(reward)
      if rm.uniform(0, 1) < 0.5: 
          state = "C2"
      else:
          state = "FB"   
      MRP(state, reward)
  elif state is 'C2':
      print(state) 
      reward = reward -2
      print(reward)
      if rm.uniform(0,1) <0.8:
          state = "C3"           
      else:
          state = "Sleep"            
      MRP(state, reward)
  elif state is 'C3':
      print(state)
      reward = reward -2
      print(reward)
      if rm.uniform(0,1) <0.6:
          state = "Pass"            
      else:
          state = "Pub"            
      MRP(state, reward)
  elif state is 'Pass':
      print(state)
      reward = reward +10
      print(reward)
      state = "Sleep"        
      MRP(state, reward)
  elif state is 'FB':
      print(state)
      reward = reward -1
      print(reward)
      if rm.uniform(0,1) <0.9:
          state = "FB"            
      else:
          state = "C1"            
      MRP(state, reward)
  elif state is 'Pub':
      print(state)
      reward = reward +1
      print(reward)
      rand = rm.uniform(0,1)
      if rand <0.2:
          state = "C1"            
      elif rand<0.6 and rand>=0.2:
          state = "C2"            
      else:
          state ="C3"            
      MRP(state, reward)   
     
"""
Trial 1
C1
-2
C2
-4
C3
-6
Pass
4
Sleep
Total reward is:
4
---------------
Trial 2
C1
-2
C2
-4
C3
-6
Pub
-5
C2
-7
C3
-9
Pub
-8
C3
-10
Pass
0
Sleep
Total reward is:
0
---------------
Trial 3
C1
-2
C2
-4
C3
-6
Pass
4
Sleep
Total reward is:
4
"""      
  
  
MRP("C1",0)   
      


     
 
  
      
 

