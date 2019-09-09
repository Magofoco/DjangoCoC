from django.urls import path, include
from . import views

urlpatterns = [
    path('initialquestionstoanswer', views.initialquestionstoanswer, name='initialquestionstoanswer'),
    path('initialquestionsdetail', views.initialquestionsdetail, name='initialquestionsdetail'),
    path('initialquestionsedit', views.initialquestionsedit, name='initialquestionsedit'),
]
