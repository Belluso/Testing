from django.contrib import admin
from .models import Apartment, Building, Tenant, PropertyManager, MaintenanceRequest
# Register your models here.
admin.site.register(Apartment)
admin.site.register(Building)
admin.site.register(Tenant)
admin.site.register(PropertyManager)
admin.site.register(MaintenanceRequest)