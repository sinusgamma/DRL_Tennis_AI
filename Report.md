# Report Continous Control

### The Algorithm

I have implemented the DDPG (Deep Deterministic Policy Gradient) algorithm for solving the environment. [DDPG algorithm description.](https://arxiv.org/abs/1509.02971)

### The Parameters

The actor and critic networks have two hidden layers. Sizes: [256, 128]

replay buffer size:                     BUFFER_SIZE = int(1e5)  
minibatch size:                         BATCH_SIZE = 1024      
discount factor:                        GAMMA = 0.99           
for soft update of target parameters:   TAU = 1e-3            
earning rate of the actor:              LR_ACTOR = 2e-4         
learning rate of the critic:            LR_CRITIC = 1e-3        
L2 weight decay:                        WEIGHT_DECAY = 0

### Experiences

It was very hard to solve the environment.
First I used an MADDPG approach, where both agents had different networks. With my hyperparameters and neural network architecture this didn't learn.

![scores](https://github.com/sinusgamma/DRL_Tennis_AI/blob/master/result.jpg)

As the world is symmetric it is possible to use the same networks for both agents. This DDPG approach converged far better.

The environment was solved in 4793 episodes.

![scores](https://github.com/sinusgamma/DRL_Tennis_AI/blob/master/result2.jpg)

### Optional Future Improvements

The environment was solved fast with the above parametes, but there is place for improvements. It is possiple to tune the hyperparameters, try out different neural network architectures.

Earlier in "Continous Control" I used batch normalization and gradient clipping, which I didn't use here. Implementing them can fasten training.

Returning to the MADDPG approach and tunning the hyperparameters could solve the environment as well. 

