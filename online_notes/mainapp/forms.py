from django import forms


class RegForm(forms.Form):
    username = forms.CharField(max_length=100, label='Username')
    first_name = forms.CharField(max_length=100)
    last_name = forms.CharField(max_length=100)
    email = forms.EmailField(max_length=100)
    password1 = forms.CharField(widget=forms.PasswordInput())
    password2 = forms.CharField(widget=forms.PasswordInput())

    def check_username(self):
        return len(self.cleaned_data['username']) >= 2

    def check_password(self):
        user_password1 = self.cleaned_data['password1']
        user_password2 = self.cleaned_data['password2']
        return user_password1 == user_password2
