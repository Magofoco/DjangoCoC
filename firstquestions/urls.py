from django.urls import path, include
from . import views

urlpatterns = [
    path('firstquestionstoanswer', views.firstquestionstoanswer, name='firstquestionstoanswer'),
    path('firstquestionsdetail', views.firstquestionsdetail, name='firstquestionsdetail'),
    path('firstquestionsedit', views.firstquestionsedit, name='firstquestionsedit'),
]


