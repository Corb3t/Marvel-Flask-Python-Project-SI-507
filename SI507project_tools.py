# from app import Traits, Stories, Superheroes, session
import csv
import marvelous
import json
import requests
from flask import Flask, render_template, session, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime as dt

#The Marvel API came back up, so I decided to try and utilize the data, along with a CSV instead of attempting to learn Plotly. I intend on pulling story data from the marvelous module, then linking it to a Superheroes db using the Superhero names from the superheroes.csv with an association table. I also plan on creating a character traits table with a one-to-one relationship.

#I should probably implement some caching since the marvelous module only returns 100 entries, so maybe I can look into doing it multiple times
public_key = "092721debb22ea64ffcf5a37b505d228"
private_key = "96c1798193a237b8ee210739dd734bd0bf2adc9c"

m = marvelous.api(public_key, private_key) # Authenticate with Marvel, with keys I got from http://developer.marvel.com/

# Application configurations
app = Flask(__name__)
app.debug = True
app.use_reloader = True
app.config['SECRET_KEY'] = 'hard to guess string for app security adgsdfsadfdflsdfsj'

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///./marvel.db' # TODO: decide what your new database name will be -- that has to go here
app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Set up Flask debug stuff
db = SQLAlchemy(app) # For database use
session = db.session # to make queries easy 

##### Set up Models #####

class Stories(db.Model):
    __tablename__ = "stories"
    story_id = db.Column(db.Integer, primary_key=True)
    story_name = db.Column(db.String(50))
    story_date = db.Column(db.Integer())
#    superheroes = db.relationship('Superheroes', backref="story") #many to many with superheroes - not very confident about this. need to implement association table (example at bottom)

#can you guys help me with this? 
#it's currently running in  if __name__ == '__main__':
#I keep getting: File "SI507project_tools.py", line 87, in <module> get_or_create_stories(pulls, session) NameError: name 'pulls' is not defined
def get_marvelous_data(m): 
    pulls = sorted(m.comics({
    'format': "comic",
    'formatType': "comic",
    'noVariants': True,
    'dateDescriptor': "thisMonth",
    'limit': 100}),
    key=lambda comic: comic.title) #puts it in order
    return pulls

def get_or_create_stories(pulls, session): #function that gets 
    for comic in pulls:
        story = Stories.query.filter_by(story_name=comic.title).first()
        # print(story)
        if not story:
            story = Stories(story_name=comic.title, story_date=comic.dates.on_sale.strftime("%Y-%m-%d"))
            session.add(story)
            session.commit()

if __name__ == '__main__':
    db.create_all() # This will create database in current directory, as set up, if it doesn't exist, but won't overwrite if you restart
    #get_marvelous_data(m)
    pulls = sorted(m.comics({
    'format': "comic",
    'formatType': "comic",
    'noVariants': True,
    'limit': 100}),
    key=lambda comic: comic.title) #orders
    get_or_create_stories(pulls, session)
    app.run() # run with this: python main_app.py runserver

#More stuff I'm working on:

def get_heroes_csv():
    hero_data = open("superheroes.csv", "r")
    csv_data = csv.reader(hero_data, delimiter=",")
    next(csv_data, None)
    return csv_data

def populate_tables(csv_data,session):
    for rows in csv_data:
    #populate superheros table
        hero_id = Superheroes(name = rows[1],
            allegiance = rows[3],
        )

    #populate traits table
        trait_ids = Traits(eye_color = rows[5],
        hair_color = rows[6],
        gender = rows[7])
        if not trait_ids:
            traits_ids = Traits() #need to still work on this.


class Superheroes(db.Model):
    __tablename__ = 'superheroes'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(65))
    allegiance = db.Column(db.String(50))
    num_appear = db.Column(db.Integer)
    first_appear = db.Column(db.Integer(50))
    stories_id = db.Column(db.Integer, db.ForeignKey("stories.story_id"))
    traits_id = db.Column(db.Integer, db.ForeignKey("traits.id"))

class Traits(db.Model): 
    __tablename__ = "traits"
    id = db.Column(db.Integer, primary_key=True)
    eye_color = db.Column(db.String(65))
    hair_color = db.Column(db.String(50)) 
    gender = db.Column(db.String(50))
    superheroes = db.relationship('Superheroes', backref="trait") #one to many relationship with Superheroes


# Many to Many Example
# Create association table above tables that exist, for clarity --
# You can also see an example of this for Artists and Albums in the Songs app example we saw before..

# performances = db.Table('performances',db.Column('song_id',db.Integer, db.ForeignKey('songs.id')),db.Column('artist_id',db.Integer, db.ForeignKey('artists.id')))

# class Song(db.Model):
#     __tablename__ = "songs"
#     id = db.Column(db.Integer, primary_key=True)
#     title = db.Column(db.String(250)) # maybe up to 250 chars long in case
#     genre = db.Column(db.String(65)) # decided no genre will be over 65 chars -- gotta be sure that's true though

# class Artist(db.Model):
#     __tablename__ = "artists"
#     id = db.Column(db.Integer, primary_key=True)
#     name = db.Column(db.String(250))
#     num_people = db.Column(db.Integer) # assuming we've got or will get this data

# Correct setup to run the app & create anything missing from db (and probably define route functions, etc) must go below...