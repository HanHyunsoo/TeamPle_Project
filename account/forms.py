from django import forms
from .models import User


class SignUpForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput, required=True)
    check_password = forms.CharField(widget=forms.PasswordInput, required=True)
    first_name = forms.CharField(required=True, max_length=100)
    last_name = forms.CharField(required=True, max_length=50)
    email = forms.CharField(required=True)

    class Meta:
        model = User
        fields = ['username',
                  'password',
                  'check_password',
                  'email',
                  'phone_number',
                  'first_name',
                  'last_name'
                  ]

    def clean_username(self):
        check_username = self.cleaned_data['username']
        if User.objects.filter(username=check_username).exists():
            raise forms.ValidationError("아이디가 이미 사용중 입니다.")
        return check_username

    def clean_check_password(self):
        password = self.cleaned_data['password']
        check_password = self.cleaned_data['check_password']
        if password and check_password and password != check_password:
            raise forms.ValidationError("비밀번호를 다시 확인해주세요.")
        return check_password

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password"])
        if commit:
            user.save()
        return user


class SignInForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Username'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Password'}))

    class Meta:
        fields = ['username', 'password']

class UserChangeForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username','password', 'email', 'first_name', 'last_name']