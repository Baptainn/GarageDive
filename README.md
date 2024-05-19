# GarageDive

## Setup
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


## Inspiration

I was inspired by local garage sales in area, thinking of the logistics of people in the community trying to interact with each other, especially during the lockdowns. I was also interested in making a web application and used that inspiration with a brief thought to make GarageDive.

## What it Does

GarageDive is able to handle account creation, item uploads, and a sleek interface to look at all the items on the marketplace currently. It interacts with a bare-bones database that can be expanded upon in the future that holds all the relevant information for the project. Community members can make an account at anytime and communicate through email that is listed on each item in order to communicate with potential buyers!

## How We Built it

Using the power of a laptop I found in my basement with the base Python IDE and Notepad++, me and my team were able to whip this project out throughout Saturday.

## Challenges We Ran into

As this is our first hackathon, we weren't sure what we were really getting into. There's a lot of say, but it takes until you actually get there to experience it. From failed project ideas and planning issues to bad equipment and never working with a proper web application before, there were many challenges that we ran into along the way. However, we used these challenges as stepping stones for our own learning and to become better coders for the future!

## Accomplishments That We're Proud Of

I'm proud that this project was able to be finished within the time limit alloted, albeit in a barebones state. I'm very proud that our team was able to learn past the hurdles along our path and make it to the end of the hackathon.

## What We Learned

Everything. A better understanding of web development and the interaction of different layers that are running within a web application. My only hope in the future is to be able to learn more in this context, perhaps for a future hackathon!

## What's Next?

For this project, it could use some more fine-tuning. I would personally remake the database in MongoDB or something similar, attempt to dockerize the entire project and run it off a webserver (eg. Apache). There are also other features to be considered, such as account authentication and chatting with other users. Better front-end development could also be achieved by adopting a web framework, such as React.js. While this project is a mere starting point, it could go so much further!

NOTE: while I didn't bother getting the domain name working, I did register the domain 'copypastewarrior.co', so I believe that deserves some credit. :)

Presentation: https://www.youtube.com/watch?v=VuzcaymkGRs
