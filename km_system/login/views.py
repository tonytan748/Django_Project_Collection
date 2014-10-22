from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from django.contrib.auth import authenticate,login,logout

from forms import LoginForm
from models import *

def mylogin(request):
	errors=[]
	if request.method=='POST' and request.POST['username']:
		form=LoginForm(request.POST)
		if form.is_valid():
			data=form.cleaned_data
			username=data['username']
			password=data['password']
			if login_validate(request,username,password):
				try:
					itemuser=ManagementList.objects.get(itemname=username)
					management_list=ManagementItem.objects.filter(user=itemuser.id)
				except Exception as e:
					print e
					management_list=[]
				return render(request,'login/welcome.html',{'user':username,'management_list':management_list})
			else:
				errors.append('Please input the correct password.')
		else:
			errors.append('Please input both username and password.')
	else:
		form=LoginForm()
	return render(request,'login.html',{'errors':errors,'form':form})

def login_validate(request,username,password):
	user=authenticate(username=username,password=password)
	if user is not None:
		if user.is_active:
			login(request,user)
			return True
	return False
		

def mylogout(request):
	logout(request)
