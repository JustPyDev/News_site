from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path("category/<slug>/", views.category, name='category_one'),
    path("category/<slug>/", views.home, name='category_one'),
    path("category/<slug>/", views.search, name='category_one'),
    path("contact/", views.contact, name='contact'),
    path("search/", views.search, name='search'),
    path("register/", views.register, name='register'),
    path("form/", views.form, name='form')
]


