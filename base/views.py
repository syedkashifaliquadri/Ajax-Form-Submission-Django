from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
# from .models import Post

def add_email(request):
    if request.method == 'GET':
        email = request.GET['email']
        return HttpResponse('Success')