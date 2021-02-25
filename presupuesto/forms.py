from django import forms

from .models import Presupuesto

 

class PresupuestoForm(forms.ModelForm):

    class Meta:
        model = Presupuesto
        fields='__all__'
       
        widgets={ 
             #----  conceptos --- 
            'f_inicio':forms.DateInput(attrs={ 'type':'date',}),
            'f_fin':forms.DateInput(attrs={ 'type':'date','onmousemove':'diasAlquilado();'}),
            'h_inicio':forms.TimeInput(attrs={ 'type':'time',}),
            'h_fin':forms.TimeInput(attrs={ 'type':'time',}),         
            'oficina':forms.TextInput(attrs={'style':'','readonly':'','style':'visibility:hidden',}),
            'empleado':forms.TextInput(attrs={'style':'','readonly':'','style':'visibility:hidden',}),

            'fianza':forms.NumberInput(attrs={ 'step':'0.01','min':'0',}),
            'total':forms.NumberInput(attrs={'readonly':'',}),
            'pConcepto1':forms.Select(attrs={ }),
            'pConcepto2':forms.Select(attrs={ }),
            'pConcepto3':forms.Select(attrs={ }),
            'pConcepto4':forms.Select(attrs={ }),
            'fianza_tarjeta': forms.CheckboxInput(attrs={ }),
           
            'cantidad_c1':forms.NumberInput(attrs={'onkeyup':'multiplicar("cantidad_c1","precio_c1","total_c1");totalAlquiler();' ,'step':'0.01','min':'0',}),    
            'precio_c1':forms.NumberInput(attrs={'onkeyup':'multiplicar("cantidad_c1","precio_c1","total_c1");totalAlquiler();' ,'step':'0.01','min':'0',}),    
            'total_c1':forms.NumberInput(attrs={'onkeyup':'dividir("cantidad_c1","total_c1","precio_c1");totalAlquiler();' ,'step':'0.01','min':'0',}),    
           
            'cantidad_c2':forms.NumberInput(attrs={'onkeyup':'multiplicar("cantidad_c2","precio_c2","total_c2");totalAlquiler();' ,'step':'0.01','min':'0',}),    
            'precio_c2':forms.NumberInput(attrs={'onkeyup':'multiplicar("cantidad_c2","precio_c2","total_c2");totalAlquiler();' ,'step':'0.01','min':'0', }),    
            'total_c2':forms.NumberInput(attrs={'onkeyup':'dividir("cantidad_c2","total_c2","precio_c2");totalAlquiler();' ,'step':'0.01','min':'0',}),    
            
            'cantidad_c3':forms.NumberInput(attrs={'onkeyup':'multiplicar("cantidad_c3","precio_c3","total_c3");totalAlquiler();' ,'step':'0.01','min':'0',}),    
            'precio_c3':forms.NumberInput(attrs={'onkeyup':'multiplicar("cantidad_c3","precio_c3","total_c3");totalAlquiler();' ,'step':'0.01','min':'0', }),    
            'total_c3':forms.NumberInput(attrs={'onkeyup':'dividir("cantidad_c3","total_c3","precio_c3");totalAlquiler();' ,'step':'0.01','min':'0', }),    
           
            'cantidad_c4':forms.NumberInput(attrs={'onkeyup':'multiplicar("cantidad_c4","precio_c4","total_c4");totalAlquiler();' ,'step':'0.01','min':'0',}),    
            'precio_c4':forms.NumberInput(attrs={'onkeyup':'multiplicar("cantidad_c4","precio_c4","total_c4");totalAlquiler();' ,'step':'0.01','min':'0', }),    
            'total_c4':forms.NumberInput(attrs={'onkeyup':'dividir("cantidad_c4","total_c4","precio_c4");totalAlquiler();' ,'step':'0.01','min':'0', }),    
            
            'entregado':forms.NumberInput(attrs={'step':'0.01','min':'0', }),    
            'reservado': forms.CheckboxInput(attrs={ }),
            
            
            
            'observacion':forms.TextInput(attrs={'maxlength':'50',}),
            
            
            # ---- cliente ------
            
            'id_cliente':forms.NumberInput(attrs={'style':'visibility:hidden','readonly':'',}),
            'cliente':forms.TextInput(attrs={'onmousemove':'PasarValorCliente();','placeholder':'Cliente'}),
            'c_apellido':forms.TextInput(attrs={'readonly':'',}),
            'c_direccion':forms.TextInput(attrs={'readonly':'',}),
            'c_poblacion':forms.TextInput(attrs={ 'readonly':'',}),
            'c_provincia':forms.TextInput(attrs={ 'readonly':'',}),
            'c_pais':forms.TextInput(attrs={ 'readonly':'',}),
            'c_telefono':forms.TextInput(attrs={ 'readonly':'',}),
            'c_movil':forms.TextInput(attrs={ 'readonly':'',}),
            'c_cp':forms.TextInput(attrs={ 'readonly':'',}),
           
            # ---- Vehiculo ------
            
            'vehiculo':forms.TextInput(attrs={ 'placeholder':'Matrícula'}),
            'marca':forms.TextInput(attrs={ 'readonly':'',}),
            'modelo':forms.TextInput(attrs={'readonly':'',}),
            't_combustible':forms.TextInput(attrs={'readonly':'',}),
            'color':forms.TextInput(attrs={ 'readonly':'',}),
            'id_vehiculo':forms.NumberInput(attrs={'style':'visibility:hidden','readonly':'',}),
            
            'km_extra':forms.TextInput(attrs={}), 
            'km_ilimitado': forms.CheckboxInput(attrs={'class':'form-control'}), 
             }
        labels={
            
        }

         
        
       




