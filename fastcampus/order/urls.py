from django.urls import path
from . import views

urlpatterns = [
    path('shops/', views.shop, name="shop"),
    path('menus/<int:shop>', views.menu, name="menu")
]