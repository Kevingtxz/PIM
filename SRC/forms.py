from django.core.exceptions import ValidationError
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms

from .models import *

class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = (
            'username',
            'email',
            'password1',
            'password2',
        )
class Voteform():
    class Meta:
        model = Vote
        fields = '__all__'

class MentorFormUpdate(ModelForm):
    class Meta:
        model = Mentor
        fields = '__all__'
        exclude = ('user', 'elo', 'points_general', 'birth', 'date_created')

class RegionForm(ModelForm):
    class Meta:
        model = Region
        fields = '__all__'

class ContentForm(ModelForm):
    class Meta:
        model = Content
        fields = '__all__'
        exclude = ('poster',)

class CommentaryForm(ModelForm):
    class Meta:
        model = Commentary
        fields = '__all__'