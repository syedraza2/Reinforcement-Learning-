import numpy as np

def sarsa_lambda(initial_Q,initial_state,transition,
          num_episodes,gamma, alpha, lambda_, epsilon=0.1):
    """
    This function implements backward view of Sarsa(lambda). It returns learned Q values.
    To crete Figure 6.3 and 6.4, the function also returns number of steps, and 
    the total rewards in each episode.
        
    Notes on inputs:    
    -transition: function. It takes current state s and action a as parameters 
                and returns next state s', immediate reward R, and a boolean 
                variable indicating whether s' is a terminal state. 
                (See windy_setup as an example)
    -epsilon: exploration rate as in epsilon-greedy policy
    
    """    
    
    # initialization
    Q = np.copy(initial_Q)
    num_states, num_actions = Q.shape   
    
    steps = np.zeros(num_episodes,dtype=int) # store #steps in each episode
    rewards = np.zeros(num_episodes) # store total rewards for each episode
    
    for ep in range(num_episodes):

        
        now_state = initial_state
        #epsilon greedy condition
        if np.random.random() < 1-epsilon:
            now_action = np.argmax(Q[initial_state]) #Chooses the best possible path and be greedy
        else:
            now_action = np.random.randint(num_actions) #epsilon chance it will do exploring
        
        terminal_state = False
        E = np.zeros(Q.shape)

        while terminal_state == False:
            steps[ep] = steps[ep] + 1
            next_state, R, terminal_state = transition(now_state, now_action)
            #epsilon greedy for next_state
            if np.random.random() < 1-epsilon:
                next_action = np.argmax(Q[next_state]) #Chooses the best possible path and be greedy
            else:
                next_action = np.random.randint(num_actions) #epsilon chance it will do exploring
            
            delta = R + gamma*Q[next_state] - Q[now_state]
            E[now_state,now_action] += 1
            Q += alpha*delta*E

            E = gamma*lambda_*E

            rewards[ep] = rewards[ep] + R * np.power(gamma,steps[ep]-1)

            now_state = next_state
            now_action = next_action


            
    return Q,  steps, rewards
        
    # lamda does have an impact on the learning curve. 