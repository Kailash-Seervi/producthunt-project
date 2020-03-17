from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib import auth
def signup(request):
    if request.method == 'POST':
        #User has info and wnats an account now!
        if request.POST['password1'] == request.POST['password2']:
            user = User.objects.get(usernae=request.POST['username'])
            return render()         
    else:
        #User wantd to enter info
        return render(request, 'account/signup.html')

def login(request):
  return render(request, 'account/login.html')
    

def logout(request):
    #TODO Need to route to homepage
    #and don't forget to logout
    return render(request, 'account/signup.html')
    