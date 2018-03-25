This readme corresponds to this project.zip file and the github repo:

LIST OF FILES:
1.project.py
2.schema SQL.pdf
3.query SQL.pdf
4.README.TXT
TOTAL NO OF FILES: 4

SYSTEM CONFIGURATION:
The system used to create this project had these configurations:
OS: ubuntu 14.04 LTS
CPU: 32 bit

SOFTWARE USED:
MySQL Version:  Ver 14.14 Distrib 5.5.59, for debian-linux-gnu (i686) using readline 6.3
Python version: Python 3.4.3
PyMySQL version: 0.8

SETUP YOUR PC AS FOLLOWS:
1. Create a mysql database with name 'exp'.
		OR
1.[NOT RECOMMENDED]change the value of 'db' in method connectToDB() with your existing database, but its NOT GUARANTEED that it will work after that as your tables can be different

2.Create tables and insert the data as shown in table schema.pdf

3.Open and edit the project.py and add your credentials like username,host,password etc. in the method connectToDB()

4.Run the script.

5.Enter The Date in given format whenever asked, it will then used to calculate a calendar month. ex:you entered 2018-03-20,it will then be used to determinig a calendar month i.e. from 2018-03-20 to 2018-02-20.

FILE DESCRIPTION:
~project.py:
This file consists the solutions in its methods for all the tasks mentioned for the fellowship.

~schema SQL.pdf:
This file contains SQL commands which can create database exp and its tables and insert some sample data into it.

~query SQL.pdf:
This file contains  SQL query that can solve the various tasks mentioned in the site, these queries are used in project.py as well, in a modified way.

~README.TXT:
this is the file you are reading now. It contains the necessary info to setup and test this project.
