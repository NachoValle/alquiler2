from django import forms

from .models import Grupo

class GrupoForm(forms.ModelForm):

    class Meta:
        model = Grupo
        fields=['grupo','ciudad','descripcion',]
        widgets={
            
            'descripcion':forms.TextInput(attrs={'class':'form-control',}),
            'ciudad':forms.TextInput(attrs={'class':'form-control','readonly':'',}),
            'grupo':forms.Select(attrs={'class':'form-control',}),




             }
        labels={
            
        }
    def clean(self):
        cleaned_data = super(GrupoForm, self).clean()
        grupo = self.cleaned_data.get("grupo")
        ciudad = self.cleaned_data.get("ciudad")
        city = Grupo.objects.filter( ciudad = ciudad)
        for i in city:
            print(i)
           
            if i.grupo == grupo:
                raise forms.ValidationError("El Grupo que instentas Crear ya Existe, prueba con Otro.")
             

    

    




