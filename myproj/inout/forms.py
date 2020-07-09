from django.contrib.auth.forms import AuthenticationForm
from django import forms
from django.contrib.auth.models import User





class SignUpForm(forms.ModelForm):
    class Meta:
        model=User
        fields=['username','password','email','first_name','last_name']
        labels={'username':'YOUR NAME','email':'EMAIL',
        'first_name':'FIRST NAME','last_name':'LAST NAME'
        }
        widgets={
        'username':forms.TextInput(attrs={'class':'form-control','placeholder':'Enter Username',
        'style':'background-color:#bdf2f1'}),
        'password':forms.PasswordInput(attrs={'class':'form-control','placeholder':'Enter Password','style':'background-color:#bdf2f1'}),
        'email':forms.EmailInput(attrs={'class':'form-control','placeholder':'Enter Your Email','style':'background-color:#bdf2f1'}),
        'first_name':forms.TextInput(attrs={'class':'form-control','required': True,'placeholder':'First Name Please','style':'background-color:#bdf2f1'}),
        'last_name':forms.TextInput(attrs={'class':'form-control','required': True,'placeholder':'Last Name Please','style':'background-color:#bdf2f1'}),

}


class UserLoginForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super(UserLoginForm, self).__init__(*args, **kwargs)
        username = forms.EmailField(widget=forms.TextInput(
            attrs={'class': 'form-control', 'placeholder': 'hello', 'id': 'hello'}))
        password = forms.CharField(widget=forms.PasswordInput(
            attrs={
                'class': 'form-control',
                'placeholder': '',
                'id': 'hi',
                }
))
