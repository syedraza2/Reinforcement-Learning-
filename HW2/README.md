Copyright: 2019, Syed Raza, <raza220489@gmail.com>, <https://sites.google.com/view/sraza/>

Textbook: Reinforcement Learning, Second Edition
By Richard S. Sutton and Andrew G. Barto

7. In this problem you will implement the policy iteration algorithm, which includes two components: policy evaluation and policy improvement.
a. Complete function policyEval in dynamicProgramming.py. Then test your code on the gridworld example (Example 4.1). Run test policyEval.py. You should get the same values as the ones on the left panel of Figure 4.1 in the textbook. Append results as comment to the test file. Submit test policyEval.py.
b. Complete function policyImprv in dynamicProgramming.py. Now you can call function policyIteration to find the optimal policy. Run test policyIteration.py , then append results as comment following the code in this test file. Submit test policyIteration.

8. In this problem you will implement the value iteration algorithm and apply it to the gambler’s problem (Example 4.3).
a. Complete valueIteration in dynamicProgramming.py. (You can test your code on the gridworld example before moving on to the next part.) Submit the complete dynamicProgramming.py on collab. (10%)
b. Set up the transition matrix P and the reward matrix R for the gambler’s problem (Example 4.3) in gambler example.py. Run the script with ph = 0.4, Your results should be similar to Figure 4.3. Then run the script with ph = 0.25 and 0.55. Briefly discuss the optimal policy when ph is 0.25 and 0.5, respectively. Submit gambler example.py and figures from these three runs.

9. As a further test, we will apply the value iteration algorithm (of course, we can also use the policy iteration algorithm) on the example of Jack’s car rental (Example 4.2). First, run carRental.py. The optimal policy should be similar to the the one in Figure 4.2. Then modify carRental setup.py according to the changes specified in Exercise 4.5 and run carRental.py again. Briefly discuss the optimal policy in this case. Submit figures of the optimal policy under both the original and the modified scenarios on collab. Submit modified carRental setup.py as well. 
