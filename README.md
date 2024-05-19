# GarageDive

## Setup

Prepared for a Windows 10 SETUP

1. Install Python 3.12
2. Clone the repo and navigate to the folder in a command prompt.
3. Create and load an virtual environment in Python by using the following command:

`python3 -m venv venv` OR `py -m venv venv`

`.\venv\Scripts\activate`

4. Download and move the `requirements.txt` file into the correct location and install using the command below:

`pip install -r requirements.txt`

**** 

If you are a contributor and trying to update the `requirements.txt` file, use the following command to export your current virtual environment: 

`pip freeze > requirements.txt`

****

5. TBA


## Preliminary Plan

plan:

landing page:
describe the purpose of the application
make an account/log in

once logged in: (no auth required, just collect some basic information like location and login info)
be able to upload possible items to sell
be able to search through other items to sell


pages:
landing page:
-> describes the product
-> navigation
 -> sign up/log in page
 AFTER LOG IN:
  -> DASHBOARD: product search screen
  -> product list screen
  -> product creation screen
  -> product deletion screen
-> missing page

there needs to be a database that holds all of this information

database -> api???
work on making a database that can have posts and gets

run database on local machine
database = BIG ASS JSON FILE
api = python class?

structures

PRIVATE AUTHOR:
-> name
-> email (email is unique identifer)
-> password

PUBLIC AUTHOR:
-> name
-> email (hash later?)
-> location (city)
-> image?

ITEM:
-> guid
-> name
-> PUBLIC AUTHOR email
-> PUBLIC AUTHOR location
-> price
-> image

functions:
UPLOAD ITEM
uses item structure

FIND ITEMS -> later on, need to split up into groups of the pointer supplied (eg. 1, 10, 100)
uses an array of item structures

CREATE AUTHOR
uses PRIVATE AUTHOR and PUBLIC AUTHOR structure

DELETE ITEM
uses item structure

BUY ITEM
-> some process in order to purchase items?
-> if interested, provide the email to communicate