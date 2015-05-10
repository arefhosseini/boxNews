from django.shortcuts import render_to_response
from django.template.context_processors import csrf
from .forms import SignupForm

def home(request):
    return render_to_response('home.html')


def varzesh(request):
    return render_to_response('varzesh.html')


def movie(request):
    return render_to_response('movie.html')


def music(request):
    return render_to_response('music.html')


def game(request):
    return render_to_response('game.html')


def signup(request):
    if request.method == 'POST':
        print(request.POST)
        form = SignupForm(request.POST)
        if form.is_valid():
            print('hello')
            form.save()
    c = {}
    c.update(csrf(request))
    return render_to_response("signup.html", c)
