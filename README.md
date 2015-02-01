#Stock trend prediction system
这是一个股票趋势预测系统，前后端分离架构。

-   前端单页面响应式设计，用的Angular
-   后端使用Django + Django ReST Framework 提供Api供前端调用
-   后端R语言实现预测算法,通过Python调用。使用ANN，SVM等机器学习算法，随机森林选择参数，时间序列预测

#Introduction
>########(The front is very simple)

-   Provide hot stocks
-   Predict stock trends(Support high concurrency, Asynchronous execution， 
Not repeat the calculation using redis cache）
-   Perform a task when the market closed calculate the predicted results
-   CORS support
-   User System(Follow stock, Registration and login)

#Requirement
-   Redis
-   Django, Django ReST Framework
-   djcelery
-   corsheaders (Provided CORS)
-   MySQL
-   Nginx(Non-essential）
-   npm, bower

#How to Start
-   cd FRONT && bower install && npm install
-   cd BACK && (With virtualenv and pip install requirement.txt)

#Demo
-   you can see the DemoPic directory

#Todo
-   Security
