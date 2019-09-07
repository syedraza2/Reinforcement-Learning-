Copyright: 2019, Syed Raza, <raza220489@gmail.com>, <https://sites.google.com/view/sraza/>

Textbook: Reinforcement Learning, Second Edition
By Richard S. Sutton and Andrew G. Barto


1. Implement the Monte Carlo ES (Exploring Starts) algorithm (see p.99 in textbook). Complete MCES.py. Run blackjack control.py to test your code on the blackjack ex- ample (see Example 5.3). Your results should be similar to Figure 5.2 (the error rate should be around 5% for 100,000 episodes). Submit MCES.py and the two figures you generated.

2. Implement Sarsa. Complete sarsa.py. Then run windy.py to test your code on the windy gridworld example (Example 6.5). You should get a figure (episodes vs time steps) similar to Figure 6.3. To get the optimal route, you may need to run windy.py a few times. Append the optimal route as comments to sarsa.py. Submit sarsa.py and the figure you generated.

3. (based on Exercise 6.9) Re-solve the windy gridworld task with 9 possible actions: left (action 0), up (1), right (2), down (3), up/left (4), up/right (5), down/right (6), down/left (7), stand(8). Specifically, complete windy9 setup.py. Run windy9.py. Ap- pend the optimal route (you may need to run the file several times) as comments to windy9 setup.py. Submit windy9 setup.py and the produced figure

4. Implement Sarsa(λ). Complete sarsa lambda.py. Run windy sarsaLambda.py to test your code on the windy gridworld example. Does λ have any impact on the learn- ing curve (comment after your code)? Submit sarsa lambda.py and the figure you generated. 
