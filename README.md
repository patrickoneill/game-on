# Game on - Final Project

Here is the app, <a href="https://game-on-challenge.herokuapp.com/">click here</a>

[![Build Status](https://travis-ci.org/patrickoneill/game-on.svg?branch=master)](https://travis-ci.org/patrickoneill/game-on)

## Overview G4M3 ON
The idea behind this project is aimed toward the gaming world industry, 
with and ecommerce side to it along with an login function. The idea is 
that you can buy items from the site like clothing and other items game
related but if with an added idea that you complete in game specific challenges.

## Languages used:
- html5
- css / bootstrap
- python/ flask
- django
- javascript 
- aws (amazon web server)


### accounts
Within this app the accounts app holds the login function to the app,
with a login, register, logout and forgotten password for the user

### checkout
The checkout app has the stripe functionality linked up fo rthe ease of 
of purchasing any items in the site

### basket
With the basket app the user can add multiple item to the basket and then
checkout

### challenge
In this page the users are able to post up challenges for the admin to choose
from and hold a competition on the page for some discounted items,
the user will have to have proof of what they have achieved using youtube and 
twitch

### templates
Using the templates ability of django I created the base.html page and
then used the extends function to keep the rest of the site the same just using 
small amounts of code on each page

### settings.py
Used for the setting up of the enironments and secret keys, the naming of the app
that are to be approved in the site. linking in the static, media and AWS file 
location for the setting to be loaded from

### urls.py
In these file the urls for each page was created and them in the main urls.py were 
all linked in using the include() function. Makes creating the link for pages a
lot easier for naming usong the {% url '< name here>' %}

### travis
Used travis to check that the app was building correctly

### heroku
Heroku was used to deploy the app
