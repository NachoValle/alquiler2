from django.contrib import admin

from .models import Cliente

class ClienteAdmin(admin.ModelAdmin):
    list_display = ('n_id','nombre','apellido')

# Register your models here.
admin.site.register(Cliente, ClienteAdmin)