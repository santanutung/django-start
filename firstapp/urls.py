
from django.urls import path,include
# from .views import home
from . import views

app_name= 'firstapp'

urlpatterns = [
    path('', views.homepage, name='home')
]

