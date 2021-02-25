from django import forms

from .models import ConceptoAlquiler,Contrato

class ConceptoForm(forms.ModelForm):

    class Meta:
        model = ConceptoAlquiler
        fields=['concepto',]
        widgets={
            
            'concepto':forms.TextInput(attrs={'class':'form-control',}),
             }
        labels={
            
        }
   

class ContratoFormUpdate(forms.ModelForm):
    
    
    class Meta:
        
        model = Contrato
        fields=['alquilado','cancelado','observacion','fianza_deposito','fianza_tarjeta','pago_tarjeta','km_fin',]

        widgets={ 
            'alquilado':forms.CheckboxInput(attrs={ 'class':'form-control','onclick':'entregado();',}),
            'cancelado':forms.CheckboxInput(attrs={ 'class':'form-control','onclick':'cancelar();',}),
            'fianza_deposito':forms.CheckboxInput(attrs={ 'class':'form-control','onclick':'fianza();',}),
            'fianza_tarjeta':forms.CheckboxInput(attrs={ 'class':'form-control','onclick':'fianzatarjeta();',}),
            'pago_tarjeta':forms.CheckboxInput(attrs={ 'class':'form-control','onclick':'alquilertarjeta();',}),
            'observacion':forms.TextInput(attrs={'class':'form-control','maxlength':'50',}),
            'km_fin':forms.NumberInput(attrs={ 'class':'form-control','step':'1','min':'0','onkeyup':'kmhechos();',}),
            
        }



class ContratoForm(forms.ModelForm):

    class Meta:
        model = Contrato
        fields='__all__'
       
        widgets={ 
             #----  conceptos --- 
            'f_inicio':forms.DateInput(attrs={ 'type':'date',}),
            'f_fin':forms.DateInput(attrs={ 'type':'date','onmousemove':'diasAlquilado();'}),
            'h_inicio':forms.TimeInput(attrs={ 'type':'time',}),
            'h_fin':forms.TimeInput(attrs={ 'type':'time',}),         
            'oficina':forms.TextInput(attrs={'style':'visibility:hidden','readonly':'',}),
            'empleado':forms.TextInput(attrs={'style':'visibility:hidden','readonly':'',}),

            'fianza':forms.NumberInput(attrs={ 'step':'0.01','min':'0',}),
            'total':forms.NumberInput(attrs={'readonly':'',}),
            'concepto1':forms.Select(attrs={ }),
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
            
            'cantidad_c5':forms.NumberInput(attrs={'onkeyup':'multiplicar("cantidad_c5","precio_c5","total_c5");totalAlquiler();' ,'step':'0.01','min':'0',}),    
            'precio_c5':forms.NumberInput(attrs={'onkeyup':'multiplicar("cantidad_c5","precio_c5","total_c5");totalAlquiler();' ,'step':'0.01','min':'0', }),    
            'total_c5':forms.NumberInput(attrs={'onkeyup':'dividir("cantidad_c5","total_c5","precio_c5");totalAlquiler();' ,'step':'0.01','min':'0', }),    
           
            'cantidad_c6':forms.NumberInput(attrs={'onkeyup':'multiplicar("cantidad_c6","precio_c6","total_c6");totalAlquiler();' ,'step':'0.01','min':'0',}),    
            'precio_c6':forms.NumberInput(attrs={'onkeyup':'multiplicar("cantidad_c6","precio_c6","total_c6");totalAlquiler();' ,'step':'0.01','min':'0', }),    
            'total_c6':forms.NumberInput(attrs={'onkeyup':'dividir("cantidad_c6","total_c6","precio_c6");totalAlquiler();' ,'step':'0.01','min':'0', }),    

            
            
            'observacion':forms.TextInput(attrs={'maxlength':'50',}),
            
             # ---- conductor ------
            'id_conductor':forms.NumberInput(attrs={'style':'visibility:hidden','readonly':'',}),
            
            
            'conductor':forms.TextInput(attrs={'onmousemove':'PasarValorConductor();','placeholder':'Conductor'}),
            'nombre':forms.TextInput(attrs={'readonly':'',}),
            'apellido':forms.TextInput(attrs={'readonly':'',}),
            'direccion':forms.TextInput(attrs={'readonly':'',}),
            'poblacion':forms.TextInput(attrs={ 'readonly':'',}),
            'provincia':forms.TextInput(attrs={ 'readonly':'',}),
            'pais':forms.TextInput(attrs={ 'readonly':'',}),
            'telefono':forms.TextInput(attrs={ 'readonly':'',}),
            'movil':forms.TextInput(attrs={ 'readonly':'',}),
            'f_nacimiento':forms.DateInput(attrs={ 'type':'date','readonly':'',}),
            'licencia':forms.TextInput(attrs={ 'readonly':'',}),
            'l_exp':forms.TextInput(attrs={ 'readonly':'',}),
            'f_exp':forms.DateInput(attrs={ 'type':'date','readonly':'',}),
            'f_caducidad':forms.DateInput(attrs={ 'type':'date','readonly':'',}),
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
            # ---- conductor Adicional ------ 
               
            'id_conductor_ad':forms.NumberInput(attrs={'style':'visibility:hidden','readonly':'',}),
            'conductor_a':forms.TextInput(attrs={'onmousemove':'PasarValorConductorA();','placeholder':'Conductor'}),
            'a_nombre':forms.TextInput(attrs={'readonly':'',}),
            'a_apellido':forms.TextInput(attrs={'readonly':'',}),
            'a_direccion':forms.TextInput(attrs={'readonly':'',}),
            'a_poblacion':forms.TextInput(attrs={ 'readonly':'',}),
            'a_provincia':forms.TextInput(attrs={ 'readonly':'',}),
            'a_pais':forms.TextInput(attrs={ 'readonly':'',}),
            'a_telefono':forms.TextInput(attrs={ 'readonly':'',}),
            'a_movil':forms.TextInput(attrs={ 'readonly':'',}),
            'a_f_nacimiento':forms.DateInput(attrs={ 'type':'date','readonly':'',}),
            'a_licencia':forms.TextInput(attrs={ 'text':'center','readonly':'',}),
            'a_l_exp':forms.TextInput(attrs={ 'readonly':'',}),
            'a_f_exp':forms.DateInput(attrs={ 'type':'date','readonly':'',}),
            'a_f_caducidad':forms.DateInput(attrs={ 'type':'date','readonly':'',}),
            # ---- Vehiculo ------
            'combustible' : forms.Select(attrs={}),
            'grupo' : forms.Select(attrs={}),
            'vehiculo':forms.TextInput(attrs={ 'placeholder':'Matrícula'}),
            'marca':forms.TextInput(attrs={ 'readonly':'',}),
            'modelo':forms.TextInput(attrs={'readonly':'',}),
            't_combustible':forms.TextInput(attrs={'readonly':'',}),
            'color':forms.TextInput(attrs={ 'readonly':'',}),
            'id_vehiculo':forms.NumberInput(attrs={'style':'visibility:hidden','readonly':'',}),
            'km_inicio':forms.NumberInput(attrs={ 'placeholder':'km inicio'}),
            'combustible':forms.Select(attrs={'selected':'f'}),
            'km_extra':forms.TextInput(attrs={}), 
            'km_ilimitado': forms.CheckboxInput(attrs={'class':'form-control'}), 

             }
        labels={
            
        }

         
        
       




