from django.urls import path, include
from . import views


urlpatterns = [
    path('seventhquestionstoanswer', views.seventhquestionstoanswer, name='seventhquestionstoanswer'),
    path('seventhquestionsdetail', views.seventhquestionsdetail, name='seventhquestionsdetail'),
    path('seventhquestionsedit', views.seventhquestionsedit, name='seventhquestionsedit'),
]


