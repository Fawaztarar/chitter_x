Chitter Challenge

We are going to write a small Twitter clone that will allow the users to post messages to a public stream.

User Stories

STRAIGHT UP

As a Maker
So that I can let people know what I am doing
I want to post a message (peep) to chitter

As a maker
So that I can see what others are saying
I want to see all peeps in reverse chronological order

As a Maker
So that I can better appreciate the context of a peep
I want to see the time at which it was made

As a Maker
So that I can post messages on Chitter as me
I want to sign up for Chitter

HARDER

As a Maker
So that only I can post messages on Chitter as me
I want to log in to Chitter

As a Maker
So that I can avoid others posting messages on Chitter as me
I want to log out of Chitter

ADVANCED

As a Maker
So that I can stay constantly tapped in to the shouty box of Chitter
I want to receive an email if I am tagged in a Peep
Additional Notes

You don't have to be logged in to see the peeps.
Users sign up to chitter with their email, password, name and a username (e.g. samm@XYZ.com, password123, Sam Morgan, sjmog).
The username and email are unique.
Peeps (posts to chitter) have the name of the user and their user handle.
Your README should indicate the technologies used, and give instructions on how to install and run the tests.
Technical Approach

In the last two weeks, you integrated a database using the psycopg package and Repository classes. You also implemented small web applications using Flask, Pytest, HTML and Jinja templates to make dynamic webpages. You can continue to use this approach when building the Chitter Challenge.










READ ME FROM PREVIOUS CHALLENGE




# Flask HTML Web & Database Project Starter

This is a starter project for you to use to start your Flask HTML web & database
projects.

It contains quite a lot of example code. You can use this to see how the various
parts of the project work, or you can delete it and start from scratch.



## Setup

```shell
# Clone the repository to your local machine


# Enter the directory
; cd YOUR_PROJECT_NAME

# Install dependencies and set up the virtual environment
; pipenv install

# Activate the virtual environment
; pipenv shell

# Install the virtual browser we will use for testing
; playwright install
# If you have problems with the above, contact your coach

# Create a test and development database
; createdb YOUR_PROJECT_NAME
; createdb YOUR_PROJECT_NAME_test

# Open lib/database_connection.py and change the database names
; open lib/database_connection.py

# Seed the development database (ensure you have run `pipenv shell` first)
; python seed_dev_database.py

# Run the tests (with extra logging)
; pytest -sv

# Run the app
; python app.py
# Now visit http://localhost:5001/emoji in your browser
```

If you would like to remove the example code:

```shell
; ./remove_example_code.sh
```


<!-- BEGIN GENERATED SECTION DO NOT EDIT -->

---

