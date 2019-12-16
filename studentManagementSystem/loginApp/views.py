from django.shortcuts import render, redirect
from django.http import HttpResponse

from loginApp.models import  department, employee

from loginApp.functions.functions import handle_uploaded_file  

from . import forms
# Create your views here.

def index(request):
	#return HttpResponse("<h1 >Hello World</h1>")
	form=forms.FormName()

	if request.method=='POST':

		data=forms.FormName(request.POST,request.FILES)

		if data.is_valid():

			handle_uploaded_file(request.FILES['file'])  

			print("Data Are....")
			print("name is "+ data.cleaned_data['name'])
			print("email is "+ data.cleaned_data['email'])
			print("Bio is "+ data.cleaned_data['bio'])

			arr={'name':data.cleaned_data['name'],'email':data.cleaned_data['email'],'bio':data.cleaned_data['bio']}
			return render(request,'profile.html',context=arr)
			#return redirect(profile,arr)

	return render(request,'index.html',{'form':form })

def logout(request):

	ar=employee.objects.order_by('emp_name')

	arr={'arr':ar}

	#arr={'name':"Tonmoy Saha",'age':'22'}
	return render(request,'logout.html',context=arr)


def profile(request,data):


	return render(request,'profile.html',context=data)

