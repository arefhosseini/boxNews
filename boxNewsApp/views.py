from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
import random, string
from django.contrib.auth.models import User
from .forms import CaptchaForm, UserForm, varzeshCommentForm, gameCommentForm, movieCommentForm, musicCommentForm
from .models import Profile
from django.core.mail import send_mail
from .manageDB import controlDb, controlData


def home(request):
    return render_to_response('home.html', {'user': request.user})


def varzesh(request, pageNumber):
    mydb = controlDb()
    pageNumber = int(pageNumber)
    cursor = mydb.db.cursor()
    cursor.execute('''SELECT username, comment FROM boxNewsApp_varzeshcomment''')
    comments = cursor.fetchall()
    commentsNumbers = len(comments)
    form = CaptchaForm()
    myData = controlData()
    cursorData = myData.db.cursor()
    cursorData.execute('''SELECT link, title, news, day, path FROM varzesh''')
    posts = cursorData.fetchmany(10 * pageNumber)
    posts = posts[(pageNumber - 1) * 10:]
    cursorData.execute('''SELECT COUNT(*) FROM varzesh''')
    allPages = cursorData.fetchone()[0]
    allPages = allPages // 10 + 1
    return render_to_response('varzesh.html', {'form': form['captcha'], 'user': request.user, 'comments': comments,
                                               'commentsNumbers': commentsNumbers, 'posts': posts,
                                               'pageNumber': pageNumber, 'nextPage': str(pageNumber + 1), 'beforePage': str(pageNumber - 1), 'allPages': allPages})


def movie(request, pageNumber):
    mydb = controlDb()
    pageNumber = int(pageNumber)
    cursor = mydb.db.cursor()
    cursor.execute('''SELECT username, comment FROM boxNewsApp_moviecomment''')
    comments = cursor.fetchall()
    commentsNumbers = len(comments)
    form = CaptchaForm()
    myData = controlData()
    cursorData = myData.db.cursor()
    cursorData.execute('''SELECT link, title, news, day, path FROM movie''')
    posts = cursorData.fetchmany(10 * pageNumber)
    posts = posts[(pageNumber - 1) * 10:]
    cursorData.execute('''SELECT COUNT(*) FROM movie''')
    allPages = cursorData.fetchone()[0]
    allPages = allPages // 10 + 1
    return render_to_response('movie.html', {'form': form['captcha'], 'user': request.user, 'comments': comments,
                                               'commentsNumbers': commentsNumbers, 'posts': posts,
                                               'pageNumber': pageNumber, 'nextPage': str(pageNumber + 1), 'beforePage': str(pageNumber - 1), 'allPages': allPages})


def music(request, pageNumber):
    mydb = controlDb()
    pageNumber = int(pageNumber)
    cursor = mydb.db.cursor()
    cursor.execute('''SELECT username, comment FROM boxNewsApp_musiccomment''')
    comments = cursor.fetchall()
    commentsNumbers = len(comments)
    form = CaptchaForm()
    myData = controlData()
    cursorData = myData.db.cursor()
    cursorData.execute('''SELECT link, title, news, day, path FROM music''')
    posts = cursorData.fetchmany(10 * pageNumber)
    posts = posts[(pageNumber - 1) * 10:]
    cursorData.execute('''SELECT COUNT(*) FROM music''')
    allPages = cursorData.fetchone()[0]
    allPages = allPages // 10 + 1
    return render_to_response('music.html', {'form': form['captcha'], 'user': request.user, 'comments': comments,
                                               'commentsNumbers': commentsNumbers, 'posts': posts,
                                               'pageNumber': pageNumber, 'nextPage': str(pageNumber + 1), 'beforePage': str(pageNumber - 1), 'allPages': allPages})


def game(request, pageNumber):
    mydb = controlDb()
    pageNumber = int(pageNumber)
    cursor = mydb.db.cursor()
    cursor.execute('''SELECT username, comment FROM boxNewsApp_gamecomment''')
    comments = cursor.fetchall()
    commentsNumbers = len(comments)
    form = CaptchaForm()
    myData = controlData()
    cursorData = myData.db.cursor()
    cursorData.execute('''SELECT link, title, news, day, path FROM game''')
    posts = cursorData.fetchmany(10 * pageNumber)
    posts = posts[(pageNumber - 1) * 10:]
    cursorData.execute('''SELECT COUNT(*) FROM game''')
    allPages = cursorData.fetchone()[0]
    allPages = allPages // 10 + 1
    return render_to_response('game.html', {'form': form['captcha'], 'user': request.user, 'comments': comments,
                                               'commentsNumbers': commentsNumbers, 'posts': posts,
                                               'pageNumber': pageNumber, 'nextPage': str(pageNumber + 1), 'beforePage': str(pageNumber - 1), 'allPages': allPages})


def send_registration_confirmation(username, confirmation_code, email):
    title = "boxNews account confirmation"
    content = "http://127.0.0.1:8000/confirm/" + str(confirmation_code) + "/" + username
    send_mail(title, content, 'boxnewsiust@gmail.com', [email], fail_silently=False)


def confirm(request, confirmation_code, username):
    try:
        user = User.objects.get(username=username)
        confirmation_code_user = Profile.objects.get(confirmation_code=confirmation_code).confirmation_code
        if confirmation_code_user == confirmation_code:
            user.is_active = True
            user.save()
            info = {'first_name': user.first_name, 'last_name': user.last_name, 'username': user.username}
            return success(request, info)
    except:
        return home(request)


@csrf_exempt
def signup(request):
    myDB = controlDb()
    if request.method == 'POST' and not request.is_ajax():
        formSignup = UserForm(request.POST)
        formCaptcha = CaptchaForm(request.POST)
        if formSignup.is_valid() and formCaptcha.is_valid():
            user = formSignup.save()
            user.set_password(user.password)
            user.is_active = False
            user.save()
            confirmation_code = ''.join(random.choice(string.ascii_letters) for i in range(32))
            profile = Profile(username=request.POST['username'], confirmation_code=confirmation_code)
            profile.save()
            send_registration_confirmation(request.POST['username'], confirmation_code, request.POST['email'])
            return render_to_response('toConfirmEmail.html')
        if not formCaptcha.is_valid():
            form = CaptchaForm()
            context = {'form': form['captcha'], 'email': request.POST['email'], 'username': request.POST['username'],
                       'first_name': request.POST['first_name'], 'last_name': request.POST['last_name'],
                       'password': '', 're_password': '', 'isValid': 'invalid'}
            return render(request, "signup.html", context)
    if request.is_ajax():
        cursor = myDB.db.cursor()
        if request.POST['input'] == 'username':
            cursor.execute('''SELECT username FROM auth_user''')
            allusername = cursor.fetchall()
            for username in allusername:
                if username[0] == request.POST['value']:
                    return HttpResponse("invalid")
            return HttpResponse("valid")
        elif request.POST['input'] == 'email':
            if "@" not in request.POST['value'] or ".com" not in request.POST['value'] and ".ir" not in request.POST[
                'value']:
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


@csrf_exempt
def sendComment(request):
    if request.method == 'POST':
        if request.POST['page'] == 'varzesh':
            formComment = varzeshCommentForm(request.POST)
        elif request.POST['page'] == 'game':
            formComment = gameCommentForm(request.POST)
        elif request.POST['page'] == 'music':
            formComment = musicCommentForm(request.POST)
        elif request.POST['page'] == 'movie':
            formComment = movieCommentForm(request.POST)
        formCaptcha = CaptchaForm(request.POST)
        if formComment.is_valid() and formCaptcha.is_valid():
            formComment.save()
            return render(request, "sentComment.html", {'info': 'نظر شما با موفقیت ثبت شد'})
        elif not formCaptcha.is_valid():
            return render(request, "sentComment.html", {'info': 'تصویر امنیتی اشتباه است'})
        else:
            return home(request)
    else:
        return home(request)


def profile(request):
    if request.user.is_authenticated():
        info = {'first_name': request.user.first_name, 'last_name': request.user.last_name,
                'username': request.user.username, 'email': request.user.email}
        return render(request, "profile.html", info)
    else:
        return home(request)