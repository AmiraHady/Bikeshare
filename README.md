# Bikeshare
### Data exploration:
* Udacity Data Analyst Nanodegree project.

### Overview:
* In this project I make use of Python to explore data related to bike share systems for three major cities in the United States—Chicago, New York City, and Washington.
I write code to import the data and answer interesting questions about it by computing descriptive statistics.
I also write a script that takes in raw input to create an interactive experience in the terminal to present these statistics.

### software requirements:
* You should have Python 3, NumPy, and pandas installed using Anaconda
* Text editor, like Atom.
* Terminal application.

### The Datasets:
All three of the data files contain the same core six (6) columns:
* Start Time 
* End Time 
* Trip Duration 
* Start Station 
* End Station 
* User Type 
The Chicago and New York City files also have the following two columns:
* Gender
* Birth Year

### Data Files:
* chicago.csv
* new_york_city.csv
* washington.csv

### Application details:
* Frist it will ask user to chose : 
  *  which city would you like to see its data?
  *  would you like to filter data by month and day or not at all?
* Second the application calculate all statistics and show up results.
* Third ask user if he  Would like to display 5 rows of individual trip data?
* Finally ask user if he Would like to restart?

### Statistics information:
* Popular times of travel: 
  * most common month
  * most common day of week
  * most common hour of day
* Popular stations and trip:
  * most common start station
  * most common end station
  * most common trip from start to end 
* Trip duration:
  * total travel time
  * average travel time
* User info:
  * counts of each user type
  * counts of each gender (only available for NYC and Chicago)
  * earliest, most recent, most common year of birth (only available for NYC and Chicago)

### To Run the application:
* Frist install python and (Numpy, Pandas libraries)
* Second open the terminal and run (python bikeshare.py)
