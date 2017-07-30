from django.contrib import admin
from .models import Company
from django.apps import AppConfig




class CompanyAdmin(admin.ModelAdmin):
	list_display=["__str__"]


admin.site.register(Company,CompanyAdmin)