
from random import choices
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms 



class NewUserForm(UserCreationForm):
    
    first_name = forms.CharField(label="Nombre",max_length=30)
    last_name = forms.CharField(label="Apellido",max_length=30)
    email = forms.EmailField(required=True)
    Choices = [('M','Male'),('F','Female')]
    like = forms.ChoiceField(widget = forms.RadioSelect,choices=Choices,label='Gender')
    
    class Meta:
        model = User
        fields = ('first_name','last_name','username','email','password1','password2','like')
        
    def save(self,commit=True):
        user = super(NewUserForm,self).save(commit=False)
        user.mail = self.cleaned_data['email']
        user.name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        user.pass1 = self.cleaned_data['password1']
        user.pass2 = self.cleaned_data['password2']
        
        if commit:
            user.save()
        return user
    