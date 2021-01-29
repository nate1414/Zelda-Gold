from django.shortcuts import render, redirect
import random
from datetime import datetime

Buildings_Map = {
    'farm': (10,20),
    'cave': (5,10),
    'house': (2,5),
    'casino': (0,50),
}

def index(request):
    if not 'process_money' in request.session or 'activities' not in request.session:
        request.session['process_money'] = 0
        request.session['activities'] = []
    return render(request, 'index.html')

def process_money(request):
    if request.method == 'GET':
        return redirect('/')
    if request.method == 'POST':
        building_name = request.POST['building']
        building = Buildings_Map[building_name]
        building_name_upper = building_name[0].upper() + building_name[1:] 
        curr_gold = random.randint(building[0], building[1])
        now_formatted = datetime.now().strftime("%m/%d/%Y %I:%M%p")
        result = 'earn'
        message = f'({now_formatted}) Earned {curr_gold} golds from the {building_name_upper}!'
        if building_name == 'casino':
            if random.randint(0,1) > 0:
                message = f' ({now_formatted}) Entered a {building_name_upper} and lost {curr_gold} golds'
                curr_gold = curr_gold * -1
                result = 'lost'
        request.session['process_money'] += curr_gold
        request.session['activities'].append({"message": message, "result": result})
        return redirect('/')

def reset(request):
    request.session.clear()
    return redirect('/')
