import numpy as np
from dynamicProgramming import *
import matplotlib.pyplot as plt

# Set up P and R
def get_P_and_R_gambler(prob_head):
    # initialization    
    P = np.zeros([101,100,101])
    R = np.zeros([101,100,101])
    
    """
    
    Your code
    
    """
    #Terminal states s=0 and s=100
    P[0,:,:]=0
    P[100,:,:]=0

    #Reward of 1 for reaching s'=100
    R[:,:,100]=1

    #s is initial state, a is stakes
    for s in range(1,100):
    	stake = min(s,100-s)
    	for a in range(1,stake+1):
    		P[s,a,s+a]=prob_head
    		P[s,a,s-a]=1-prob_head


    return P,R    

# initial value function
initial_v = np.zeros(101)
initial_v[0] = 0
initial_v[-1]=1

gamma = 1
theta = 1e-9
ph = 0.75

P, R = get_P_and_R_gambler(ph) 

opt_actions,opt_v = valueIteration(P,R,gamma,theta,initial_v,1e12)

plt.figure(figsize=(8,12))
plt.subplot(211)
plt.plot(opt_actions,'s')
plt.xlabel('capital')
plt.ylabel('stake')
plt.title('p_h = '+str(ph))
plt.grid()
plt.subplot(212)
plt.plot(opt_v,'.-')
plt.xlabel('capital')
plt.ylabel('value')
plt.grid()
plt.savefig('gambler_example_p=' + str(ph) +'.pdf',dpi=180)

