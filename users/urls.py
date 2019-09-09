from django.urls import path
from .views import SignUpView, SignUpViewNHS

urlpatterns = [
    path('signup/', SignUpView.as_view(), name='signup'),
    path('signupnhs/', SignUpViewNHS.as_view(), name='signupnhs'),

]
