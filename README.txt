Welcome to log analysis code:

prerequests:
-python2
-psql

How the program runs:
1- connect and make sure that you can use psycopg2 on your machine
2- run the file logs-analysis.py and it will give you the results

The program design:
-this code have 4 functions used to get the results:
	1-first one is connect and it's resposible for connecting to the data base named "news"
	2-second one is mostPopulatArticles and it gets the most three popular articles
	3-third one is mostPopularAuthors and it shows the most popular authors according to thier read articles
	4-fourth and last one is precentageGRTone and it get the error requests with precentage more than 1%

create view errors_perDay as
	select date(time) as date, count(*) as num 
	from log where status = '404 NOT FOUND' 
	group by(date) 
	order by(date);

create view total_perDay as
	select date(time) as date, count(*) as total 
	from log 
	group by (date) 
	order by(date);


create view precentage as
	select errors_perDay.date,(100.0*num/total) as precentage 
	from total_perDay join errors_perDay on total_perDay.date = errors_perDay.date;

this code use python2 as mentioned in the code file

after making the views you can run the code file and everything will work well and i have provided a views.sql file so you can use it directly
