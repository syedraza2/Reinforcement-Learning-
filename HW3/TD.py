import numpy as np

def TD0(get_episode,policy, initial_v, gamma, alpha,num_episodes = 1):
# This function implements TD(0).
# get_episode: function to generate an episode
# policy: the policy to be evaluated 
# initial_v: initial estimate for value function v
# gamma: discount factor
# alpha: learning rate
# num_episodes: number of episodes (iterations)
# The function returns the estimate of v

    # initialization  
    v = np.copy(initial_v)
    
    for ep in range(num_episodes):
    
        states,_,rewards = get_episode(policy) # generate an episode
        #print('states',states)
        #print('rewards',rewards)

        for s in range(len(states)-1): #iteration over the length of the states
            stateLocation = states[s] #finds the location of the particular state
            stateLocationNxt = states[s+1] #finds the location of the next state
            rewardValue = rewards[s] #finds the value of reward of the particular state
            #print('stateLocation',stateLocation)
            v[stateLocation] = v[stateLocation] + alpha*(rewardValue + gamma*v[stateLocationNxt] - v[stateLocation])
            #print('v',v)
    
    
    """ 
    Your Code
    """
    
    return v


def TD_n(get_episode, policy, initial_v, n, gamma, alpha,num_episodes = 1):
# This function implements n-step TD.
# get_episode: function to generate an episode
# policy: the policy to be evaluated 
# initial_v: initial estimate for value function v
# n: number of steps to look ahead
# gamma: discount factor
# alpha: learning rate
# num_episodes: number of episodes (iterations)
# The function returns the estimate of v

    # initialization
    v = np.copy(initial_v)
    
    """
    Your Code
    """
    # states = [0,1,2,3,4] where 0 and 4 are terminal states
    # Example state episode = [2,3,4]
    # Reward = [0,1]
    # N_s = 3 (length of episode of states)
    # t = 0,1
    # n=2
    # t+n min=2, max=3
    # case 1 t+n<3 

    for ep in range(num_episodes):
    
        states,_,rewards = get_episode(policy) # generate an episode
        N_s = len(states) # length of episodic states
 
        for t in range(N_s-1): #iteration over the length of the states except terminal
            G=0
            
            
            # there are two cases, 1) t+n<T(length of states N_s) and 2) t+n>=N_s
            #case 1 t+n < N_s
            if t+n<N_s:
                # when t=0, t+n = 0,1 
                for ncount in range(n):
                    G=gamma*G+rewards[t+ncount] #goes till gamma^(n-1)
                #additional term in reward, correction gamma^n
                G=G+pow(gamma,n)*v[states[t+n]] 
                v[states[t]] = v[states[t]] + alpha*(G-v[states[t]])
            else:
            #case 2 when t+n >= N_s. We just have to use old reward formula as G_(t+n) = G_t 
            # for t=1,n=2, N_s =3    
                for r in range(len(rewards)):
                    G=gamma*G+rewards[r] #goes till gamma^(n-1)
                    # don't care about n and assume everything else is zer in the reward function
                v[states[t]] = v[states[t]] + alpha*(G-v[states[t]])





    return v


def TD_lambda(get_episode, policy, initial_v, lambda_, gamma, alpha,
              num_episodes=1):
# This function implements TD_lambda (backward view).
# get_episode: function to generate an episode
# policy: the policy to be evaluated 
# initial_v: initial estimate for value function v
# lambda_: value of lambda in TD(lambda)
# gamma: discount factor
# alpha: learning rate
# num_episodes: number of episodes (iterations)
# The function returns the estimate of v
              
    # initialization 
    v = np.copy(initial_v)
    E_trace = np.zeros(len(v))

    for ep in range(num_episodes):

        #Using formula from slides 41 and 42 of lecture 4
    
        states,_,rewards = get_episode(policy) # generate an episode
        N_s = len(states) # length of episodic states
        
 
        for t in range(N_s-1): #iteration over the length of the states in each episode excluding terminal
            delta_t =  rewards[t] + gamma*v[states[t+1]] -v[states[t]] #TD error
            for s in range(len(v)): #Iteration through each of the states in the value function to update E_trace
                if s == states[t]:# if the state index matches with state label then get a 1, otherwise 0
                    a=1
                else:
                    a=0
                E_trace[s] = gamma*lambda_*E_trace[s]+a
            v = v + alpha*delta_t*E_trace
            
        


    return v


        