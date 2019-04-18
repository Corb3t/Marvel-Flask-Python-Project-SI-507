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

