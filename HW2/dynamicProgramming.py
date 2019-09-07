import numpy as np

def policyEval(policy, P, R, gamma, theta, max_iter=1e5):
    """
    This function implements the policy evaluation algorithm (the synchronous
    version) 
    It returns state value function v_pi.
    """    
    num_S, num_a = policy.shape    
    v = np.zeros(num_S) # initialize value function
    k = 0 # counter of iteration
    delta = 1
    """
    
    Your code


    """
   
    # transition probabilities p(s,a,s')
    
    while True:

        k=k+1
        v_test=np.zeros(num_S)
        for s in range(num_S):

            for a in range(num_a):
            
                v_test[s] = v_test[s] + policy[s,a]*(R[s,a,s]+np.dot(gamma* v , P[s, a, :]))
            
            
        delta = min(delta, max(np.abs(v_test - v)))
    
        v = v_test
        if delta < theta or k>max_iter-1:
            #print(k)
            break

    return v
    

def policyImprv(P,R,gamma,policy,v):
    """
    This function implements the policy improvement algorithm.
    It returns the improved policy and a boolean variable policy_stable (True
    if the new policy is the same as the old policy)
    """
    # initialization    
    num_S, num_a = policy.shape
    policy_new = np.zeros([num_S,num_a])
    policy_stable = True

    
    policy_old = policy
    action_old = policyEval(policy_old, P, R, gamma, 1e-8, max_iter=1e5)
    action_value = np.zeros(num_a)
    v=action_old

        
    """
    
    Your code 
    
    """
    while True:
        for s in range(num_S):
            for a in range(num_a):
                action_value[a] = R[s,a,s]+np.dot(gamma* v , P[s, a, :]) 
            greedy_iter = np.argmax(action_value) #chooses the argument for action with max value in each state 
        #print('g=',greedy_iter)
    #print('-----')
            ActionProb = 0;
            for a in range(num_a):
                if action_value[a] == action_value[greedy_iter]: 
                #print('s=',s,'a=',a)
                    ActionProb = ActionProb+1 #if multiple paths give greedy then assign equal prob
                #print('a_val',action_value[a]) 
                
            for a in range(num_a):
                if action_value[a] == action_value[greedy_iter]: #assign prob to greedy actions for each state
                    policy_new[s,a] = 1/ActionProb #if multiple paths give greedy then assign equal prob
            #print('----')
        if np.array_equal(policy_new,policy_old):
            Policy_stable = True
            print('True')
            break
        else:
            Policy_stable = False
            policy_old = policy_new
            print('False')
        
  
    return policy_new, policy_stable


def policyIteration(P,R,gamma,theta,initial_policy,max_iter=1e6):
    """
    This function implements the policy iteration algorithm.
    It returns the final policy and the corresponding state value function v.
    """
    policy_stable = False
    policy = np.copy(initial_policy)
    num_iter = 0
    
    while (not policy_stable) and num_iter < max_iter:
        num_iter += 1
        print('Policy Iteration: ', num_iter)
        # policy evaluation
        v = policyEval(policy,P,R,gamma,theta)
        # policy improvement
        policy, policy_stable = policyImprv(P,R,gamma,policy,v)
    return policy, v



def valueIteration(P,R,gamma,theta,initial_v,max_iter=1e8):
    """
    This function implements the value iteration algorithm (the in-place version).
    It returns the best action for each state  under a deterministic policy, 
    and the corresponding state-value function.
    """
    print('Running value iteration ...')    
    
    # initialization
    v = initial_v    
    num_S, num_a = P.shape[:2]
    k = 0 
    best_actions = [0] * num_S
    




    delta= 1
    action_value = np.zeros(num_a)
    v = np.zeros(num_S) # initialize value function
    theta=1e-6
    """
    
    Your code
    
    """
    while True:
        k=k+1
        vmax=np.zeros(num_S)
        for s in range(num_S):
            for a in range(num_a):
                action_value[a] = np.dot(R[s, a, :] + gamma* v, P[s, a, :])
        #print('a_valu=',action_value)
            vmax[s] = np.max(action_value)
    #print('vmax=',vmax)
        delta = min(delta, max(np.abs(vmax - v)))
    #print('delta=',delta)
        v = vmax
        if delta < theta or k>max_iter-1:
            print('k=',k)
            break
            
    for s in range(num_S):
        for a in range(num_a):
            action_value[a] = np.dot(R[s, a, :] + gamma* v, P[s, a, :])
        best_actions[s] = np.argmax(action_value)
        #print('s=',s)
        #print('actionval=', action_value)
        #print('argmax=',np.argmax(action_value))
        #print('best_actions=',best_actions)
    
    print('number of iterations:', k)
    return best_actions, v