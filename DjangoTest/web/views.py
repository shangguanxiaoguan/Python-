import json

from django.shortcuts import render
# from __future__ import unicode_literals

from django.http.response import HttpResponse
from django.shortcuts import render

# Create your views here.


def LoginForPost(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        print(username)
        return HttpResponse(username)
    else:
        return render(request, 'login.html', context={'foo': 'bar'})


def LoginForGet(request):
    if request.method == 'GET':
        result = {}
        username = request.GET.get('username')
        mobile = request.GET.get('mobile')
        data = request.GET.get('data')
        result['user'] = username
        result['mobileNum'] = mobile
        result['data'] = data
        result = json.dumps(result)
        return HttpResponse(result, content_type='application/json;charset=utf-8')
    else:
        context = {'foo': 'bar'}
        return render(request, 'login.html', context)

