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


## _Contribution_
Contributions are always welcome in the form of pull requests with explanatory comments.
