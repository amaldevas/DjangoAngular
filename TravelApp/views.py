from django.http import HttpResponse
from django.shortcuts import render, redirect
def name(request):
	 return HttpResponse("HAI");
def index(request):
	return render(request, 'home.html')