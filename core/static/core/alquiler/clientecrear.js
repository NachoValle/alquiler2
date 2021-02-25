function Listanegra(){
    var a = document.getElementById('id_negra').checked;
    if (a == true){
      document.getElementById('labelnegra').innerHTML = "Cliente en lista Negra";
      document.getElementById('labelnegra').style.color = "red";
     
  
      }else{
        document.getElementById('labelnegra').innerHTML = "Añadir a la Lista Negra";
        document.getElementById('labelnegra').style.color = "black";
      };
  
  
  };

function OcultarLicencia(){
  var tipodoc = document.getElementById('id_tipo').value;
  
  if (tipodoc == "C.I.F."){
    
    document.getElementById('licen').style.display = 'none';
    document.getElementById('a').style.display = 'none';
    document.getElementById('c').style.display = 'none';
    document.getElementById("nom").className = "col-sm-6";
    
  }else{
    
    document.getElementById('licen').style.display = 'block';
    document.getElementById('a').style.display = 'block';
    document.getElementById('c').style.display = 'block';
    document.getElementById("nom").className = "col-sm-3";
    
  }
  
  };

  function pasarDni(){
    var a = document.getElementById('id_n_id').value;
    document.getElementById('id_licencia').value = a;
    var b = document.getElementById('id_pais').value;
    document.getElementById('id_l_exp').value = b;

  };