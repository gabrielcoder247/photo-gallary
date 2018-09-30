
## Photo Gallery is a simple web application that allows user to views picture/images on category and also search for pictures/images.Basically it is a Photo Album
### september, 30th,  2018
#### By **[GABRIEL NWACHUKWU](https://github.com/gabrielcoder247)**

## Description
Photo gallery is a simple photo- album application

    1. View picture/images
    2. View picture/images base on category
    3. Search for pictures/images
    4. Copy the link of the picture/image to other sources
    5.Admin panel to manage the database
    


## Specifications
Get the specs [here](https://github.com/gabrielcoder247/photo-gallary/blob/master/SPECS.md)

## Set-up and Installation

### Prerequiites
    - Python 3.6
    - Ubuntu software
    -Django 
    

### Clone the Repo
Run the following command on the terminal:
`git clone https://github.com/gabrielcoder247/photo-gallary && cd gallary on your machine terminal`

Install [Postgres](https://www.postgresql.org/download/)

### Create a Virtual Environment
Run the following commands in the same terminal:
`sudo apt-get install python3.6-venv`
`python3.6 -m venv virtual`
`source virtual/bin/activate, to activate the virtual environment`

### Install dependancies
Install dependancies that will create an environment for the app to run
`pip3 install -r requirements`


### Run Database Migrations
```
python manage.py makemigration <appname>
python manage.py  migrate 
```

### Running the app in development
In the same terminal type:
`python3 manage.py server`

Open the browser on `http://localhost:8000/`

## Known bugs
SQLAlchemy errors, automatic sign out has a short time span

## Technologies used
    - Python 3.6
    - HTML
    - Bootstrap 4
    - JavaScript
    - Heroku
    - Postgresql
    -Django

## Support and contact details
Contact me on gabrielcoder@gmail.com for any comments, reviews or advice.

### License
Copyright (c) **Gabriel Nwachukwu**