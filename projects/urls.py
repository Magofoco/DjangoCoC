from django.urls import path, include
from . import views

urlpatterns = [
    # Regarding the projects
    path('allprojects', views.allprojects, name='allprojects'),
    path('createproject', views.createproject, name='createproject'),
    path('<int:project_id>', views.projectdetail, name='projectdetail'),
    path('<int:project_id>/editproject', views.editproject, name='editproject'),
    path('<int:project_id>/deleteproject', views.deleteproject, name='deleteproject'),
    path('<int:project_id>/auditproject', views.auditproject, name='auditproject'),


    # Regarding ranking statistics for NHS
    path('nhsstatistics', views.nhsstatistics, name='nhsstatistics'),

    # Regarding the set of questions
    path('<int:project_id>/', include('initialquestions.urls')),
    path('<int:project_id>/', include('firstquestions.urls')),
    path('<int:project_id>/', include('secondquestions.urls')),
    path('<int:project_id>/', include('thirdquestions.urls')),
    path('<int:project_id>/', include('fourthquestions.urls')),
    path('<int:project_id>/', include('fifthquestions.urls')),
    path('<int:project_id>/', include('sixthquestions.urls')),
    path('<int:project_id>/', include('seventhquestions.urls')),
    path('<int:project_id>/', include('eighthquestions.urls')),
    path('<int:project_id>/', include('ninthquestions.urls')),
    path('<int:project_id>/', include('tenthquestions.urls')),

    # Regarding statistics for NHS and supplier
    path('<int:project_id>/statistics', views.statistics, name='statistics'),


]


