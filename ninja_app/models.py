from django.db import models
import re, bcrypt

username_regex = re.compile(r'')

class UserManager(models.Manager):
    def basic_validator(self, postdata):
        errors = {}
        username_checker = re.compile(r'')
        check = User.objects.filter(username=postdata['username'])
        if len(postdata['first_name']) < 2:
            errors['first_name'] = 'Your first name must be at least 2 characters'
        if len(postdata['last_name']) < 2:
            errors['last_name'] = 'Your last name must be at least 2 characters' 
        if len(postdata['username']) < 2:
            errors['username'] = 'Your username must be at least 2 characters'
        if len(postdata['password']) < 6:
            errors['password'] = 'Your password must be at least 6 characters'
        if len(postdata['email']) < 1:
            errors['email'] = 'Email cannot be blank'
        elif not username_regex.match(postdata['username']):
            errors['username'] = "Please enter a valid username."
        elif check:
            errors['username'] = 'Username is already registered'
        if postdata['password'] != postdata['confirm_password']:
            errors['password'] = 'Password and Corfirm Password do not match'
        return errors

    def login_validator(self, postdata):
        errors = {}
        check = User.objects.filter(username=postdata['username'])
        if not check:
            errors['username'] = 'Username has not been registered'
        else:
            if not bcrypt.checkpw(postdata['password'].encode(), check[0].password.encode()):
                errors['username'] = "Username and password do not match."
        return errors

class User(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    username = models.CharField(max_length=50)
    email = models.CharField(max_length=255)
    password = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = UserManager()

    def full_name(self):
        return f'{self.first_name} {self.last_name}'

    def delete_user(self):
        self.User.delete()
