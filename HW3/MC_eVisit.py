import numpy as np

def MC_eVisit(get_episode,policy,initial_v,gamma,alpha,num_episodes=1):
# This function implements the Monte Carlo every-visit algorithm.
# get_episode: function to generate an episode
# policy: the policy to be evaluated 
# initial_v: initial estimate for value function v
# gamma: discount factor
# alpha: if alpha = 0 , updata v[s] by v[s] += (G - v[s]) / N_s[s] ;   
		# Otherwise, update v[s] by v[s] += alpha * (G - v[s])
# num_episodes: number of episodes (iterations)
# The function returns the estimate of v

	# initialization  
	num_states = policy.shape[0]
	v = np.copy(initial_v)
	N_s = np.zeros(num_states) # counter for states
	R_s = np.zeros(num_states) # sum of returns
	#print('number of states',num_states)
   
	for ep in range(num_episodes):
		states,_,rewards = get_episode(policy) # generate an episode
		#print('state',states)
		#print('reward',rewards)


		
		"""
		Your Code

		"""
		#print('new ep',ep)
		
		for s in range(len(states)): #iteration over the length of the states
			G=0
			stateLocation = states[s] #finds the location of the particular state
			N_s[stateLocation] = N_s[stateLocation] + 1 #counter for how many times this particular state came in all the episodes
			
			for r in range(len(rewards)):
				G= gamma*G + rewards[r]
				#R_s[stateLocation] = R_s[stateLocation] + G #cumulative total rewards for one of the 200 states
			if alpha == 0:
				v[stateLocation] = v[stateLocation] + (G-v[stateLocation])/N_s[stateLocation]
			else:
				v[stateLocation] = v[stateLocation] + alpha*(G-v[stateLocation]) #I think this should be divided by N_s here

	#print('R_s',R_s)
	#print('N_s',N_s)
	#print('v',v)

	 
	return v

