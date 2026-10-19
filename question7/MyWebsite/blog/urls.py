from django.urls import path
from . import views

urlpatterns = [
    path('hello/', views.hello_django, name='hello_django'),
    path('profile/', views.profile_view, name='profile_view'),
    path('home/', views.home_view, name='home'),
    path('about/', views.about_view, name='about'),
    # Question 13 URLs
    path('books/', views.book_list, name='book_list'),
    path('form/', views.submit_form, name='submit_form'),
]