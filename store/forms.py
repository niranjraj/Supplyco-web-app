from django.forms import ModelForm
from django import forms
from store.models import Help

class HelpForm(ModelForm):
    name=forms.CharField(label='Name',widget=forms.TextInput(attrs={'placeholder':'Name'}),max_length=200)
    phoneNumber=forms.CharField(label='phoneNumber',widget=forms.TextInput(attrs={'placeholder':'phoneNumber'}),max_length=10)
    question=forms.CharField(label='question',widget=forms.TextInput(attrs={'placeholder':'question'}),max_length=200)
    description=forms.CharField(label='description',widget=forms.Textarea(attrs={'placeholder':'description'}),max_length=500)
    email = forms.EmailField(label='Email',widget=forms.EmailInput(attrs={'placeholder':'Email'}),max_length=200)
 
    class Meta:
        model = Help
        fields = ('name','phoneNumber','question','description','email')
       