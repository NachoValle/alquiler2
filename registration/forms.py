from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile


class ProfileForm(forms.ModelForm):
    class Meta:
         model = Profile
         fields = ['avatar_user','movil','fianza','f_carga','f_turismo','km_extra_turismo','km_extra_carga','trato']
         widgets = {
                 'avatar_user': forms.ClearableFileInput(attrs={'class':'form-control-file mt-3'}),                 
                 'movil':forms.TextInput(attrs={'class':'form-control','placeholder':'Telefono'}),
                 'trato':forms.TextInput(attrs={'class':'form-control',}),
                 'fianza':forms.NumberInput(attrs={ 'step':'0.01','min':'0','class':'form-control',}),
                 'f_carga':forms.NumberInput(attrs={ 'step':'0.01','min':'0','class':'form-control',}),
                 'f_turismo':forms.NumberInput(attrs={ 'step':'0.01','min':'0','class':'form-control',}),
                 'km_extra_turismo':forms.NumberInput(attrs={ 'step':'0.0001','min':'0','class':'form-control',}),
                 'km_extra_carga':forms.NumberInput(attrs={ 'step':'0.0001','min':'0','class':'form-control',}),
                
                 
        
         }

class EmailForm(forms.ModelForm):
        email= forms.EmailField(required=True, help_text="Requerido, debe ser valido. Para poder recuperar la contraseña")
        class Meta:
                model = User
                fields = ['email']
        
        def clean_email(self):
                email = self.cleaned_data.get('email')
                if 'email' in self.changed_data:
                      
                        return email

class UsuariosForm(forms.ModelForm):
        class Meta:
         model = Profile
         fields = ['oficina','madrid','valladolid','salamanca','las_palmas','mallorca','zamora','todas','p_vehiculos','p_user']
         widgets = {
                  'madrid':forms.CheckboxInput(attrs={'onclick':'Simadrid();',}),
                  'valladolid':forms.CheckboxInput(attrs={'onclick':'Sivalladolid();',}),
                  'salamanca':forms.CheckboxInput(attrs={'onclick':'Sisalamanca();',}),
                  'las_palmas':forms.CheckboxInput(attrs={'onclick':'Silaspalmas();',}),
                  'mallorca':forms.CheckboxInput(attrs={'onclick':'Simallorca();',}),
                  'zamora':forms.CheckboxInput(attrs={'onclick':'Sizamora();',}),
                  'todas':forms.CheckboxInput(attrs={'onclick':'Sitodas();',}),
                  'p_user':forms.CheckboxInput(attrs={'onclick':'Siuser();',}),
                  'p_vehiculos':forms.CheckboxInput(attrs={'onclick':'Sivehiculo();',}),
          }
        
                
                