from django.shortcuts import render, redirect, HttpResponse 
import random

# Create your views here.
def index(request):
    request.session['gold'] = 0
    request.session['activities'] = []
    return render(request, 'index.html')

def process(request):
    num1 = random.randint(10, 20)
    if request.POST['which_form'] == 'farm':
        request.session['gold'] += num1
        string = f"You Earned {num1} gold from Farm!"
        request.session['activities'].append(string)
        print(string)

    elif request.POST['which_form'] == 'cave':
        num2 = random.randint(5, 10)
        request.session['gold'] += num2
        string = f"You earned {num2} gold from cave!"
        request.session['activities'].append(string)

    elif request.POST['which_form'] == 'house':
        num3 = random.randint(2, 5)
        request.session['gold'] += num3
        string = f"You earned {num3} gold from House!"
        request.session['activities'].append(string)

    elif request.POST['which_form'] == 'casino':
        num4 = random.randint(-50, 50)
        if num4 < 0:
            request.session['gold'] += num4
            string = f"Entered a casino and lost{num4}... ouch!"
        elif num4 > 0:
            string = f"You earned {num4} from the casino!"
            request.session['gold'] += num4
        request.session['activities'].append(string)
    return render(request, 'index.html')

def complete(request):
    if 'gold' in request.session:
        del request.session['gold']
    return redirect('/')