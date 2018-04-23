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

        users_wish = Item.objects.filter(wished_by = id)
        print(users_wish.all()[0].wished_by.all()[0].first_name, "pppppppppppp")

        # context = {
        #     'users_wish':users_wish
        # }

        

        print(users_wish, "88888888888888888")
        print(users_wish, "555555555555555555")


        # wish = all_wishes[0]

        # print(wish)
        
        # get all users wishes
       
        all_wishes = Item.objects.all().order_by('-created_at') 
        all_wish = all_wishes[0].wished_by.all()[0]
        
        users = all_wishes[0].wished_by.all()
        print(users[0].first_name, "8888888888888")
        


       
        allitems = Item.objects.all()
        items = allitems[0]

        wishedby = items.wished_by.all()
        wisher = wishedby[0]



        useritems = Item.objects.filter(id = id)

        context = {
            'items': items,
            # 'wish':wish,
            'useritems': useritems,
            'wisher':wisher,
            'all_wishes': all_wishes,
            'all_wish': all_wish,
            'users_wish': users_wish,
            'users': users,
            'user': user
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

        allitems = Item.objects.filter(id = item_id)
        useritem = allitems[0]


        # all items
        
        


        wishedby = Item.objects.filter(wished_by = User.objects.filter(id = id))

        context = {
            'item': item,
            'name': name
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
            Item.objects.create(item = item)
            # get the last item created
            allitems = Item.objects.last()
            # get specific item
            item = allitems
            # assign user to item
            item.wished_by= User.objects.filter(id = id)

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