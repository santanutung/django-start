"# django-start"
# django-start
pip install gunicorn

pip  freeze > requirements.txt


import  django_heroku
import dj_database_url

django_heroku.settings(locals())

