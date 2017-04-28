# Utilization-focused Evaluation on Serverless Architectures

Serverless computing is a pay-as-you-go code execution plat- form in which the cloud provider fully manages the exe- cution environment to serve requests. As it potentially de- crease the application operating cost to 77.08%[17], a heat- ing trend of adopting serverless architectures had be found since 2016. A sufficient understanding of the system uti- lization of a serverless architecture will benefit both service providers in designing architectures and application devel- opers in making adoption decisions.

In this paper, we first describe design goals of a server- less architecture then evaluate three serverless architectures: OpenLambda, IronFunctions, and Clofly. Both OpenLambda and IronFunctions apply Docker containers with different strategies of using state operations on containers for pro- viding application isolations, while Clofly handles requests purely by using subprocess calls. We observed that the cur- rent isolation solution costs five times more on server re- source usages comparing to the one with no isolation guar- antee. Also, we discussed the importance of limited resource allocations for user functions, scalable-concerned cache poli- cies, and efficiency improvements by sharing runtime re- sources.

Please refer to [our paper](serverless.pdf) for details.
