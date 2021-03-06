from django.shortcuts import render,redirect
from django.template import loader
from django import forms
from django.urls import reverse
from django.http import HttpResponse,HttpResponseRedirect
from .models import *
from .forms import *
from django.db.models import Q
from django.contrib import messages



def base(request):
	return render(request,'basic/base.html')


def create(request):
 		if(request.method=='POST'):
 			form=ProfileForm(request.POST)
 			if form.is_valid():
 				form.save()
 				messages.success(request,'User Created Successfully')
 				return render(request, 'basic/success.html',{'form':form})
 		else:
 			form=ProfileForm()
 		return render(request, 'basic/register.html',{'form':form})


def read(request):
	alldetails=Profile.objects.all()
	args={'alldetails':alldetails}
	return render(request, 'basic/details.html', args)


def detailsofuser(request, id_no):
		details=Profile.objects.filter(id_no=id_no).values()
		print(id_no)
		args={'details':details}
		return render(request, 'basic/detailsofuser.html', args)


def edituser(request, id_no):
	details=Profile.objects.get(id_no=id_no)
	if request.method == "POST":
		form = ProfileForm(request.POST, instance=details)
		if form.is_valid():
			profile = form.save(commit=False)
			profile.save()
			messages.success(request,'Informations Edited Successfully')
			return redirect('read')
		
	else:
		form=ProfileForm(instance=details)
	return render(request, 'basic/edituser.html', {'form': form})


def deleteuser(request,id_no):
	details=Profile.objects.get(id_no=id_no)
	details.delete()
	messages.success(request,'User Removed SuccessFully')
	return redirect('read')