# Data Representation - ATU Winter 2022
# Big Project - RESTful APIs
# Lecturer: Andrew Beatty
# Author: Ross Downey (G00398275)
***
***
<br>
This repository was created to submit the required project for Data Representation module of the Higher Diploma in Data Analytics in ATU.
The project consists of the creation of a Flask Application that has a RESTful API. <br>
The Flask Application links to one SQL database called 'nflstats'. Contained in this database are two tables. <br>
The two tables are data from quarterbacks in the NFL in 2022, and data from running backs.<br>
A web page was also created to consume the API, and the project has been hosted on python anywhere.<br>
***

## Running the application
1. The app can be run by cloning this repo from github on CMDER or another console emulator (git clone https://github.com/G00398275/DR_Project.git")<br>
2. Download and install [ANACONDA](https://www.anaconda.com/) to run Python code.<br>
3. Flask can then be used to run on a local host. Refer to [Flask](https://flask.palletsprojects.com/en/2.2.x/) for a user guide.
4. The app has also been hosted on python anywhere. See http://datarepg00398275.pythonanywhere.com/main2.html for online hosting. <br>
***

### SQL
The data has been added to a SQL database called 'nflstats' on my machine. <br>
Running the code should also add this database to a local machine if required. <br>
An example of one of the database tables is given below. <br>
The user name for SQL is "root" and the password is blank (just press enter)<br>

![](https://github.com/G00398275/DR_Project/blob/main/static_pages/images/QBTableImage.JPG)<br>


### Python Anywhere
The web page has also been hosted on python anywhere for ease of access. The link is given above.<br>
A screenshot of the web page as seen on python anywhere can be seen below.<br>

![](https://github.com/G00398275/DR_Project/blob/main/static_pages/images/webPage.JPG)<br>
***

## Process
The file nflDAO2.py was created first in this project. In this file a number of different classes were created <br>
in the object oriented style of programming in order to create the required database and tables. <br>
The database created was called 'nflstats', it contains statistics from players in the NFL league. <br>
Contained within this database are two tables 'qbtable'(Statistics for Quarterbacks) and <br>
'rbtable' (Statistics for Running Backs). Each table has values relevant to each type of player. <br>
The QB table has columns for the player's name, team, passing yards, touchdowns (TDs) and <br>
Interceptions(INTs, not to be confused with integers, although the value is an integer...). <br>
The RB table also has columns for the player's name and team, the yards are for rushing yards, <br>
instead of passing yards. There are also columns for rushing attempts (ATTs) and touchdowns (TDs). <br>
<br>
The commands for creating these tables are for use in SQL. Following the creation of all of the objects <br>
required in the nfl_DAO class the code can be run and data for 10 players in each position will be added <br>
to the two tables.<br>
Other commands are located in this code such as updating, deleting, creating a new player etc. <br>
These can be commented out or amended as required. <br>
<br>
Following this the file 'rest_server2.py was created. This file contains the flask server needed <br>
to host the tables on the internet. This can be done using a local server in virtual environment <br>
(create virtual environment on CMDER for example, and use the http address given) or the page can be hosted <br>
online using python anywhere for example (more on this later).<br>
Contained within the flask server file are CRUD (Create, Read, Update, Delete) commands for the web page. <br>
These can also be tested using CURL functions on CMDER for example (examples of these are given as <br>
comments in the code) or using Postman (API platform for using APIs, [POSTMAN](https://www.postman.com/))<br>
<br>
The file main2.html was then created to design the web page itself. In this file the tables were created <br>
again to be popualted by the SQL tables. The layout was made to look appealing using bootstrap and CSS. <br>
A number of javascript functions were then created to allow the user perform CRUD operations on the <br>
web page itself. <br>
Also, within these Javascript functions were further AJAX functions which were also used to call the <br>
data from the database. Most of the calls for these have been commented out except the ones which <br>
populate the tables. <br>
Finally, the github repository was duplicated to host the web page on python anywhere. <br>
[Pythonanywhere](https://www.pythonanywhere.com/) is an online environment and web hosting service <br>
which can be used to host web pages instead of creating the virtual environment on your local machine. <br>
This web page can be found [here](http://datarepg00398275.pythonanywhere.com/main2.html) <br>
***

## Contact
I cane be contacted at G00398275@atu.ie for any issues or queries. <br>

## End
***
***








