from django.shortcuts import render
from django.urls import reverse_lazy, reverse
from django.views.generic import CreateView
from django.http import HttpResponseRedirect, HttpResponse
from accounts.models import Profile
from accounts.forms import ProfileForm

from . import forms
# Create your views here.

# class SignUp(CreateView):
#     form_class = forms.UserCreateForm
#     success_url = reverse_lazy('login')
#     template_name = 'signup.html'

def SignUp(request):

    registered = False

    if request.method == "POST":
        user_form = forms.UserCreateForm(data=request.POST)
        profile_form = ProfileForm(data=request.POST)

        if user_form.is_valid() and profile_form.is_valid():

            user = user_form.save()
            user.set_password(user.password)
            user.save()

            profile = profile_form.save(commit=False)
            profile.user = user

            profile.save()

            registered = True
            return HttpResponseRedirect(reverse_lazy('login'))
        else:
            print(user_form.errors,profile_form.errors)

    else:
        user_form = forms.UserCreateForm()
        profile_form = ProfileForm()
        
    return render(request,'signup.html',{'user_form':user_form,'profile_form':profile_form,'registered':registered})
