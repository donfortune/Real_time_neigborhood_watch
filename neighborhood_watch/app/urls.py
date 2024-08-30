from django.urls import path, include
from . import views 
  
urlpatterns = [ 
    path('', views.index, name="index"), 
    path('alert/', views.alert, name="alert"),
    path('add_alert/', views.add_alert, name="add_alert"),
]