from django.db import models
# from django.core.validators import RegexValidator
import re
import bcrypt

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
# Create your models here.
class UserManager(models.Manager):
    def register_validator(self, postData):
        errors = {}
        # First name validates length
        if len(postData['first_name']) < 2:
            errors["firstname"] = "First name must be at least 2 characters"
        # Last name validates length
        if len(postData['last_name']) < 2:
            errors["lastname"] = "Last name must be at least 2 characters"
        # Email validates length
        if len(postData['email']) < 1:
            errors["email"] = "Email cannot be empty"
        email_check  = User.objects.filter(email = postData['email'])
        # Email validate if email exits
        if email_check:
            errors["email_check"] = "Email already exits"
        # Email validates valid email
        elif not EMAIL_REGEX.match(postData['email']):
            errors['valid_email'] = "Please enter a valid email"
        # Password check length of password
        if len(postData['password']) < 8:
            errors["password"] = "Password must contain at least 9 characters"
        # Password check matching password
        if postData['password'] != postData['conf_password']: 
            errors['confpassword'] = "Passwords do not match"
        return errors 
    def login_validator(self, postData):
        errors = {}
        email = postData['email']
        users = User.objects.filter(email=email)
        if len(users) == 0:
            errors['failed'] = "failed to login"
        else:
            user = users[0]
            print(user.password)
        
            
            if bcrypt.checkpw(postData['password'].encode(), user.password.encode()):
                print("password match")
            else:
                print('--------faild tp login')
                errors['login'] = "Failed to login"
        
        
        return errors 

class User(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = UserManager()
class Item(models.Model):
    item = models.CharField(max_length=255)
    wished_by = models.ManyToManyField(User, related_name="wished_item")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)