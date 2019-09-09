from django.urls import path, include
from . import views

urlpatterns = [
    path('secondquestionstoanswer', views.secondquestionstoanswer, name='secondquestionstoanswer'),
    path('secondquestionsdetail', views.secondquestionsdetail, name='secondquestionsdetail'),
    path('secondquestionsedit', views.secondquestionsedit, name='secondquestionsedit'),
]

