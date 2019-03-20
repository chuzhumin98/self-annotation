from django.http import HttpResponse
from django.shortcuts import render
import time

def hello(request):
    context = {}
    context['name'] = 'Python'
    return render(request, 'show.html', context)

def base(request):
    return render(request, 'base.html',
                  {
                      'cur_user': 'catfish'
                  })