from django.shortcuts import render, redirect, HttpResponse
from .models import *
from django.contrib import messages
import bcrypt
from django.db.models import Q

# Create your views here.
def index(request):

    return render(request, "first_app/index.html")
def results(request):
    if 'userid' in request.session:
        id = request.session['userid']
        user = User.objects.get(id = id)

        current_user_items = Item.objects.filter(uploader_id = id)
        users_wishes = Item.objects.filter(wished_by = user)
        not_wished = Item.objects.filter(~Q(wished_by = user)).order_by("-created_at")



        context = {
            'not_wished':not_wished,
            'current_user_items':current_user_items,
            'users_wishes':users_wishes,
            'user': user,
        }

        return render(request, "first_app/results.html", context)
    else:   
        return redirect('/')

# Render Show.HTML
def addnew(request):
    if 'userid' in request.session:
        id = request.session['userid']
        user = User.objects.get(id = id)
        return render(request, "first_app/additem.html")
    else:   
        return redirect('/')

def logout(request):
    request.session.clear()
    return redirect('/')

def add_newitem(request):
    if request.method == "POST":
        if 'userid' in request.session:
            id = request.session['userid']
            user = User.objects.get(id = id)
            newitem = request.POST['newitem']

            addeditem = Item.objects.create(item = newitem, uploader = User.objects.get(id = id))

            user.wished_item.add(addeditem)
            user.save()
        
            return redirect('/results')
def show_item(request, item_id):
    if 'userid' in request.session:
        id = request.session['userid']
        user = User.objects.get(id = id)

        item = Item.objects.get(id = item_id)
        wishedby = User.objects.filter(wished_item = Item.objects.get(id = item_id))
        context={
            'item': item,
            'wishedby': wishedby
        }
        return render(request, "first_app/show.html", context)

def remove_item(request, item_id):
    if 'userid' in request.session:
        id = request.session['userid']
        user = User.objects.get(id = id)

        item = user.wished_item.get(id = item_id)
        item.delete()
        item.save()
        return redirect('/results')

def add_to_my_list(request, item_id):
    if 'userid' in request.session:
        id = request.session['userid']
        user = User.objects.get(id = id)

        item = Item.objects.get(id = item_id)
        user.wished_item.add(item)
        user.save()
        
        return redirect('/results')
def delete(request, item_id):
    if 'userid' in request.session:
        id = request.session['userid']
        user = User.objects.get(id = id)

        item = Item.objects.get(id = item_id)
        item.delete()

        
        return redirect('/results')

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