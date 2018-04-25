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

        current_user_quotes = Quote.objects.filter(uploader_id = id)
        users_fav_quotes = Quote.objects.filter(favorited_by = user)
        not_faved = Quote.objects.filter(~Q(favorited_by = user)).order_by("-created_at")



        context = {
            'not_faved':not_faved,
            'current_user_quotes':current_user_quotes,
            'users_fav_quotes':users_fav_quotes,
            'user': user,
        }

        return render(request, "first_app/results.html", context)
    else:   
        return redirect('/')

def addquote(request):
    if request.method == "POST":
        errors = User.objects.quote_validator(request.POST)
        if len(errors):
            # if the errors object contains anything, loop through each key-value pair and make a flash message
            for key, value in errors.items():
                messages.error(request, value)
            # redirect the user back to the form to fix the errors
            return redirect('/results')
        else:
            if 'userid' in request.session:
                id = request.session['userid']
                user = User.objects.get(id = id)
                quoted_by = request.POST['quoted_by']
                quote = request.POST['quote']

                addedquote = Quote.objects.create(quote = quote, quoter = quoted_by, uploader = User.objects.get(id = id))

                user.fav_quotes.add(addedquote)
                user.save()
            
                return redirect('/results')

def addtolist(request, quote_id):
    if 'userid' in request.session:
        id = request.session['userid']
        user = User.objects.get(id = id)

        quote = Quote.objects.get(id = quote_id)
        user.fav_quotes.add(quote)
        user.save()
        
        return redirect('/results')

def removefromlist(request, quote_id):
    if 'userid' in request.session:
        id = request.session['userid']
        user = User.objects.get(id = id)

        item = user.fav_quotes.get(id = quote_id)
        item.delete()
        item.save()
        return redirect('/results')

def showuser(request, user_id):
    if 'userid' in request.session:
        id = request.session['userid']
        user = User.objects.get(id = id)

        postedby = User.objects.get(id = user_id)
        # wishedby = User.objects.filter(wished_item = Item.objects.get(id = item_id))
        userquotes = Quote.objects.filter(uploader = User.objects.get(id = user_id))

        quotes = postedby.quotes.all()
        count = len(quotes)
        context={
            'userquotes': userquotes,
            'postedby': postedby,
            'count': count
        }
        return render(request, "first_app/show.html", context)






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