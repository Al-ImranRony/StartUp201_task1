from django.urls import path
from . import views


urlpatterns = [
	path('', views.indexPage, name="index"),
	path('home/', views.homePage, name="home"),
	path('register/', views.registerPage, name="register"),  
]