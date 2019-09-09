from django.urls import path, include
from . import views


urlpatterns = [
    path('eighthquestionstoanswer', views.eighthquestionstoanswer, name='eighthquestionstoanswer'),
    path('eighthquestionsdetail', views.eighthquestionsdetail, name='eighthquestionsdetail'),
    path('eighthquestionsedit', views.eighthquestionsedit, name='eighthquestionsedit'),
]
