from django.shortcuts import render, redirect
from django.contrib import messages
from .models import *
import random
from datetime import datetime

Buildings_Map = {
<<<<<<< HEAD
    'dungeon 1': (10,20),
    'dungeon 2': (5,10),
    'dungeon 3': (2,5),
    'dungeon 4': (0,50),
}

def index(request):
    if not 'process_money' in request.session or 'activities' not in request.session:
        request.session['process_money'] = random.randint(1, 11)

        request.session['activities'] = []
    return render(request, 'index.html')
=======
    'Shrines': (10,20),
    'Labyrinths': (5,10),
    'Hideout': (2,5),
    'Hyrule Castle': (0,50),
}

def index(request):
    return render(request, 'Log_Reg.html')
>>>>>>> master

def register(request):
    errors = User.objects.basic_validator(request.POST)
    if len(errors)>0:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect('/')
    password = request.POST['password']
    pw_hash = bcrypt.hashpw(password.encode(), bcrypt.gensalt()).decode()
    user = User.objects.create(
        first_name = request.POST['first_name'], 
        last_name = request.POST['last_name'], 
        email = request.POST['email'], 
        username = request.POST['username'],
        password = pw_hash
    ) 
    request.session['user_id'] = user.id
    return redirect('/game')

def login(request):
    errors = User.objects.login_validator(request.POST)
    if len(errors)>0:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect('/')
    else:
        user = User.objects.filter(username=request.POST['username'])
        if user:
            logged_user = user[0]
            if bcrypt.checkpw(request.POST['password'].encode(), logged_user.password.encode()):
                request.session['user_id'] = logged_user.id
                return redirect('/game')
    return redirect('/')

def game(request):
    if 'user_id' in request.session:
        context = {
            'user': User.objects.get(id=request.session['user_id']),
            'stats': Stat.objects.all(),
        }
        if not 'gold' in request.session or 'activities' not in request.session:
            request.session['gold'] = 200
            request.session['activities'] = []
        return render(request, 'index.html', context)
    return redirect('/')

def gold(request):
    if request.method == 'GET':
        return redirect('/')
    if request.method == 'POST':
        building_name = request.POST['building']
        building = Buildings_Map[building_name]
        building_name_upper = building_name[0].upper() + building_name[1:] 
        curr_gold = random.randint(building[0], building[1])
        now_formatted = datetime.now().strftime("%m/%d/%Y %I:%M%p")
        result = 'earn'
<<<<<<< HEAD
        message = f'({now_formatted}) Earned {curr_gold} rupees from the {building_name_upper}!'
        if building_name == 'dungeon 4':
=======
        message = f'({now_formatted}) Earned {curr_gold} golds from the {building_name_upper}!'
        if building_name == 'Hyrule Castle':
>>>>>>> master
            if random.randint(0,1) > 0:
                message = f' ({now_formatted}) Entered {building_name_upper} and lost {curr_gold} rupees'
                curr_gold = curr_gold * -1
                result = 'lost'
        request.session['gold'] += curr_gold
        request.session['activities'].append({"message": message, "result": result})
        return redirect('/game')

def reset(request):
    request.session.clear()
    return redirect('/game')

def edit_profile(request, id):
    if 'user_id' in request.session:
        context = {
            'user': User.objects.get(id=request.session['user_id']),
        }
        return render(request, 'edit_profile.html', context)
    return redirect('/')

def update(request, id):
    errors = User.objects.basic_validator(request.POST)
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect('/game')
    if 'user_id' in request.session:
        edit_user = User.objects.get(id=id)
        edit_user.first_name = request.POST.get('first_name')
        edit_user.last_name = request.POST.get('last_name')
        edit_user.username = request.POST.get('username')
        edit_user.email = request.POST.get('email')
        edit_user.password = request.POST.get('password')
        edit_user.save()
        return redirect('/game')
    return redirect('/')

def logout(request):
    request.session.flush()
    return redirect('/')

def delete_user(request):
    if 'user_id' in request.session:
        delete_userprofile = User.objects.all()
        delete_userprofile.delete()
        return redirect('/')
    return redirect('/')