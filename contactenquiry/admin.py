from django.contrib import admin
from contactenquiry.models import contactEnquiry

# Register your models here.

class ContactAdmin(admin.ModelAdmin):
    contect_info=('name','email','phone','message')


admin.site.register(contactEnquiry,ContactAdmin)