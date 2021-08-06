from django.shortcuts import render
from django.http import HttpResponse
from rango import models
from .models import Athlete, Sport, user, meda
from django.shortcuts import redirect
from django.urls import reverse
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse
from django.urls import reverse
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from datetime import datetime
from django.contrib.auth.models import User
from rango.models import UserProfile
from rango.forms import UserForm, UserProfileForm

def index(request):
    sport_list = Sport.objects.order_by('-likes')[:5]
    athlete_list = Athlete.objects.order_by('-likes')[:5]
    context_dict = {'sports': sport_list,'athletes':athlete_list}
    uname = request.POST.get('uname')  
    password = request.POST.get('password')
    if uname:
        users = user.objects.filter(email=uname)
        if not users:  
            return render(request, 'rango/login.html', {'u': 'donot have this email'})
        psw = user.objects.filter(password=password)
        if not psw:
            return render(request, 'rango/login.html', {'us': 'wrong password'})

        return render(request, 'rango/index.html', {'lucky': users})

    return render(request, 'rango/index.html',context_dict)

def sport(request):
    context_dict = {}
    sport_list = Sport.objects.all()
    context_dict = {'sports': sport_list}
   
    return render(request, 'rango/sport.html',context=context_dict)

def about(request):

    return render(request, 'rango/about.html')


def like_sport(request):
    sport_id = None
    if request.method == 'GET':
        sport_id = request.GET['sport_id']
    likes = 0
    if sport_id:
        sport = Sport.objects.get(id = int(sport_id))
        if sport:
            likes = sport.likes + 1
            sport.likes = likes
            sport.save()
    return HttpResponse(likes)

   

def register(request):
    registered = False

    if request.method == 'POST':
        user_form = UserForm(request.POST)
        profile_form = UserProfileForm(request.POST)

        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()
            profile = profile_form.save(commit=False)
            profile.user = user

            if 'picture' in request.FILES:
                profile.picture = request.FILES['picture']
            
            profile.save()
            registered = True
        else:
            print(user_form.errors, profile_form.errors)
    else:
        user_form = UserForm()
        profile_form = UserProfileForm()
    
    return render(request,
                  'rango/register.html', 
                  context={'user_form': user_form, 
                           'profile_form': profile_form, 
                           'registered': registered})



def athlete(request):
    return render(request, 'rango/athlete.html')

def contact(request):
    return render(request, 'rango/contact.html')

def collected_data(request):
    return render(request, 'rango/collected_data.html')


def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)

        if user:
            if user.is_active:
                login(request, user)
                return redirect(reverse('rango:index'))
            else:
                return HttpResponse("Your Rango account is disabled.")
        else:
            print(f"Invalid login details: {username}, {password}")
            return HttpResponse("Invalid login details supplied.")
    else:
        return render(request, 'rango/login.html')





@login_required
def user_logout(request):
    logout(request)
    return redirect(reverse('rango:index'))


def visitor_cookie_handler(request, response):
    visits = int(request.COOKIES.get('visits', '1'))

    last_visit_cookie = request.COOKIES.get('last_visit', str(datetime.now()))
    last_visit_time = datetime.strptime(last_visit_cookie[:-7], '%Y-%m-%d %H:%M:%S')

    if (datetime.now() - last_visit_time).days > 0:
        visits = visits + 1
        response.set_cookie('last_visit', str(datetime.now()))
    else:
        response.set_cookie('last_visit', last_visit_cookie)
    response.set_cookie('visits', visits)


def get_server_side_cookie(request, cookie, default_val=None):
    val = request.session.get(cookie)
    if not val:
        val = default_val
    return val


def visitor_cookie_handler(request):
    visits = int(get_server_side_cookie(request, 'visits', '1'))
    last_visit_cookie = get_server_side_cookie(request, 'last_visit', str(datetime.now()))
    last_visit_time = datetime.strptime(last_visit_cookie[:-7], '%Y-%m-%d %H:%M:%S')

    if (datetime.now() - last_visit_time).days > 0:
        visits = visits + 1
        request.session['last_visit'] = str(datetime.now())

    else:
        request.session['last_visit'] = last_visit_cookie

    request.session['visits'] = visits
