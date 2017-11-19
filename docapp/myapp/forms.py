from django import forms
from myapp.models import UserModel, PostModel


class LoginForm(forms.ModelForm):
    class Meta:
        model = UserModel
        fields = ['username', 'password']


class SignUpForm(forms.ModelForm):
    class Meta:
        model = UserModel
        fields = ['email', 'username', 'name', 'password']


class PostForm(forms.ModelForm):
    class Meta:
        model = PostModel
        fields = ['image', 'heading', 'definition']
