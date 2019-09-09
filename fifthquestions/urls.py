from django.urls import path, include
from . import views


urlpatterns = [
    path('fifthquestionstoanswer', views.fifthquestionstoanswer, name='fifthquestionstoanswer'),
    path('fifthquestionsdetail', views.fifthquestionsdetail, name='fifthquestionsdetail'),
    path('fifthquestionsedit', views.fifthquestionsedit, name='fifthquestionsedit'),
]
