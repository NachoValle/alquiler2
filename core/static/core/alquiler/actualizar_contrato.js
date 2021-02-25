function entregado(){
    var a = document.getElementById('id_alquilado').checked;
    if (a == true){
      document.getElementById('entregado').innerHTML = "Vehiculo Alquilado";
      document.getElementById('entregado').style.color = "blue";
      document.getElementById('id_cancelado').checked = false;
      document.getElementById('cancelado').innerHTML = "Contrato Activo";
      document.getElementById('cancelado').style.color = "green";
  
      }else{
        document.getElementById('entregado').innerHTML = "Vehiculo Entregado";
        document.getElementById('entregado').style.color = "green";
      };
  
  
  };

function cancelar(){
    var a = document.getElementById('id_cancelado').checked;
    if (a == true){
      document.getElementById('cancelado').innerHTML = "Contrato Cancelado";
      document.getElementById('cancelado').style.color = "red";
      document.getElementById('id_alquilado').checked = false;
      document.getElementById('entregado').innerHTML = "Vehiculo Entregado";
      document.getElementById('entregado').style.color = "green";
  
  
      }else{
        document.getElementById('cancelado').innerHTML = "Contrato Activo";
        document.getElementById('cancelado').style.color = "green";
      };
  
    };


function fianza(){
    var a = document.getElementById('id_fianza_deposito').checked;
    if (a == true){
      document.getElementById('fianzabol').innerHTML = "Fianza en Depósito";
      document.getElementById('fianzabol').style.color = "blue";
      }else{
        document.getElementById('fianzabol').innerHTML = "Fianza Devuelta";
        document.getElementById('fianzabol').style.color = "green";
      };
  
  
  };
  function fianzatarjeta(){
    var a = document.getElementById('id_fianza_tarjeta').checked;
    if (a == true){
      document.getElementById('fianzatarjeta').innerHTML = " <i style='color:orange' class='fas fa-credit-card'></i> Fianza en TARJETA:";
  
      }else{
        document.getElementById('fianzatarjeta').innerHTML = "<i style='color:green' class='fas fa-money-bill-wave'></i> Fianza en EFECTIVO: ";
        
      };
  
  
  };
  function alquilertarjeta(){
    var a = document.getElementById('id_pago_tarjeta').checked;
    if (a == true){
      document.getElementById('alquilertarjeta').innerHTML = "<i style='color:orange' class='fas fa-credit-card'></i> Alquiler en TARJETA: ";
      
      }else{
        document.getElementById('alquilertarjeta').innerHTML = " <i style='color:green' class='fas fa-money-bill-wave'></i> Alquiler en EFECTIVO:";
        
      };
  
  
  };
  function kmhechos(){
    /* kilometros a la salida */
  var salida = document.getElementById('kmsalida').innerHTML;
  /* kilometros libres */
  var libre = document.getElementById('kmlibres').innerHTML;
  libre = Number(libre);
  /* kilometros a la entrega */
  var fin = document.getElementById('id_km_fin').value;
  /* kilometros hechos */
  var hechos = Number(fin)-Number(salida);
  
  /*---------- si hay limite de kilometros -------- */
  if (libre != 'ILIMITADOS'){
  
    if (hechos >= 0){
      document.getElementById('kmhechos').innerHTML = hechos;
      } 
    else{
      document.getElementById('kmhechos').innerHTML = "NO"
    };
  
  
   
    if (hechos>libre){
    
      var extra = hechos - libre;
      document.getElementById('kmextra').innerHTML = extra;
      }
    else{  
      
      document.getElementById('kmextra').innerHTML = "NO";  
    };
  
  }
  /*---------- SI ES ILIMITADO -------- */
  else{
      
      document.getElementById('kmextra').innerHTML = "NO";
     
      if (hechos >= 0){
      document.getElementById('kmhechos').innerHTML = hechos;
      } 
    else{
      document.getElementById('kmhechos').innerHTML = "NO"
    };
  
  
  };
  
  };

  function pasarDni(){
    var dni = document.getElementById('id_n_id').value;
    console.log(dni);
  }