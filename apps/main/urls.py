from apps.main import views 
from django.urls import path
 
urlpatterns = [
    path('', views.home, name='home'),
]