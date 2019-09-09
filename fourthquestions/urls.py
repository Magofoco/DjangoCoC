from django.urls import path, include
from . import views


urlpatterns = [
    path('fourthquestionstoanswer', views.fourthquestionstoanswer, name='fourthquestionstoanswer'),
    path('fourthquestionsdetail', views.fourthquestionsdetail, name='fourthquestionsdetail'),
    path('fourthquestionsedit', views.fourthquestionsedit, name='fourthquestionsedit'),
]
