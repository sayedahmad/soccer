# Soccer Game App

Soccer Game app allow you to register teams, players and match. With the help of this app you can record a team matchs, view the team rank based on its scores throughout the matchs. The app is also able to suggest teams based on players strength.

## Sub application
This project have the following applications

1. Match
2. Team 
3. Player
4. Soccer_Game (used only for home page)
5. soccer:  The main project app includes (setting, urls)

## How to run the application

1. clone the project with `git clone https://github.com/ssahim/soccer.git`
2. `cd soccer`
3. create the python3 virtual environment with `python3 -m venv .`
4. Activate the virtual environment with `source bin/activate`
5. install the requirements `pip install -r requirements.txt`
6. perform `python src/manage.py makemigrations` and ` python src/manage.py migrate` to populate the database.
7. run the application with `python src/manage.py runserver`
8. open the browser and navigate to `localhost:8000`


**Note**

I have included cdn for bootstrap and javascript. if there is no internet then you might experience problems