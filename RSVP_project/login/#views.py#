from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.views import generic
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from .forms import UserForm
from django.contrib.auth.models import User

'''
def login(request):
    form_class = UserLoginForm
    template_name = 'login.html'
    
    if request.method == 'GET':
        user_login_form = form_class()
        return render(request, template_name, {'user_login_form':user_login_form})

    if request.method == 'POST':
        user_form = form_class(request.POST)
        if user_form.is_valid():
            # cleaned (normalized data)
            username = user_form.cleaned_data['User_name']
            password = user_form.cleaned_data['Password']

            # return User object if credentials are correct
            user = authenticate(username=username, password=password)
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return redirect('userhome')# change it
            return redirect('login')
'''

def register(request):
    form_class = UserForm
    template_name = 'register.html'

    if request.method == 'GET':
        user_form = form_class()
        return render(request, template_name, {'user_form':user_form})

    if request.method == 'POST':
        user_form = form_class(request.POST)
        if user_form.is_valid():
            # cleaned (normalized data)
            username = user_form.cleaned_data['User_name']
            password = user_form.cleaned_data['Password']
            email = user_form.cleaned_data['Email']

            # create a new user and save to database
            user = User.objects.create_user(username, email, password)
            user.set_password(password)
            user.save()
            # return User object if credentials are correct
            user = authenticate(username=username, password=password)
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return redirect('userhome')
                else:
                    return redirect('login')
            else:
                return redirect('login')

def user_home(request):
    template_name = 'user_home.html'
    return render(request, template_name)

'''
# Create your views here.
class UserFormView(view):
    form_class = UserForm
    tempalte_name = 'registration_form.html'

    # display registation form
    def get(self, request):
        form = self.form_class(None)
        return render(request, self.template_name, {'form':form})
    # process form data
    def post(self, request):    
        form = self.form_class(request.POST)
        if form.is_valid():
            # create an obj from form
            user = form.save(commit=False)
            # cleaned (normalized data)
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            email = form.cleaned_data['email']
            user.set_password(password)
            user.save()
            
            # return User object if credentials are correct
            user = authenticate(username=username, password=password)
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return redirect('index')# change it
'''
