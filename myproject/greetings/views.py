from django.shortcuts import render
from django.http import HttpResponse

def welcome(request):
    return HttpResponse("Welcome to faiyaz's website!")

def greet_user(request, username):
    return HttpResponse(f"Hello, {username}!")

def farewell_user(request, username):
    return HttpResponse(f"Goodbye, {username}!")