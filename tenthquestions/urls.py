from django.urls import path, include
from . import views


urlpatterns = [
    path('tenthquestionstoanswer', views.tenthquestionstoanswer, name='tenthquestionstoanswer'),
    path('tenthquestionsdetail', views.tenthquestionsdetail, name='tenthquestionsdetail'),
    path('tenthquestionsedit', views.tenthquestionsedit, name='tenthquestionsedit'),
]
