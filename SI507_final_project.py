import csv
import marvelous
import json
import random
import requests
from flask import Flask, render_template, session, redirect, url_for # tools that will make it easier to build on things
from flask_sqlalchemy import SQLAlchemy # handles database stuff for us - need to pip install flask_sqlalchemy in your virtual env, environment, etc to use this and run this

#Marvel API Keys
public_key = "092721debb22ea64ffcf5a37b505d228"
private_key = "96c1798193a237b8ee210739dd734bd0bf2adc9c"

# Application configurations
app = Flask(__name__)
app.debug = False
app.use_reloader = True
app.config['SECRET_KEY'] = 'hard to guess string for app security adgsdfsadfdflsdfsj'

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///./marvel.db' # TODO: decide what your new database name will be -- that has to go here
app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Set up Flask debug stuff
db = SQLAlchemy(app) # For database use
session = db.session # to make queries easy 

##### Set up Models #####
class Superheroes(db.Model):
    __tablename__ = 'superheroes'
    hero_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    allegiance = db.Column(db.String(50))
    eye_color = db.Column(db.Integer, db.ForeignKey("eyes.id"))
    hair_color = db.Column(db.Integer, db.ForeignKey("hair.id"))
    gender = db.Column(db.Integer, db.ForeignKey("gender.id"))
    num_appear = db.Column(db.Integer)
    first_appear = db.Column(db.Integer)

class Eyes(db.Model): 
    __tablename__ = "eyes"
    id = db.Column(db.Integer, primary_key=True)
    eye_color = db.Column(db.String(65))

class Hair(db.Model): 
    __tablename__ = "hair"
    id = db.Column(db.Integer, primary_key=True)
    hair_color = db.Column(db.String(65))

class Gender(db.Model): 
    __tablename__ = "gender"
    id = db.Column(db.Integer, primary_key=True)
    gender = db.Column(db.String(50))

class Stories(db.Model):
    __tablename__ = "stories"
    story_id = db.Column(db.Integer, primary_key=True)
    story_name = db.Column(db.String(50))
    story_date = db.Column(db.Integer())

class Battles(db.Model): #many to many table joining Stories with Superheroes
    __tablename__ = "battles"
    id = db.Column(db.Integer, primary_key=True)
    hero_id = db.Column(db.Integer, db.ForeignKey("superheroes.hero_id"))
    story_id = db.Column(db.Integer, db.ForeignKey("stories.story_id"))

##### Helper functions #####
####code inspired by db_populate.py and app.py####

def get_heroes_csv():
    hero_data = open("superheroes.csv", "r")
    csv_data = csv.reader(hero_data, delimiter=",")
    next(csv_data, None)
    return csv_data

def populateMappingTable(hero, session):
    hero_id = hero.hero_id
    hero_name = hero.name.split(" (")[0].replace('"', '').replace("'", "").replace("\\","")
    filtered_stories = session.execute('SELECT story_id FROM stories WHERE story_name LIKE "%{}%"'.format(hero_name))
    for row in filtered_stories.fetchall():
        battle = Battles(hero_id=hero_id, story_id=row[0])
        session.add(battle)
        session.commit()

def populate_tables(csv_data,session):
    for rows in csv_data:

    #populate superheros table
        hero = rows[1]
        eye_id = Eyes.query.filter_by(eye_color=rows[5]).first()
        if not eye_id:
            eye_id = Eyes(eye_color=rows[5])
            session.add(eye_id)
            session.commit()

        hair_id = Hair.query.filter_by(hair_color=rows[6]).first()
        if not hair_id:
            hair_id = Hair(hair_color=rows[6])
            session.add(hair_id)
            session.commit()

        gender_id = Gender.query.filter_by(gender=rows[7]).first()
        if not gender_id:
            gender_id = Gender(gender=rows[7])
            session.add(gender_id)
            session.commit()

        hero_id = Superheroes.query.filter_by(name=rows[1]).first()
        if not hero_id:
            hero_id = Superheroes(name=rows[1], allegiance=rows[4], num_appear=rows[10], first_appear=rows[12], hair_color=hair_id.id, eye_color=eye_id.id, gender=gender_id.id)
            session.add(hero_id)
            session.commit()

        populateMappingTable(hero_id, session)

def get_marvelous_data(m): 
    pulls = sorted(m.comics({
    'format': "comic",
    'formatType': "comic",
    'noVariants': True,
    'dateDescriptor': "thisMonth",
    'limit': 100}),
    key=lambda comic: comic.title) #puts it in order
    return pulls

def get_or_create_stories(pulls, session): #function that creates DB with Marvel API data
    for comic in pulls:
        story = Stories.query.filter_by(story_name=comic.title).first()
        # print(story)
        if not story:
            story = Stories(story_name=comic.title, story_date=comic.dates.on_sale.strftime("%Y-%m-%d"))
            session.add(story)
            session.commit()

#########################################

@app.route('/') #home route
def home():
    return render_template("index.html", title="Marvel DB")  

# Searching through DB to return Superhero data
@app.route('/heroes/<search_term>')
def hero_search(search_term):
    results = {}
    results["heroes"] = []
    if search_term == "random":
        heroes = session.execute('SELECT superheroes.name, superheroes.allegiance, superheroes.first_appear, superheroes.num_appear, eyes.eye_color, hair.hair_color, gender.gender, superheroes.hero_id FROM superheroes, hair, eyes, gender WHERE superheroes.hair_color = hair.id AND superheroes.eye_color = eyes.id AND superheroes.gender = gender.id ORDER BY random() LIMIT 5'.format(search_term))
    else:
        heroes = session.execute('SELECT superheroes.name, superheroes.allegiance, superheroes.first_appear, superheroes.num_appear, eyes.eye_color, hair.hair_color, gender.gender, superheroes.hero_id FROM superheroes, hair, eyes, gender WHERE name LIKE "%{}%" AND superheroes.hair_color = hair.id AND superheroes.eye_color = eyes.id AND superheroes.gender = gender.id'.format(search_term))
    format_stories = []
    for hero in heroes:
        stories = session.execute('SELECT stories.story_name FROM stories, battles WHERE battles.hero_id=={} AND battles.story_id = stories.story_id'.format(hero[7]))
        
        for story in stories.fetchall(): 
            format_stories.append(story[0])
        
        hero_obj = {
            "name": hero[0],
            "allegiance": hero[1],
            "eyes": hero[4],
            "hair": hero[5],
            "gender": hero[6],
            "firstAppear": hero[2],
            "numAppear": hero[3],
            "stories": ', '.join(format_stories)
        } 
        results["heroes"].append(hero_obj)
    return render_template("hero_results.html", title="MarvelDB: Results", heroes=results["heroes"], search_term=search_term)

@app.route('/heroes/gender/<gender>') #displays all heroes filtered by gender
def filter_gender(gender):
    results = {}
    results["heroes"] = []
    heroes = session.execute('SELECT superheroes.name, superheroes.allegiance, superheroes.first_appear, superheroes.num_appear, eyes.eye_color, hair.hair_color, gender.gender, superheroes.hero_id FROM superheroes, hair, eyes, gender WHERE gender.gender LIKE "%{}%" AND superheroes.hair_color = hair.id AND superheroes.eye_color = eyes.id AND superheroes.gender = gender.id'.format(gender))
    format_stories = []
    for hero in heroes:
        stories = session.execute('SELECT stories.story_name FROM stories, battles WHERE battles.hero_id=={} AND battles.story_id = stories.story_id'.format(hero[7]))
        
        for story in stories.fetchall(): 
            format_stories.append(story[0])
        
        hero_obj = {
            "name": hero[0],
            "allegiance": hero[1],
            "eyes": hero[4],
            "hair": hero[5],
            "gender": hero[6],
            "firstAppear": hero[2],
            "numAppear": hero[3],
            "stories": ', '.join(format_stories)
        } 
        results["heroes"].append(hero_obj)
    return render_template("hero_results.html", title="MarvelDB: Results", heroes=results["heroes"], search_term=gender)

if __name__ == '__main__':
    db.create_all() # This will create database in current directory, as set up, if it doesn't exist, but won't overwrite if you restart - so no worries about that
    m = marvelous.api(public_key, private_key) # Authenticate with Marvel, with keys I got from http://developer.marvel.com/
    pulls = get_marvelous_data(m)
    get_or_create_stories(pulls, session)
    get_data = get_heroes_csv()
    populate_tables(get_data, session) # Or whatever filename
    app.run() # run with this: python main_app.py runserver

