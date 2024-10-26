from django import forms
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth.models import User




class signupForm(UserCreationForm):
    email = forms.EmailField(widget=forms.EmailInput(attrs={'placeholder': 'Email','class':'w-full py-4 px-5 rounded-xl'}))

    username = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Username','class':'w-full py-4 px-5 rounded-xl'}))
    

    password1=forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Password','class':'w-full py-4 px-5 rounded-xl '}))
    password2=forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Repeat Password','class':'w-full py-4 px-5 rounded-xl'}))
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')


class loginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Username','class':'w-full py-4 px-5 rounded-xl'}))
    

    password=forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Password','class':'w-full py-4 px-5 rounded-xl '}))
    



    