from django import forms

from .models import Cliente

class ClienteForm(forms.ModelForm):

    class Meta:
        model = Cliente
        fields='__all__'
        widgets={
            'negra':forms.CheckboxInput(attrs={ 'class':'form-control','onclick':'Listanegra();',}),
            'tipo':forms.Select(attrs={'class':'form-control','onChange':'OcultarLicencia();',}),
            'n_id':forms.TextInput(attrs={'class':'form-control', 'placeholder':'Nº documento'}),
            'f_exp_id':forms.DateInput(attrs={'type':'date','class':'form-control',}),

            'nombre':forms.TextInput(attrs={'class':'form-control', 'placeholder':'Nombre'}),
            'apellido':forms.TextInput(attrs={'class':'form-control', 'placeholder':'Apellidos'}),
            'direccion':forms.TextInput(attrs={'class':'form-control', 'placeholder':'Dirección'}),
            'poblacion':forms.TextInput(attrs={'class':'form-control', 'placeholder':'Población'}),
            'provincia':forms.TextInput(attrs={'class':'form-control', 'placeholder':'Provincia'}),
            'cp':forms.TextInput(attrs={'class':'form-control', 'placeholder':'C.P.'}),
            'pais':forms.TextInput(attrs={'class':'form-control', 'placeholder':'País'}),

            

            'movil':forms.TextInput(attrs={'class':'form-control', 'placeholder':'Móvil'}),
            'telefono':forms.TextInput(attrs={'class':'form-control', 'placeholder':'Teléfono'}),
            'email':forms.EmailInput(attrs={'class':'form-control', 'placeholder':'Email'}),

            'f_nacimiento':forms.DateInput(attrs={'type':'date','class':'form-control', 'placeholder':'País'}),
            'l_nacimiento':forms.TextInput(attrs={'class':'form-control', 'placeholder':'Lugar nacimiento'}),
            'licencia':forms.TextInput(attrs={'class':'form-control', 'placeholder':'Número licencia'}),
            'l_exp':forms.TextInput(attrs={'class':'form-control', 'placeholder':'Lugar expedición'}),
            'f_exp':forms.DateInput(attrs={'type':'date','class':'form-control', 'placeholder':'dd/mm/aaaa'}),
            'f_caducidad':forms.DateInput(attrs={'type':'date','class':'form-control', 'placeholder':'Fecha Caducidad'}),

            'trabajo':forms.TextInput(attrs={'class':'form-control', 'placeholder':'Profesión'}),
            'obs':forms.TextInput(attrs={'class':'form-control', 'placeholder':'Observaciones'}),
            'banco':forms.TextInput(attrs={'class':'form-control', 'placeholder':'Cuenta Bancaria'}),
            'tarjeta':forms.TextInput(attrs={'class':'form-control', 'placeholder':'XXXX XXXX XXXX XXXX'}),
            'f_tarjeta':forms.TextInput(attrs={'class':'form-control', 'placeholder':'MM/AA'}),




        }
        labels={
            
        }
    def clean_n_id(self):
        n_id = self.cleaned_data.get('n_id')
        n_id = n_id.upper()
        if  Cliente.objects.filter(n_id=n_id).exists():
            raise forms.ValidationError("El cliente ya está registrado")
        return n_id    

class ClienteFormUpdate(forms.ModelForm):

    class Meta:
        model = Cliente
        fields='__all__'
        widgets={
            'negra':forms.CheckboxInput(attrs={ 'class':'form-control','onclick':'Listanegra();',}),

            'tipo':forms.Select(attrs={'class':'form-control', 'onChange':'Ocultar();' ,}),
            'n_id':forms.TextInput(attrs={'class':'form-control', 'placeholder':'Nº documento'}),
            'f_exp_id':forms.DateInput(attrs={'class':'form-control',}),

            'nombre':forms.TextInput(attrs={'class':'form-control', 'placeholder':'Nombre'}),
            'apellido':forms.TextInput(attrs={'class':'form-control', 'placeholder':'Apellidos'}),
            'direccion':forms.TextInput(attrs={'class':'form-control', 'placeholder':'Dirección'}),
            'poblacion':forms.TextInput(attrs={'class':'form-control', 'placeholder':'Población'}),
            'provincia':forms.TextInput(attrs={'class':'form-control', 'placeholder':'Provincia'}),
            'cp':forms.TextInput(attrs={'class':'form-control', 'placeholder':'C.P.'}),
            'pais':forms.TextInput(attrs={'class':'form-control', 'placeholder':'País'}),

            

            'movil':forms.TextInput(attrs={'class':'form-control', 'placeholder':'Móvil'}),
            'telefono':forms.TextInput(attrs={'class':'form-control', 'placeholder':'Teléfono'}),
            'email':forms.EmailInput(attrs={'class':'form-control', 'placeholder':'Email'}),

            'f_nacimiento':forms.DateInput(attrs={'class':'form-control', 'placeholder':'País'}),
            'l_nacimiento':forms.TextInput(attrs={'class':'form-control', 'placeholder':'Lugar nacimiento'}),
            'licencia':forms.TextInput(attrs={'class':'form-control', 'placeholder':'Número licencia'}),
            'l_exp':forms.TextInput(attrs={'class':'form-control', 'placeholder':'Lugar expedición'}),
            'f_exp':forms.DateInput(attrs={'class':'form-control', 'placeholder':'dd/mm/aaaa'}),
            'f_caducidad':forms.DateInput(attrs={'class':'form-control', 'placeholder':'dd/mm/aaaa'}),

            'trabajo':forms.TextInput(attrs={'class':'form-control', 'placeholder':'Profesión'}),
            'obs':forms.TextInput(attrs={'class':'form-control', 'placeholder':'Observaciones'}),
            'banco':forms.TextInput(attrs={'class':'form-control', 'placeholder':'Cuenta Bancaria'}),
            'tarjeta':forms.TextInput(attrs={'class':'form-control', 'placeholder':'XXXX XXXX XXXX XXXX'}),
            'f_tarjeta':forms.TextInput(attrs={'class':'form-control', 'placeholder':'MM/AA'}),




        }
        labels={
            
        }
   
         
        
       




