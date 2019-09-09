from django.urls import path, include
from . import views


urlpatterns = [
    path('sixthquestionstoanswer', views.sixthquestionstoanswer, name='sixthquestionstoanswer'),
    path('sixthquestionsdetail', views.sixthquestionsdetail, name='sixthquestionsdetail'),
    path('sixthquestionsedit', views.sixthquestionsedit, name='sixthquestionsedit'),
]
