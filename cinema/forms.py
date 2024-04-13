from django import forms


class RegistrationForm(forms.Form):
    name = forms.CharField(label='姓名', max_length=100)
    gender = forms.ChoiceField(label='性别', choices=[('male', '男'), ('female', '女')])
    age = forms.IntegerField(label='年龄', min_value=1)
    contact = forms.CharField(label='联系方式', max_length=20, widget=forms.Textarea)
    username = forms.CharField(label='用户名', max_length=20, widget=forms.TextInput(attrs={'autofocus': True}))
    password = forms.CharField(label='密码', widget=forms.PasswordInput)
    confirm_password = forms.CharField(label='确认密码', widget=forms.PasswordInput)


class LoginForm(forms.Form):
    username = forms.CharField(label='用户名', max_length=20)
    password = forms.CharField(label='密码', widget=forms.PasswordInput)
