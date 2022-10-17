# Scheduler
Simple Scheduling App created by Python to solve Our *`College Problem`*

## Table Of Contents
* [Introduction](#introduction)
* [Setup](#setup)
* [Features Of The Program](#features-of-the-program)

## Introduuction
In this document we will discuss the problem that counters our college each year and takes a great effort of them to try to handle.<br />
To be more specified, it may cause them a terrible headache each semester they are trying to put an examination timetable for each division in our college in all branches (Elkhalfawy – Rodelfarag – Eloupoor) or scheduling the observers in each hall or section.<br />
So, it was a small identification to our Problem.<br /> 
Our App is divided into 3 parts *`halls distribution`*, *`Observers Scheduling`* and the *`UI (User Interface)`*.<br />
It has Some features such as it can inform the observer about the days and the times of his observation in any branch of our college.

### Problem identification
Halls Distribution and Observers Scheduling in all the existence branches of Our College.

### Objective
A computer software Program to solve this problem.

### Solution
A desktop Application using Python Language that shows the solutions to the user including the Optimal Sol with a little contribution of a user to choose one of the available solutions or to interact with the App itself. Such as Printing the Observers ExcelSheet or halls sheet or the task of each Observer.

## Setup
- download any Version for Python (We Recommended Version 3.8.10).
- download any IDE for Python (We Recommended VScode).
- open Your Terminal and Write These Instructions to download The Libraries which used.
    - pip install pyqt5
    - pip install pyqt5-tools
    - pip install QT-PyQt-PySide-Custom-Widgets
    - pip install typing_extensions
    - pip install pywin32
    - pip install pandas
    - pip install arabic_reshaper
    - pip install xlsxwriter
    - pip install tabulate
    - pip install pretty_html_table
    - pip install fpdf
    - pip install psutil
    - pip install wget
    - pip install openpyxl

## Features Of The Program

### Halls Distribution

### observers distribution over halls
*this part must be runned after the halls part<br />*
what this part do:
- take the halls data form halls part and where each degree in the collage will be examed.
- take the exam time table from the user .
- do some validation on the gathered data then start solving the problem.
- display the solution on the screen u can change things in it then save it as you like but the rightness of the anwser is on you.
- print his/her data.
- output excel all obsevers data combined.
- output pdf containing all data for all ovservers a page for each one ease to be printed !!this can last for `30 sec` at most.

### E-mail Automation by using Outlook
Another feature in our App is automated e-mails. This feature is used to send assignment schedule to every employee.<br />
E-mail automation was done by using `Outlook App` through a module in python.<br />
This feature do two main functions:
- Send an e-mail to the only chosen employee.
- Send an email to all employees at once.
- send email to all observers this can last for `2 min` at most.

