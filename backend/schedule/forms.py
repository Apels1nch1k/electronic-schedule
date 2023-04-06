from django import forms
from .models import User
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.core.validators import RegexValidator

class RegistrationForm(UserCreationForm):
    first_name = forms.CharField(
        max_length=30,
        widget=forms.TextInput(attrs={'autocomplete': 'text', 'placeholder': 'Введите имя', 'class' : ' focus:outline-none focus:border-sky-900 focus:ring   rounded-md px-3 border border-sky-500/50'}),
        required=False,
        validators=[RegexValidator(r'[а-яА-Я]+', "Введите имя кириллицой")]
        
    )
    last_name = forms.CharField(
        max_length=30,
        widget=forms.TextInput(attrs={'autocomplete': 'text', 'placeholder': 'Введите фамилию', 'class' : ' focus:outline-none focus:border-sky-900 focus:ring   rounded-md px-3 border border-sky-500/50'}),
        required=False,
        validators=[RegexValidator(r'[а-яА-Я]+', "Введите фамилию кириллицой")]
        )
    patronymic = forms.CharField(
        max_length=30,
        widget=forms.TextInput(attrs={'autocomplete': 'text', 'placeholder': 'Введите отечество ', 'class' : ' focus:outline-none focus:border-sky-900 focus:ring   rounded-md px-3 border border-sky-500/50'}),
        required=False,
        validators=[RegexValidator(r'[а-яА-Я]+', "Введите отечество кириллицой")]
        )
    username = forms.CharField(max_length=30, widget=forms.TextInput(attrs={'autocomplete': 'text', 'placeholder': 'Введите логин ', 'class' : ' focus:outline-none focus:border-sky-900 focus:ring   rounded-md px-3 border border-sky-500/50'}))
    password1 = forms.CharField(max_length=30, widget=forms.PasswordInput(attrs={'placeholder': 'Введите пароль ', 'class' : ' focus:outline-none focus:border-sky-900 focus:ring   rounded-md px-3 border border-sky-500/50'}))
    password2 = forms.CharField(max_length=30, widget=forms.PasswordInput(attrs={'placeholder': 'Введите пароль повторно', 'class' : ' focus:outline-none focus:border-sky-900 focus:ring   rounded-md px-3 border border-sky-500/50'}))
    group = forms.Select()
        
    def clean_password1(self):
        password = self.cleaned_data['password1']
        if password == '':
            raise forms.ValidationError('Введите пароль', code='invalid')
        return password
    
    def clean_first_name(self):
        first_name = self.cleaned_data['first_name']
        if first_name == '':
            raise forms.ValidationError('Поле пустое', code='invalid')
        return first_name
    
    def clean_last_name(self):
        last_name = self.cleaned_data['last_name']
        if last_name == '':
            raise forms.ValidationError('Поле пустое', code='invalid')
        return last_name
    
    def clean_patronymic(self):
        patronymic = self.cleaned_data['patronymic']
        if patronymic == '':
            raise forms.ValidationError('Поле пустое', code='invalid')
        return patronymic
    
    def clean_group(self):
        group = self.cleaned_data['group']
        if not group :
            raise forms.ValidationError('Поле пустое', code='invalid')
        return group
    
    class Meta(UserCreationForm.Meta):
        model = User
        fields = ('first_name', 'last_name', 'patronymic','username','password1','password2', 'group')
        
        
class SingInForms(AuthenticationForm):
    username = forms.CharField(
        label=(""),
        max_length=254,
        widget=forms.TextInput(
            attrs={
                'autocomplete': 'text',
                'placeholder': 'Логин',
                'class': 'agreedInput',
            }
        ),
        required=False
    )
    password = forms.CharField(
        label=(""),
        widget=forms.PasswordInput(
            attrs={
                "autocomplete": "current-password",
                'placeholder': 'Пароль',
                'class': 'agreedInput',
            }
        ),
        required=False
    )
    
    error_messages = {
        "invalid_login": (
            "Введите логин и пароль правильно"
        ),
    }
    

    def clean_password(self):
        password = self.cleaned_data['password']
        if password == '':
            raise forms.ValidationError('Введите пароль', code='invalid')
        return password 
    def clean_username(self):
        username = self.cleaned_data['username']
        if username == '':
            raise  forms.ValidationError('Введите логин ', code='invalid')
        if not User.objects.filter(username=username):
            raise  forms.ValidationError('Такого пользователя не существует', code='invalid')
        return username