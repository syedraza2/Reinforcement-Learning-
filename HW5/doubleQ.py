import numpy as np

def doubleQ(initial_Q1,initial_Q2,initial_state,transition,
           num_episodes,gamma, alpha, epsilon=0.1):
    #This function implements double Q-learning. It returns Q1, Q2 and their sum Q
    
    """
    Your code
    """

        # initialization
    Q1 = np.copy(initial_Q1)
    Q2 = np.copy(initial_Q2)
    num_states, num_actions = Q1.shape    
 
    steps = np.zeros(num_episodes,dtype=int) # store #steps in each episode
    rewards = np.zeros(num_episodes) # store total rewards for each episode
    
    for ep in range(num_episodes):
        s = initial_state
        terminal = False   
       
        # set policy based on Q-values
        #policy[s] = epsilon / num_actions
        #policy[s,np.argmax(Q[s])] += 1 - epsilon
        
        # choose action according to current policy            
        #a = np.random.choice(num_actions, p=policy[s])


       

            
        while not terminal:

            if np.random.random() < 1-epsilon:
                a = np.argmax(Q1[s]+Q2[s]) #Chooses the best possible path and be greedy
            else:
                a = np.random.randint(num_actions) #epsilon chance it will do exploring
            # take action, observe S', R
            next_s, reward, terminal = transition(s,a)

            if np.random.random()<0.5:
                next_a = np.argmax(Q1[next_s,:])            
                # update Q(s,a)
                Q1[s,a] += alpha * (reward + gamma * Q2[next_s,next_a] - Q1[s,a])
            else:
                next_a = np.argmax(Q2[next_s,:])            
                # update Q(s,a)
                Q2[s,a] += alpha * (reward + gamma * Q1[next_s,next_a] - Q2[s,a])

            
            # update s,a
            s = next_s
            a = next_a
            
            # increase number of steps in the current episode
            steps[ep] += 1
            rewards[ep] += reward
            Q=Q1+Q2

    
    return Q1, Q2, Q #,  steps#, rewards
           