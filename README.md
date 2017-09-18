# System-Capacity-Planning
This project is inspired by the research work reported in the article Optimal Power Allocation in Server Farms [1]. Server farms are a common part of many corporations’ computing infrastructure but they consume a lot of energy. The key question asked in this research is: Is it possible to reduce the energy consumption of server farms while maintaining good response time of the com- puting system.

## _Objectives_

1.  To apply discrete event simulation to a performance analysis problem
2.  To use statistically sound methods to analyse simulation outputs

## _Background_

A typical architecture of a server farm is shown in below figure.  The server farm consists of a high-
speed router at the front end and a number of computing servers at the back end.  A job arriving
at the server farm will first reach the high-speed router.  The function of the router is to send the
job to one of the servers in the back end.  The job will then be processed by the server and once
it is completed, the job leaves the server.  Most servers use Processor Sharing (PS) rather than
first-come-first-serve to process the jobs.  The PS in below Figure  indicates the servers are using PS
for job processing.

![image14](https://user-images.githubusercontent.com/26761582/30526603-b97f118e-9c60-11e7-8dfd-6a0d44e0e496.jpg)
Figure:  Typical architecture of a server farm.  The front-end consists of a high-speed router and
the back-end has a number of computer servers.  Each server uses processor sharing (PS)

A key performance issue in a server farm is its response time.  In this project, we will assume
that the high-speed router takes negligible time to distribute the jobs to the servers.  Therefore,
the response time of a job is due entirely to the processing in the server
Energy cost in operating servers is high.  Each server consumes typically hundreds of Watts of power.  The article stated that “
Server farms today consume more than 1.5% of the total electricity in the U.S. at a cost of nearly $4.5 billion.” (Note:  the article was published in 2009 so these are past figures.)  Given the high operating cost of server farms, a question is whether it is possible to reduce the energy consumption while maintaining the same level of system performance in terms of response time.

Modern servers are equipped with power management technologies such as Dynamic Frequency Scaling (DFS) or Dynamic Voltage and Frequency Scaling (DVFS). These technologies allow a system administrator to operate the servers at different power levels.  If the server is operating at a higher (resp.  lower) power level, then it is operating at a higher (resp.  lower) clock frequency or higher (resp.  lower) computing speed.  Figure 2 shows the relationship between clock frequency and power consumption for a particular type of server under a specific workload.  You can clearly see that the clock frequency is an increasing function of the power consumption.

The  power  management  technologies  have  provided  us  with  a  method  to  reduce  the  power consumption while maintaining the performance.  You can approach this problem in two different ways.  You can fix the performance (i.e.  response time) and see how you can reduce power consumption.  Alternatively, you can fix the power consumption and see how you can maximise the
performance.  We will take the latter approach in this project.

For example let us assume that you have a power budget of 3000W. You can operate each server at 150W, 200W and 250W, which will give you a clock frequency of 1.2 GHz, 2.7 GHz and 3 GHz.  (These clock frequencies correspond roughly to the curve in Fig. 2b.)  You can use your 3000W power budget in a variety of configurations, for example:
Operate 20 servers at 150W at clock frequency of 1.2 GHz (the slowest speed).

Operate 15 servers at 200W at clock frequency of 2.7 GHz (the medium speed).

Operate 12 servers at 250W at clock frequency of 3.0 GHz (the highest speed).

## _Description of Workload and Server farm_
In this simulation, we will assume that
1. The server farm has n servers.
2. Each server uses Processor Sharing (PS) to process the requests.
3. The power budget is xxxx watts.This means that if you switch on s serveres adn leave the other (n-s)servers off then each running server is operating at a powerr level of xxxx watts.(xxxx can be any value)
4. If a server is running at a power level of p Watts, then its clock frequency f (measured in
GHz) is a function of p and is given by
f = 1:25 + 0.31(p/200-1)

For example, if 8 servers are switched on, then each server operates at a power level of 250
Watts and its clock frequency f is 1.25 + 0:31( 250/200 - 1) = 1:3275 GHz.(assuming xxxx = 2000Watts).

Note: For simplicity, we assume in this project that the servers can operate at any power
level but in reality, a server can only operate at a discrete number of power levels.

5.  We use{a1,a2,...,ak,...,...} to denote the inter-arrival times of the requests arriving at the high-speed router.  These inter-arrival times have the following properties:
(a)  Each ak is the product of two random numbers a1k and a2k, i.e ak =a1k a2k ∀k= 1,2,...
(b)  The sequence a1k is exponentially distributed with a mean arrival rate 7.2 requests/s.
(c)  The sequence a2k is uniformly distributed in the interval [0.75,1.17].

Note:  The  easiest  way  to  generate  the  inter-arrival  times  is  to  multiply  an  exponentially
distributed random number with the given rate and a uniformly distributed random number
in the given range.  It would be more difficult to use the inverse transform method in this
case, though it is doable.

6.  The high-speed router distributes the requests using round robin job assignment.  For example, assuming s servers that are switched on and the servers that are on are Server 1, Server 2, ...., Server s.  The round robin job assignment means tha Request 1 is assigned to Server1,  Request 2 to Server 2,  ...,  Requests to Servers,  Request (s+ 1) to Server 1,  Request(s+2) to Server 2, ..., Request 2s to Server s, Request (2s+ 1) to Server 1, and so on.  You can assume the time to distribute a request to a server is negligible.

7. If the server is operating at 1 GHz, then the probability density function g(t) of the service
time t of the requests is:



## _Contribution_
Contributions are always welcome in the form of pull requests with explanatory comments.
