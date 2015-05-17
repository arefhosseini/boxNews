from django.contrib.auth.models import AnonymousUser
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.template.context_processors import csrf
from .forms import SignupForm, CaptchaForm, UserForm
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from .manageDB import controlDb
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required


def home(request):
    return render_to_response('home.html', {'user': request.user})


def varzesh(request):
    return render_to_response('varzesh.html', {'user': request.user})


def movie(request):
    return render_to_response('movie.html', {'user': request.user})


def music(request):
    return render_to_response('music.html', {'user': request.user})


def game(request):
    return render_to_response('game.html', {'user': request.user})


@csrf_exempt
def signup(request):
    myDB = controlDb()
    if request.method == 'POST' and not request.is_ajax():
        print(request.POST)
        formSignup = UserForm(request.POST)
        formCaptcha = CaptchaForm(request.POST)
        if formSignup.is_valid() and formCaptcha.is_valid():
            user = formSignup.save()
            user.set_password(user.password)
            user.save()
            info = {'first_name': request.POST['first_name'], 'last_name': request.POST['last_name'],
                    'username': request.POST['username']}
            return success(request, info)
        if not formCaptcha.is_valid():
            print('captcha is not valid :D')
            form = CaptchaForm()
            context = {'form': form['captcha'], 'email': request.POST['email'], 'username': request.POST['username'],
                       'first_name': request.POST['first_name'], 'last_name': request.POST['last_name'],
                       'password': '', 're_password': '', 'isValid': 'invalid'}
            return render(request, "signup.html", context)
    if request.is_ajax():
        cursor = myDB.db.cursor()
        print(request.POST['input'])
        if request.POST['input'] == 'username':
            cursor.execute('''SELECT username FROM auth_user''')
            allusername = cursor.fetchall()
            for username in allusername:
                if username[0] == request.POST['value']:
                    return HttpResponse("invalid")
            return HttpResponse("valid")
        elif request.POST['input'] == 'email':
            if "@" not in request.POST['value'] or ".com" not in request.POST['value'] and ".ir" not in request.POST['value']:
                return HttpResponse("invalid")
            cursor.execute('''SELECT email FROM auth_user''')
            allEmail = cursor.fetchall()
            for email in allEmail:
                if email[0] == request.POST['value']:
                    return HttpResponse("repetitive")
            return HttpResponse("valid")
    if request.method == 'GET':
        form = CaptchaForm()
        context = {'form': form['captcha'], 'email': '', 'username': '',
                   'first_name': '', 'last_name': '',
                   'password': '', 're_password': ''}
        return render(request, "signup.html", context)


@csrf_exempt
def login_user(request):
    print(request.user)
    context = RequestContext(request)
    if request.method == "GET":
        return render_to_response('login.html', {'user': request.user})
    elif request.method == "POST":
        """myDB = controlDb()
        cursor = myDB.db.cursor()
        cursor.execute('''SELECT username , password FROM boxNewsApp_signup WHERE username=?''',
                       (request.POST['username'],))
        user = cursor.fetchone()"""
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        print(user, type(user))
        if user:
            if user.is_active:
                login(request, user)
                return render_to_response('varzesh.html', {'user': request.user})
            else:
                return render_to_response('login.html', {'info': 'disabled'}, context)
        else:
            return render_to_response('login.html', {'info': 'invalid'}, context)


@login_required()
def exituser(request):
    logout(request)
    return HttpResponseRedirect('/')


def success(request, info={}):
    if info == {}:
        return signup(request)
    return render(request, "success.html", info)