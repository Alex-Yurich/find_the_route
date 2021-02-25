from django.http import HttpResponse
from django.shortcuts import render
from requests import get
from . import settings


def home(request):
    # name = 'some name that i have sent'
    ip = get('https://api.ipify.org').text
 #   print('My public IP address is: {}'.format(ip))
    if ip in settings.ALLOWED_HOSTS:
        wan_ip = ip
    else:
        wan_ip = 'hahaha'


    cont = {'name': 'name', 'ip': wan_ip}



    # return render(request, 'home.html', {'name': name, 'index': '5'})
    return render(request, 'home.html', cont)


def about(request):
    name = 'This page about us!'

    return render(request, 'about.html', {'name': name})
