from django.contrib import admin
from demoapp.models import Service
# Register your models here.

class ServiceAdmin(admin.ModelAdmin):
    list_display=('service_icon', 'service_title','service_des')

admin.site.register(Service,ServiceAdmin)