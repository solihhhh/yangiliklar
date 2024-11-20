from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django import forms
from blog.models import CustomUser, Comment, Article


class RegisterForm(UserCreationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'class': "form-control", 'placeholder': "Username"}))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'class': "form-control", 'placeholder': "password"}))
    password2 = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': "form-control", 'placeholder': "re-password"}))

    class Meta:
        model = CustomUser
        fields = ('username', 'password1', 'password2')

class LoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'class': "form-control", 'placeholder': "Username"}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': "form-control", 'placeholder': "password"}))

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('title',)
        widgets = {
            'title': forms.Textarea(attrs={
                'class':"form-control",
                'placeholder':"Write your comment",
                'rows':5
            })
        }

class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = ("title","description","photo","category","publish")

        widgets = {
            'title':forms.TextInput(attrs={'class':"form-control",'placeholder':"Title"}),
            'description':forms.Textarea(attrs={'class':"form-control",'placeholder':"Write description"}),
            'photo':forms.FileInput(attrs={'class':"form-control"}),
            'category':forms.Select(attrs={'class':"form-control"}),
            'publish':forms.CheckboxInput(attrs={'class':"form-control"}),
        }
