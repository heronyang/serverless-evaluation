# Utilization-focused Evaluation on Serverless Architectures

Serverless computing is a pay-as-you-go code execution platform in which the cloud provider fully manages the execution environment to serve requests. As it potentially decrease the application operating cost to 77.08%, a heating trend of adopting serverless architectures had be found since 2016. A sufficient understanding of the system utilization of a serverless architecture will benefit both service providers in designing architectures and application developers in making adoption decisions.

In this paper, we first describe design goals of a serverless architecture then evaluate three serverless architectures: OpenLambda, IronFunctions, and Clofly. Both OpenLambda and IronFunctions apply Docker containers with different strategies of using state operations on containers for providing application isolations, while Clofly handles requests purely by using subprocess calls. We observed that the current isolation solution costs five times more on server resource usages comparing to the one with no isolation guarantee. Also, we discussed the importance of limited resource allocations for user functions, scalable-concerned cache policies, and efficiency improvements by sharing runtime resources.

Please refer to [our paper](serverless.pdf) for details.
