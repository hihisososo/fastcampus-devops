from django.urls import path
from boss import views

urlpatterns = [
  path('timeinput/', views.timeinput, name='timeinput')
]