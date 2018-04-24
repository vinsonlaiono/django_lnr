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

        # get all items from user in session
        # user_items = Item.objects.filter(uploader_id = id)
        users = Item.objects.filter(uploader_id = id)
        # print(users.item, 'aaaaaaaaaa')
        # get all users items

        liked = Item.objects.filter(wished_by = user)
        not_liked = Item.objects.filter(~Q(wished_by = user))

        all_users = Item.objects.all().order_by("-created_at") 

        context = {
            'user': user,
            'users': users,
            'all_users': all_users,
            'liked': liked,
            'not_liked': not_liked
        }

        return render(request, "first_app/results.html", context)
    else:   
        return redirect('/')
def additem(request):
    if 'userid' in request.session:
        id = request.session['userid']
        user = User.objects.get(id = id)
        return render(request, "first_app/additem.html", {'user': user})
    else:   
        return redirect('/')

def show_item(request, item_id):
    if 'userid' in request.session:
        id = request.session['userid']
        user = User.objects.get(id = id)

        

        # all items

        wished_item = Item.objects.get(id = item_id)

        wishedby = User.objects.filter(wished_item = Item.objects.get(id = item_id) )

        context = {
           'wished_item': wished_item,
           'wishedby': wishedby
        }



        # create a wish list for one user
        # add an item to the users wish list.

        #adding a comment made by someone else to someones wall
        # get the user who create the item
        # show that item on the users table


        return render(request, "first_app/show.html", context)
    else:   
        return redirect('/')

def logout(request):
    request.session.clear()
    return redirect('/')

def item_process(request):
    if request.method == "POST":
        # errors = User.objects.register_validator(request.POST)
        # if len(errors):
        #     # if the errors object contains anything, loop through each key-value pair and make a flash message
        #     for key, value in errors.items():
        #         messages.error(request, value)
        #     # redirect the user back to the form to fix the errors
        #     return redirect('/')
        # else:
        if 'userid' in request.session:
            id = request.session['userid']
            user = User.objects.get(id = id)

            item = request.POST['item']


            # users_wish = Item.objects.filter(wished_by = id)
            
            # create the item
            Item.objects.create(item = item, uploader_id = id)
            # get the last item created
            allitems = Item.objects.last()
            # get specific item
            item = allitems
            # assign user to item
            item.wished_by= User.objects.filter(id = id)

            return redirect('/results')
def addmylist(request, item_id):
    if 'userid' in request.session:
        id = request.session['userid']
        user = User.objects.get(id = id)

        item = Item.objects.get(id = item_id)

        user.wished_item.add(item) 
        user.save()
        


        return redirect('/results')
def remove_item(request, item_id):
    if 'userid' in request.session:
        id = request.session['userid']
        user = User.objects.get(id = id)

        remove = user.wished_item.get(id = item_id)

        remove.delete()
        remove.save()
        


        return redirect('/results')
def delete(request, item_id):
    if 'userid' in request.session:
        id = request.session['userid']
        user = User.objects.get(id = id)

        delete = Item.objects.get(id = item_id)

        delete.delete()


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