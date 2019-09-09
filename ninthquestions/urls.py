from django.urls import path, include
from . import views


urlpatterns = [
    path('ninthquestionstoanswer', views.ninthquestionstoanswer, name='ninthquestionstoanswer'),
    path('ninthquestionsdetail', views.ninthquestionsdetail, name='ninthquestionsdetail'),
    path('ninthquestionsedit', views.ninthquestionsedit, name='ninthquestionsedit'),
]
