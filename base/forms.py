from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from .models import Room, User


class MyUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'email', 'password1', 'password2']


class RoomForm(ModelForm):
    class Meta:
        model = Room
        fields = '__all__'
        exclude = ['host']


class UserForm(ModelForm):
    class Meta:
        model = User
        fields = ['avatar', 'first_name', 'last_name', 'username', 'email', 'bio']
