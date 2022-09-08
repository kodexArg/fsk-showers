# fsk-showers
This project track the use of paid showers on a fuel station in Uspallata, Mendoza (Argentina-Chile frontier).

## What am I using in this project
### Docker (50%)
A simple mariadb docker from the included _yml_ because I'm still on development. I'll put the app inside before development stage.
### Blueprints
Leaving the door open. At this point is just a mere project, but I'm planning to implement separate views for users, managers and clients, so the use of Blueprints helps me to encapsulate the reachability of each profile.
### Flask-SQLAlchemy
Obvius ORM choice for Flask. I will stop missing Django's ORM as soon as they fix intellisense for code, but w/e.
### Flask-Migrate
I still miss django at this point but Flask-Migrate does a decent job.
### Flask-Bootstrap & Flask-Moment
And that's all the time I'm willing to waste in the backend. Bootstrap v3 fills the needs of this project. 
### Config.py
A single pythonic file with Production, Staging and DevelopmentConfig from the begining.
## What I dodge (to-do)
### Testing
Test-drive development sounds like a good idea, I just didn't have enough time to study it at deep.
### Startup Scripts
At this moment this project is a draw on my board and a dream. Less poetry: I'm using Flask v2 and ATM it's icompatible with Flask-Scripts, so I'll drop some hand made scripts to set up the db and nothing more.
