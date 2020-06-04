# pokedex
A system that allows you to backup and delete pokemon cards.

#### Limitations
This only backs up the name and id of pokemon cards, and the search feature is not implemented

# Installation Instructions
Install Python 3

#### Python Requirements

`pip install django`

`pip install pokemontcgsdk`

#### Secret Key

As a best practice, I removed the secret key from settings.py. In order for the server to run, you'll need to generate your own secret key and store it in an environment variable called SECRET_KEY.

1. Generate your secret key here: https://djecrety.ir/
2. Set SECRET_KEY to that value. This can be configured in your run configuration in pycharm, or you can set it in your terminal with `export SECRET_KEY=<your-secret-key>`

### Database Migrations

The database is not stored the git repository either, which is another best practice. Luckily, this is easy to set up with manage.py in the ./pokedex folder.

`python manage.py migrate`

### Starting the server

Start the server with `python manage.py runserver`. The application can be accessed at http://127.0.0.1:8000/cardarchive/.
