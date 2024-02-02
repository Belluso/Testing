from django.shortcuts import render, redirect
from django.http.response import HttpResponse
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required, permission_required
from .models import *
from .forms import ApartmentForm

def home(request):
   
   apartments = Apartment.objects.all()
   context = { 
      'apartments' : apartments
   }
   return render(request,  'pages/homepage.html', context)
  
def about(request):
   return render(request, "pages/aboutpage.html")

def services(request):
   
   apartments = Apartment.objects.all()
   
   if request.method == 'POST':
      apartment_data = {
         'apartment_number' : request.POST.get('apartment_number'),
         'number_bed_rooms' : request.POST.get('number_bed_rooms'),
         'number_bath_rooms' : request.POST.get('number_bath_rooms'),
         'rent_amount' : request.POST.get('rent_amount'),
         'lease_start_date' : request.POST.get('lease_start_date'),
         'lease_end_date' : request.POST.get('lease_end_date')
      } 
      
      Apartment.objects.create(
         ApartmentNumber=apartment_data['apartment_number'],
         NumBedrooms=apartment_data['number_bed_rooms'],
         NumBathrooms=apartment_data['number_bath_rooms'],
         RentAmount=apartment_data['rent_amount'],
         LeaseStartDate=apartment_data['lease_start_date'],
         LeaseEndDate=apartment_data['lease_end_date'],
         image=request.FILES['image']
      )
      
      return redirect(to="services")
      
   context = {
      'apartments' : apartments
   }
   
   return render(request, "pages/services.html", context)

def contact(request):
   return render(request, "pages/contact.html")

def sign_in(request):
   
   if(request.user.is_authenticated):
      return redirect(to='home')
   
   if request.method == 'POST':
      
      credentials = {
         'username' : request.POST.get('username'),
         'password' : request.POST.get('password')
      }
      
      authenticated_user = authenticate(request, username=credentials['username'], password=credentials['password'])
      
      if authenticated_user is not None:
         login(request, authenticated_user);
         return redirect(to="home")
      
      return render(request, "pages/login.html")
   
   return render(request, "pages/login.html")

@login_required(login_url='login')
def service_show(request, serviceID):
   service = Apartment.objects.filter(id=serviceID).first()
   
   
   print(service)
   context = {
      'service' : service
   }
   return render(request, 'pages/service_show.html', context)

@login_required(login_url='login')
def service_delete(request, serviceID):
   service = Apartment.objects.filter(id=serviceID).first()
   service.delete()
   return redirect(to='services')

@login_required(login_url='login')
def service_edit(request, serviceID):
   service = Apartment.objects.filter(id=serviceID).first()
   context = {
      'service' : service,
      'apartment_form': ApartmentForm
   }
   if request.method == 'POST':
      apartmentForm = ApartmentForm(request.POST, request.FILES, instance=service)
      if apartmentForm.is_valid():
         apartmentForm.save()
         return redirect(to="services")
      context = {
      'service' : service,
      'apartment_form': apartmentForm
   }
      return render(request, 'pages/service_edt.html', context)
   
   return render(request, 'pages/service_edit.html', context)


@login_required(login_url='login')
def sign_out(request):
   logout(request)
   return redirect(to='home')





