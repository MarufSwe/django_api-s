from django.contrib import admin
from .models import *

# Register your models here.

class EmployeeAdmin(admin.ModelAdmin):
    list_display = ['name']


class ProjectAdmin(admin.ModelAdmin):
    list_display = ['name']


admin.site.register(Employee, EmployeeAdmin)
admin.site.register(Project, ProjectAdmin)