# -*- coding: utf-8 -*-

from django.shortcuts import render
from django import forms
from django.shortcuts import render_to_response
from django.http import HttpResponse,HttpResponseRedirect
from django.template import RequestContext
from account.models import User

class UserForm(forms.Form):
    username = forms.CharField(label=' 用户名:',max_length=100,required=True)
    passworld = forms.CharField(label='  密码:',widget=forms.PasswordInput(),required=True)
    realname = forms.CharField(label='真实名字:',max_length=100,required=True)
    area=forms.CharField(label=' 营业厅:',max_length=100,required=True)

def register(request):
    if request.method == "POST":
        uf = UserForm(request.POST)
        if uf.is_valid():
            username = uf.cleaned_data['username']
            passworld = uf.cleaned_data['passworld']
            realname = uf.cleaned_data['realname']
            area = uf.cleaned_data['area']
            user = User()
            user.username = username
            user.passworld = passworld
            user.realname =realname
            user.area=area
            user.save()

            return render_to_response('success.html',{'username':username})
    else:
        uf = UserForm()
    return render_to_response('register.html',{'uf':uf})