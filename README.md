# JobSeeker

## Setup

1. Install Python 3.12
2. Create and load an virtual environment in Python by typing the following in a command prompt:

`python3 -m venv local_python_environment`
`source local_python_environment/bin/activate`

4. Download and move the `requirements.txt` file into the correct location and install using the command below:

`pip install -r requirements.txt`

** If you are a contributor and trying to update the `requirements.txt` file, use the following command to export your current virtual environment: **

`pip freeze > requirements.txt`

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
