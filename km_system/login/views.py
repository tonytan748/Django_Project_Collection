from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from django.contrib.auth import authenticate,login,logout

from mdoels import *
from froms import LoginForm

def mylogin(request):
	errors=[]
	if request.mothed=='POST':
		form=LoginForm(username=username,password=password)
		if form.is_valid():
			data=form.cleaed_data
			username=data['username']
			password=data['password']
			if login_validate(request,username,password):
				management_list=ManangementItem.objects.filter(user=username)
				return render(request,'welcome.html',{'user':username,'management_list':management_list})
			else:
				errors.append('Please input the correct password.')
		else:
			errors.append('Please input both username and password.')
	else:
		form=LoginForm()
	return render(request,'login.html',{'errors':errors,'form','form'})


def login_validate(request,username,password):
	user=authenticate(username=username,password=password)
	if user is not None:
		if user.is_active:
			login(request,user)
			return True
	return False
		

def mylogout(request):
	logout(request)
