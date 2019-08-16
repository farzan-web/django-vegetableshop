from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from django import forms
from accounts.models import Profile

class UserCreateForm(UserCreationForm):

    class Meta:
        fields = ('username','email','first_name','last_name','password1','password2')
        model = get_user_model()

    def __init__(self,*args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].label = 'User Name'
        self.fields['email'].label = "Email Address"
        self.fields['email'].required = True
        self.fields['first_name'].required = True
        self.fields['last_name'].required = True

class ProfileForm(forms.ModelForm):

    class Meta:
        model = Profile
        fields = ('state_country','address', 'phone_number')

    def __init__(self,*args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['state_country'].required = True
        self.fields['address'].required = True
        self.fields['phone_number'].required = True
        