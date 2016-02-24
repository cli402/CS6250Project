# CS6250Project

##Georgia Tech Master Course: CS6250 Computer Networks

##Project: Software Defined Network with Machine Learning
Software Defined network(SDN),Software-defined networks is an emerging architecture that 
separates the control plane and data plane. This paradigm enables flexible network resource 
allocations for traffic engineering, which aims to gain better network capacity and improved 
delay and loss performance


#####feature
>1. Implement a framework with supervised machine learning based meta-layer to solve the dynamic 
routing problem in real time based on the paper (Yanjun Li, et at al.), with different choices 
of machine learning algorithms.
>2. Compared Heuristic routing algorithm with Neural Network classification of routing decision 
made based on the current network states. 
>3. Interesting to see that with a static network topology, neural network got a significant improvement of the routing calculation time
 
#####Simulation Tools
-Mininet 
-Link Layer Forwarding (L2)
-Pyretic Controller
-Generate Random Traffic     :    "iperf"
-Measure Traffic                      :    "bwm-ng"
-Heuristic                                   :    Backtracking
-Machine Learning                   :    Neural Network (Pybrain)
-* Smaller Graphs (Computation Constraint)


## To set up pyretic for running switch, do
```
./pyretic.sh
```

## To run pyretic switch (defined in pyretic/learning-switch.py), do
```
./start_controller.sh
```


###Presentation slide could be downloaded in this repository
