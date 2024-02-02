from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),

    path('about/', views.about, name="about"),

    path('services/', views.services, name="services"),

    path('contact/', views.contact, name="contact"),
   
    path('login/', views.sign_in, name="login"),
    
    path('logout', views.sign_out, name="logout"),
    
    path('service_show/<int:serviceID>', views.service_show, name="service_show"),
    
    path('service_delete/<int:serviceID>', views.service_delete, name="service_delete"),
    
    path('service_edit/<int:serviceID>', views.service_edit, name="service_edit")
]
