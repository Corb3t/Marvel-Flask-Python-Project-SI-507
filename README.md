# README.MD - SI 507 Final Project
### Description: New Modules and New Flask Routes and New APIS, oh my!
### Python Version: Python3
---

---
## Description
SI507_final_project.py is an application that utilizes Flask, a library for Python that lets users interact with an html page to display information related to comic book heros from Marvel's API and a CSV file.

## Flask Routes

> **Flask Route:** http://localhost:5000 **Description:** Shows a table of contents and outline of how the routes work.

> **Flask Route:** http://localhost:5000/(superhero name) **Description:** Lets the user enter a superheroes name and see information about them including character traits and first appearances

> **Flask Route:** http://localhost:5000/(superhero)/stories **Description:** Gives the user a list of upcoming comics that a specific superhero will be appearing in

> **Flask Route:** http://localhost:5000/stories/all **Description:** Gives the user a list of upcoming comics

## Files Included
1. **SI507_final_project.py:** Utilized to create the database and populate it with csv data and data from the marvelous API, and run the flask module.

2. **templates** Contains the flask route html files.

7. **requirements.txt:** The installed python modules that are required to run this project.

---
## Required Modules

Marvelous can be installed by running the command:

> $ pip3 install marvelous

Further information can be found at https://marvelous.readthedocs.io/en/latest/


---
## Requirements.txt / Dependencies

The following dependencies were ran in a virtualenv for the python files included in this repo:


- astroid==2.2.5
- beautifulsoup4==4.7.1
- bs4==0.0.1
- future==0.17.1
- isort==4.3.16
- lazy-object-proxy==1.3.1
- mccabe==0.6.1
- pyglet==1.3.2
- pylint==2.3.1
- six==1.12.0
- soupsieve==1.9
- typed-ast==1.3.1
- virtualenv==16.4.3
- wrapt==1.11.1


Below is a list of the requirements listed in the rubric for you to copy 
and paste.  See rubric on Canvas for more details.
### General
-  [ ] Project is submitted as a Github repository
-  [ ] Project includes a working Flask application that runs locally on a 
computer
-  [ ] Project includes at least 1 test suite file with reasonable tests 
in it.
-  [ ] Includes a `requirements.txt` file containing all required modules 
to run program
-  [ ] Includes a clear and readable README.md that follows this template
-  [ ] Includes a sample .sqlite/.db file
-  [ ] Includes a diagram of your database schema
-  [ ] Includes EVERY file needed in order to run the project
-  [ ] Includes screenshots and/or clear descriptions of what your project 
should look like when it is working
### Flask Application
-  [ ] Includes at least 3 different routes
-  [ ] View/s a user can see when the application runs that are 
understandable/legible for someone who has NOT taken this course
-  [ ] Interactions with a database that has at least 2 tables
-  [ ] At least 1 relationship between 2 tables in database
-  [ ] Information stored in the database is viewed or interacted with in 
some way
### Additional Components (at least 6 required)
-  [X] Use of a new module
-  [ ] Use of a second new module
-  [ ] Object definitions using inheritance (indicate if this counts for 2 
or 3 of the six requirements in a parenthetical)
-  [X] A many-to-many relationship in your database structure
-  [ ] At least one form in your Flask application
-  [ ] Templating in your Flask application
-  [ ] Inclusion of JavaScript files in the application
-  [X] Links in the views of Flask application page/s
-  [ ] Relevant use of `itertools` and/or `collections`
-  [ ] Sourcing of data using web scraping
-  [ ] Sourcing of data using web REST API requests
-  [X] Sourcing of data using user input and/or a downloaded .csv or .json 
dataset
-  [ ] Caching of data you continually retrieve from the internet in some 
way
### Submission
-  [ ] I included a link to my GitHub repository with the correct 
permissions on Canvas! (Did you though? Did you actually? Are you sure 
you didn't forget?)
-  [ ] I included a summary of my project and how I thought it went **in 
my Canvas submission**!