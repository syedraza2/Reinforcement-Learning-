import numpy as np

def q_learn(initial_Q,initial_state,transition,
          num_episodes,gamma, alpha, epsilon=0.1):
              
    """
    This function implements Q-learning. It returns learned Q values.
    To crete figure in Eg 6.6, the function also returns number of steps, and 
    the total rewards in each episode.
        
    Notes on inputs:    
    -transition: function. It takes current state s and action a as parameters 
                and returns next state s', immediate reward R, and a boolean 
                variable indicating whether s' is a terminal state. 
                (See windy_setup as an example)
    -epsilon: exploration rate as in epsilon-greedy policy
    
    """    
    
    """ 
    Your code


    """

    # initialization
    Q = np.copy(initial_Q)
    num_states, num_actions = Q.shape    
    policy = np.zeros([num_states,num_actions])   
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
                a = np.argmax(Q[s]) #Chooses the best possible path and be greedy
            else:
                a = np.random.randint(num_actions) #epsilon chance it will do exploring
            # take action, observe S', R
            next_s, reward, terminal = transition(s,a)

            # choose next action A'

            next_a = np.argmax(Q[next_s,:])
            
            # update Q(s,a)
            Q[s,a] += alpha * (reward + gamma * Q[next_s,next_a] - Q[s,a])
            
            # update s,a
            s = next_s
            a = next_a
            
            # increase number of steps in the current episode
            steps[ep] += 1
            rewards[ep] += reward


    return Q,  steps, rewards


'''
path learned from Sarsa:
state: [0, 0]   action: up
state: [0, 1]   action: up
state: [0, 2]   action: up
state: [0, 3]   action: right
state: [1, 3]   action: right
state: [2, 3]   action: right
state: [3, 3]   action: right
state: [4, 3]   action: right
state: [5, 3]   action: right
state: [6, 3]   action: right
state: [7, 3]   action: right
state: [8, 3]   action: right
state: [9, 3]   action: right
state: [10, 3]   action: right
state: [11, 3]   action: down
state: [11, 2]   action: down
state: [11, 1]   action: down
state: [7,3]
number of steps:  17
--------------------------------------
path learned from Q-learning:
state: [0, 0]   action: up
state: [0, 1]   action: right
state: [1, 1]   action: right
state: [2, 1]   action: right
state: [3, 1]   action: right
state: [4, 1]   action: right
state: [5, 1]   action: right
state: [6, 1]   action: right
state: [7, 1]   action: right
state: [8, 1]   action: right
state: [9, 1]   action: right
state: [10, 1]   action: right
state: [11, 1]   action: down
state: [7,3]
number of steps:  13
'''
