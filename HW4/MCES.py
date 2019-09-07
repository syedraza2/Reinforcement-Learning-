import numpy as np

def MCES(get_episode,initial_Q,initial_policy,gamma,alpha,num_episodes=1e6):
    # This function implements the Monte Carlo ES algorithm. 
    # It returns the learned Q values and the greedy policy w.r.t. Q.
    
    # If alpha = 0, update Q[s,a] += (G - Q[s,a]) / N_sa[s,a];
    # otherwise, Q[s,a] += (G - Q[s,a]) * alpha

    # initialization  
    Q = np.copy(initial_Q)
    policy = np.copy(initial_policy)
    num_states, num_actions = Q.shape
    N_sa = np.zeros([num_states,num_actions]) #counter of (s,a)
    
    iteration = 0
    
    while iteration < num_episodes:

        """
        Your code
        """
        
        states,actions,rewards = get_episode(policy,None, np.random.randint(2)) # generate an episode
        #print('state',states)
        #print('reward',rewards)
        G=0

        for t in range(len(states)): #iteration over the length of the states
            N_sa[states[t],actions[t]] = N_sa[states[t],actions[t]] +1
            G= gamma*G + rewards[t]
            if (alpha == 0):
                Q[states[t],actions[t]] += (G - Q[states[t],actions[t]] ) / N_sa[states[t],actions[t]] 
            else:
                Q[states[t],actions[t]]  += (G - Q[states[t],actions[t]] ) * alpha

            #Now for the best policy
            if Q[states[t],1] < Q[states[t],0]:
                policy[states[t],1] = 1
            elif Q[states[t],1] > Q[states[t],0]:
                policy[states[t],0] = 1
            else:
            	policy[states[t]] = np.ones(2)/2





        
        iteration += 1                                        
        
    return Q , policy

