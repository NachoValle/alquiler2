from django import forms

from .models import Agencia

class AgenciaForms(forms.ModelForm):

    class Meta:
        model = Agencia
        fields=['direccion','codigo_postal','telefono_movil','telefono_fijo','email','condiciones',]
        widgets={
           
            'ciudad':forms.TextInput(attrs={'class':'form-control', 'placeholder':'Nº documento'}),
            'codigo':forms.TextInput(attrs={'class':'form-control', 'placeholder':'CODIGO CIUDAD'}),
            'direccion':forms.TextInput(attrs={'class':'form-control', 'placeholder':'Dirección'}),
            'codigo_postal':forms.NumberInput(attrs={'class':'form-control', 'placeholder':'C.P.'}),
            'telefono_movil':forms.TextInput(attrs={'class':'form-control', 'placeholder':'Móvil'}),
            'telefono_fijo':forms.TextInput(attrs={'class':'form-control', 'placeholder':'Teléfono'}),
            'email':forms.EmailInput(attrs={'class':'form-control', 'placeholder':'Email'}),
            'condiciones':forms.Textarea(attrs={'class':'form-control',}),
                  
            
        }
        labels={
            
        }
   




