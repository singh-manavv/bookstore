from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name='index'),
    path('contact/',views.contact,name='contact'),
    path('about/',views.about,name='about'),
    path('signup/',views.signup,name='signup'),
    path('signin/',views.signin,name='signin'),
    path('categories/',views.categories,name='categories'),
    path('signout/',views.signout,name='signout'),
    path('upload_book/',views.upload_book,name='upload_book'),
    path('managebooks/',views.managebooks,name='managebooks'),
]