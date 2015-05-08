from django.http import Http404, HttpResponse
from django.shortcuts import render_to_response
from django.shortcuts import render
from django.template import loader, Context
from boxNewsApp.models import Poll


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