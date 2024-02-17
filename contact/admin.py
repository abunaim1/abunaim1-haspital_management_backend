from django.contrib import admin
from contact.models import Contact
# Register your models here.

class ContactModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'phone', 'problem']
admin.site.register(Contact, ContactModelAdmin)