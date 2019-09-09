from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser
from crispy_forms.helper import FormHelper
from django.contrib.messages.views import SuccessMessageMixin

class CustomUserCreationForm(UserCreationForm):
  helper = FormHelper()
  class Meta(UserCreationForm):
    model = CustomUser
    fields = ('first_name', 'password1', 'username', 'email', 'last_name', 'organization', 'location', 'postcode', 'phone', 'agree_conditions', 'is_nhs')

class CustomUserChangeForm(UserChangeForm):
  class Meta(UserChangeForm):
    model = CustomUser
    fields = ('username', 'email', 'first_name', 'last_name','organization', 'location', 'postcode', 'phone', 'agree_conditions', 'is_nhs')

