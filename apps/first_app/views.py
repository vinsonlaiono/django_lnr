from django.shortcuts import render, redirect, HttpResponse
from .models import *
from django.contrib import messages
import bcrypt

# Create your views here.
def index(request):

    return render(request, "first_app/index.html")
def results(request):
    if 'userid' in request.session:
        id = request.session['userid']
        user = User.objects.get(id = id)
        return render(request, "first_app/results.html", {'user': user})
    else:   
        return redirect('/')

def logout(request):
    request.session.clear()
    return redirect('/')
def process(request):
    if request.method == "POST":
        errors = User.objects.register_validator(request.POST)
        if len(errors):
            # if the errors object contains anything, loop through each key-value pair and make a flash message
            for key, value in errors.items():
                messages.error(request, value)
            # redirect the user back to the form to fix the errors
            return redirect('/')
        else:
            # add the queries that will update the data base
            firstname = request.POST['first_name']
            lastname = request.POST['last_name']
            email = request.POST['email']
            password = request.POST['password']
            pw = bcrypt.hashpw(password.encode(), bcrypt.gensalt())
            conf_password = request.POST['conf_password']

            user = User.objects.create(first_name = firstname, last_name = lastname, email = email, password = pw)

            id = user.id
            print(id)
            request.session['userid'] = id
            print(request.session['userid'])

            return redirect('/results')
def login(request):
    if request.method == "POST":
        errors = User.objects.login_validator(request.POST)
        if len(errors):
            # if the errors object contains anything, loop through each key-value pair and make a flash message
            for key, value in errors.items():
                messages.error(request, value)
            # redirect the user back to the form to fix the errors
            return redirect('/')
        else:
            user = User.objects.get(email = request.POST['email'])
            id = user.id
            request.session['userid'] = id
            # add the queries that will update the data base
            
            return redirect('/results')
