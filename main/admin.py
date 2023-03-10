from django.contrib import admin
from django import forms

from .models import (
    CustomUser,
    Region,
    District, 
    Indisturial_sector,
    Speciality,
    Currency_types
)
  

@admin.register(CustomUser)
class CustomUserAdmin(admin.ModelAdmin):
    list_display = ('id', 'phone_number', 'email') 
    list_display_links = ('phone_number', 'email') 
 
@admin.register(Region)
class RegionAdmin(admin.ModelAdmin):
    list_display = ('id', 'name') 
    list_display_links = ('name',)

@admin.register(District)
class DistrictAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'region_id') 
    list_display_links = ('name',)
    list_filter = ('region_id',)
    search_fields = ('name',) 

@admin.register(Indisturial_sector)
class IndisturialSectorAdmin(admin.ModelAdmin):
    list_display = ('id', 'name') 
    list_display_links = ('name',)

@admin.register(Speciality)
class SpecialityAdmin(admin.ModelAdmin):
    list_display = ('id', 'name') 
    list_display_links = ('name',)

@admin.register(Currency_types)
class CurrencyTypesAdmin(admin.ModelAdmin):
    list_display = ('id', 'name') 
    list_display_links = ('name',) 



