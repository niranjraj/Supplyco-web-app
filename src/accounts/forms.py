from django.contrib.auth.forms import ReadOnlyPasswordHashField
from django import forms
from store.models import Customer
from django.contrib.auth import get_user_model


User=get_user_model()

class UserAdminCreationForm(forms.ModelForm):
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput(attrs={'placeholder':'Password'}))
    password2 = forms.CharField(label='Password confirmation', widget=forms.PasswordInput(attrs={'placeholder':'ConfirmPassword'}))

    class Meta:
        model = User
        fields = ('email','aadhaar')

    def clean_password2(self):
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Passwords don't match")
        return password2

    def save(self, commit=True):

        user = super(UserAdminCreationForm, self).save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user


class UserAdminChangeForm(forms.ModelForm):
   
    password = ReadOnlyPasswordHashField()

    class Meta:
        model = User
        fields = ('email', 'aadhaar','password', 'active', 'admin')

    def clean_password(self):
        return self.initial["password"]


class LoginForm(forms.Form):
    email=forms.EmailField(label='Email',widget=forms.EmailInput(attrs={'placeholder':'Email'}))
    password=forms.CharField(widget=forms.PasswordInput(attrs={'placeholder':'Password'}))

class SignUpForm(forms.ModelForm):
    email=forms.EmailField(label='Email',widget=forms.EmailInput(attrs={'placeholder':'Email'}))
    aadhaar=forms.CharField(label='aadhaar',widget=forms.TextInput(attrs={'placeholder':'Aadhaar'}),max_length=12)
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput(attrs={'placeholder':'Password'}))
    password2 = forms.CharField(label='Password confirmation', widget=forms.PasswordInput(attrs={'placeholder':'ConfirmPassword'}))

    class Meta:
        model = User
        fields = ('email','aadhaar')

    def clean_password2(self):
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Passwords don't match")
        return password2

    def clean_aadhaar(self):
        data=self.cleaned_data.get("aadhaar")
        checkingData=Customer.objects.filter(aadhaar__contains=data)
        if not checkingData:
            raise forms.ValidationError("Passwords don't match")
        return data


    def save(self, commit=True):
        user = super(SignUpForm, self).save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.active=False;
            user.save()
        return user