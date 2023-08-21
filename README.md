# MSc Project
### Creator: Jemma Smith
#### Summer 2023

This web application has been produced in partial fulfillment of my MSc in Computer Science at the Univeristy of Nottingham.

This tool has been developed to allow participants to self-serve while completing a controlled experiment, which seeks to assess the impact of gamification when teaching media literacy skills as an effort to combat the spread of fake news.


To use this resource, please fork the repository and be sure to run all necesarry migrations and load the necessary data from the fixtures directory. If you do so, and then use the code as a the basis for future work, please get in touch.

Necessary Commands in GitBash or Command Prompt:
    cd mscproject
    python manage.py flush
    python manage.py makemigrations
    python manage.py migrate
    python manage.py loaddata basicapp/fixtures/quiz.json
    python manage.py loaddata basicapp/fixtures/treatments.json
    python manage.py loaddata basicapp/fixtures/tutorial.json
    python manage.py createsuperuser
     - Add name, when asked
     - Add email, when asked
     - Create password, when asked

