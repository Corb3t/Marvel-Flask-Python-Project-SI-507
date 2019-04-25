# README.MD - SI 507 Final Project
### Description: New Modules and New Flask Routes and New APIS, oh my!
### Python Version: Python3

[Github Link] (https://github.com/Corbot5000/SI-507-Final-Project)
---

![Imgur](https://i.imgur.com/L2HUSA2.png)

---
## Project Description

SI507_final_project.py is an application that utilizes Flask, a library for Python that lets users interact with an html page to display information related to comic book heros from Marvel's API and a CSV file. The CSV and API contain data about Marvel superheroes, including their biography information, number of appearances, and upcoming stories they're featured in. Users can search for a specific hero, view all of them, or get a random hero using the flask routes outlined below.

## How to Run

1. Install the requirements from requirements.txt by running the following code in your terminal: ''pip install -r requirements.txt'' 

2. Run 'SI507_final_project.py' by cd'ing to the file's folder, and running ''python 'SI507_final_project.py''

3. Once the database's tables are created, users can then access the flask routes by going to: ``http://127.0.0.1:5000/``

## How to use

1. Once you access the main flask route, users can easily enter a hero's name in the search bar. They can also click links to access all superhero data and a random superheroes data.

## Flask Routes

> **Flask Route:** http://localhost:5000 **Description:** Shows a table of contents and outline of how the routes work.

![Imgur](https://i.imgur.com/L2HUSA2.png)

> **Flask Route:** http://localhost:5000/heroes/(superhero) **Description:** Lets the user enter a superheroes name and see information about them including character traits and upcoming stories from the Marvel API. You can also search "random" to see 5 random superheroes.

![Imgur](https://i.imgur.com/7TVHuN6.png)

> **Flask Route:** http://localhost:5000/heroes/gender/(gender) **Description:** Lets the user filter by each hero's gender

![Imgur](https://i.imgur.com/Jurdga4.png)

> **Flask Route:** http://localhost:5000/stories/all **Description:** Gives the user a list of upcoming comics

## How to run tests
1. First, cd to the main directory of the project
2. Run SI507_final_project.py to create a database
3. run SI507_project_tests.py to run unit tests

## Files Included
- SI507_final_project.py
- SI507_project_tests.py
- README.md
- requirements.txt
- superheroes.csv
- Marvel DB Diagram.png
- DB Example
    - marvel.db
- static
    - logo.jpg
    - js
        - index.js
- templates
    - hero_results.html
    - index.html

---
## Requirements.txt / Dependencies

The following dependencies were ran in a virtualenv for the python files included in this repo:

- certifi==2019.3.9
- chardet==3.0.4
- Click==7.0
- Flask==1.0.2
- Flask-SQLAlchemy==2.4.0
- idna==2.8
- itsdangerous==1.1.0
- Jinja2==2.10.1
- MarkupSafe==1.1.1
- marshmallow==2.19.2
- marvelous==1.0.4
- requests==2.21.0
- SQLAlchemy==1.3.3
- urllib3==1.24.2
- Werkzeug==0.14.1


### General
-  [x] Project is submitted as a Github repository
-  [x] Project includes a working Flask application that runs locally on a computer
-  [x] Project includes at least 1 test suite file with reasonable tests 
in it.
-  [x] Includes a `requirements.txt` file containing all required modules 
to run program
-  [x] Includes a clear and readable README.md that follows this template
-  [x] Includes a sample .sqlite/.db file
-  [x] Includes a diagram of your database schema
-  [x] Includes EVERY file needed in order to run the project
-  [x] Includes screenshots and/or clear descriptions of what your project should look like when it is working

### Flask Application
-  [X] Includes at least 3 different routes
-  [X] View/s a user can see when the application runs that are 
understandable/legible for someone who has NOT taken this course
-  [X] Interactions with a database that has at least 2 tables
-  [X] At least 1 relationship between 2 tables in database
-  [X] Information stored in the database is viewed or interacted with in some way

### Additional Components (at least 6 required)
-  [X] Use of a new module
-  [ ] Use of a second new module
-  [ ] Object definitions using inheritance (indicate if this counts for 2 
or 3 of the six requirements in a parenthetical)
-  [X] A many-to-many relationship in your database structure
-  [X] At least one form in your Flask application
-  [ ] Templating in your Flask application
-  [X] Inclusion of JavaScript files in the application
-  [X] Links in the views of Flask application page/s
-  [ ] Relevant use of `itertools` and/or `collections`
-  [ ] Sourcing of data using web scraping
-  [ ] Sourcing of data using web REST API requests
-  [X] Sourcing of data using user input and/or a downloaded .csv or .json 
dataset
-  [ ] Caching of data you continually retrieve from the internet in some way

### Submission
-  [X] I included a link to my GitHub repository with the correct 
permissions on Canvas! (Did you though? Did you actually? Are you sure you didn't forget?)
-  [X] I included a summary of my project and how I thought it went in my Canvas submission!