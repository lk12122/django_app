# django_app
Simple django app to populate user activity data and display in json format.


**Introduction

This app has a custom management command that is used to populate user activity data and a view function to display all user data in json format.

**Requirements

python 3.5.2 or above 
django 2.2.13 or above

This app uses uses only libraries which comes inbuilt with python and django.

**Database

This app uses django inbuilt database sqlite3.

**Running on your own machine/server
In case, one wants to run the application on his localhost, following steps need to be followed:
1. Clone using git command - https://github.com/lk12122/django_app.git
2. enter your server ip in Allowed Hosts at file - ./django_app/assignment_project/assignment_project/settings.py
3. cd  ./django_app/assignment_project
4. use this command to run application - python manage.py runserver <yourIpAddress>:<port>
5. Hit this url in browser to view response - https://<ipAddress>:<port>/user_act/ 



**Custom Management Command

Please use below syntax to insert data in databse:
python manage.py insert_user_activity <user_id> <user_name> <user_time_zone> <user_start_time> <user_end_time>
eg: python manage.py insert_user_activity W07QCRPA4 'Glinda Southgood' Asia/Kolkata 'Feb 1 2020  1:33PM' 'Feb 1 2020 1:54PM'

If user already exists, it will update user activity else it will insert a new user along with the activity.


