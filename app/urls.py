from django.urls import path
from .views import *

urlpatterns = [
	path('', HomeView , name='home'),
	path('edit/<int:pk>/edit/' , detail , name ='edit')
	
]