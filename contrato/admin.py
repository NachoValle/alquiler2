from django.contrib import admin

from .models import ConceptoAlquiler, Contrato
# Register your models here.


class ConceptoAdmin(admin.ModelAdmin):
    list_display = ('id', 'concepto')


class ContratoAdmin(admin.ModelAdmin):
    list_display = ('id', 'c_general', 'h_contrato', 'f_contrato', 'c_madrid',
                    'c_salamanca', 'c_valladolid', 'c_las_palmas', 'c_mallorca', 'c_zamora')


admin.site.register(ConceptoAlquiler, ConceptoAdmin)
admin.site.register(Contrato, ContratoAdmin)
