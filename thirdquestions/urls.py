from django.urls import path, include
from . import views

urlpatterns = [
    path('thirdquestionstoanswer', views.thirdquestionstoanswer, name='thirdquestionstoanswer'),
    path('thirdquestionsdetail', views.thirdquestionsdetail, name='thirdquestionsdetail'),
    path('thirdquestionsedit', views.thirdquestionsedit, name='thirdquestionsedit'),
]

