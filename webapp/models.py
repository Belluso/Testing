from django.db import models


# Create your models here.
class Apartment(models.Model):
    image = models.ImageField(upload_to='media/apartment', null=True)
    ApartmentNumber = models.IntegerField(blank=False)
    NumBedrooms = models.IntegerField(blank=False)
    NumBathrooms = models.IntegerField(blank=False)
    RentAmount = models.IntegerField(blank=False)
    LeaseStartDate = models.DateField(auto_now_add=True)
    LeaseEndDate = models.DateField(auto_now_add=True)


def __str__(self):
    return self.ApartmentID


class Building(models.Model):
    apartment = models.ForeignKey(Apartment, on_delete=models.SET_NULL, null=True)
    BuildingID = models.IntegerField(blank=False)


BuildingName = models.CharField(max_length=50)
Address = models.CharField(max_length=50)
NumFloors = models.IntegerField(blank=False)
YearBuilt = models.IntegerField(blank=False)
PropertyManagerID = models.IntegerField(blank=False)


def __str__(self):
    return self.BuildingID


class Tenant(models.Model):
    apartment = models.ForeignKey(Apartment, on_delete=models.SET_NULL, null=True)
    TenantID = models.IntegerField(blank=False)


FirstName = models.CharField(max_length=50)
LastName = models.CharField(max_length=50)
Email = models.CharField(max_length=50)
Phone = models.IntegerField(blank=False)
MoveInDate = models.DateField(auto_now_add=True)
MoveOutDate = models.DateField(auto_now_add=True)
ApartmentID = models.IntegerField(blank=False)


def __str__(self):
    return self.TenantID


class PropertyManager(models.Model):
    PropertyManagerID = models.IntegerField(blank=False)
    building = models.ForeignKey(Building, on_delete=models.SET_NULL, null=True)


FirstName = models.CharField(max_length=50)
LastName = models.CharField(max_length=50)
Email = models.CharField(max_length=50)
Phone = models.IntegerField(blank=False)


def __str__(self):
    return self.PropertyManagerID


class MaintenanceRequest(models.Model):
    RequestID = models.IntegerField(blank=False)
    tenant = models.ForeignKey(Tenant, on_delete=models.SET_NULL, null=True)
    apartment = models.ForeignKey(Apartment, on_delete=models.SET_NULL, null=True)


ApartmentID = models.IntegerField(blank=False)
RequestDate = models.DateField(auto_now_add=True)
Description = models.CharField(max_length=50)
Status = models.CharField(max_length=50)


def __str__(self):
    return self.RequestID
