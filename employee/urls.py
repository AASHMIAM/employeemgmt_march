from django.urls import path
from employee import  views
urlpatterns=[
    path("index/",views.LoginView.as_view()),
    path("signup/",views.RegistrationView.as_view())
]