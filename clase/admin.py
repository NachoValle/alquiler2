from django.contrib import admin
from .models import Grupo
class GrupoAdmin(admin.ModelAdmin):
    list_display = ('grupo','ciudad','descripcion')

# Register your models here.
admin.site.register(Grupo, GrupoAdmin)
