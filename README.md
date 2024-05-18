# JobSeeker

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

jobseeker application

python
front-end: website (using react?)

back-end:
django?


process:

user enters website
-> landing page
-> account creation?
 -> make an account
 -> save job listings
-> search bar?
 -> job title
 -> location
 -> filter list?
 -> company?? 

when searched
-> web scraper checks reputable job listings
 -> indeed
 -> glassdoor?
 -> linked in? 
 -> etc.
-> web scaper takes appropiate information
 -> job title
 -> location
 -> company title
 -> link to actual listing
-> sorts them into a digestable list
 -> allow searchable filters
 -> date
 -> rating (if possible)
 -> some sort of algorithm to make an 'usefulness score'
-> sends it to the website
-> displays on website through a list of jobs based on filter settings
