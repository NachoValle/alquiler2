



/*  ---- AUTOCOMPLETADO ----  */


function autocomplete(inp, arr) {
  /* la función de autocompletar toma dos argumentos,
  el elemento de campo de texto y una matriz de posibles values autocompletados: */
    var currentFocus;
    /*ejecutar una función cuando alguien escribe en el campo de texto:*/
    inp.addEventListener("input", function(e) {
        var a, b, i, val = this.value;
        /*cerrar cualquier lista ya abierta de values autocompletados*/
        closeAllLists();
        if (!val) { return false;}
        currentFocus = -1;
        /*cree un elemento DIV que contendrá los elementos (values):*/
        a = document.createElement("DIV");
        a.setAttribute("id", this.id + "autocomplete-list");
        a.setAttribute("class", "autocomplete-items");
        /*Añada el elemento DIV como hijo del contenedor de autocompletado.:*/
        this.parentNode.appendChild(a);
        /*para cada elemento de la matriz ...*/
        for (i = 0; i < arr.length; i++) {
          /*

compruebe si el elemento comienza con las mismas letras que el valor del campo de texto*/
          if (arr[i].substr(0, val.length).toUpperCase() == val.toUpperCase()) {
            /*cree un elemento DIV para cada elemento coincidente:*/
            b = document.createElement("DIV");
            /*poner las letras a juego en negrita:*/
            b.innerHTML = "<strong>" + arr[i].substr(0, val.length) + "</strong>";
            b.innerHTML += arr[i].substr(val.length);
            /*inserte un campo de entrada que contendrá el valor del elemento de matriz actual:*/
            b.innerHTML += "<input type='hidden' value='" + arr[i] + "'>";
            ;
            /*ejecutar una función cuando alguien hace clic en el valor del elemento (elemento DIV):*/
                b.addEventListener("click", function(e) {
                /*inserte el valor para el campo de texto de autocompletar:*/
                inp.value = this.getElementsByTagName("input")[0].value;
               
                /*cierra la lista de valores autocompletados,
                (o cualquier otra lista abierta de valores autocompletados:*/
                closeAllLists();
            });
            a.appendChild(b);
           
           
          }
        }
    });
    /*ejecutar una función presiona una tecla en el teclado:*/
    inp.addEventListener("keydown", function(e) {
        var x = document.getElementById(this.id + "autocomplete-list");
        if (x) x = x.getElementsByTagName("div");
        if (e.keyCode == 40) {
          /*Si se presiona la tecla de flecha ABAJO,
           aumentar la variable currentFocus*/
          currentFocus++;
          /*y hacer que el elemento actual sea más visible:*/
          addActive(x);
        } else if (e.keyCode == 38) { //up
          /*Si se presiona la tecla de flecha ARRIBA,
           disminuir la variable currentFocus:*/
          currentFocus--;
          /*y hacer que el elemento actual sea más visible:*/
          addActive(x);
        } else if (e.keyCode == 13) {
          /*Si se presiona la tecla ENTER, evite que se envíe el formulario,*/
          e.preventDefault();
          if (currentFocus > -1) {
            /*y simule un clic en el elemento "activo":*/
            if (x) x[currentFocus].click();
          }
        }
    });
    function addActive(x) {
      /*una función para clasificar un elemento como "activo":*/
      if (!x) return false;
      /*comience eliminando la clase "activa" en todos los elementos:*/
      removeActive(x);
      if (currentFocus >= x.length) currentFocus = 0;
      if (currentFocus < 0) currentFocus = (x.length - 1);
      /*Agregar la clase "autocompletar-activa":*/
      x[currentFocus].classList.add("autocomplete-active");
    }
    function removeActive(x) {
      /*una función para eliminar la clase "activa" de todos los elementos de autocompletar:*/
      for (var i = 0; i < x.length; i++) {
        x[i].classList.remove("autocomplete-active");
      }
    }
    function closeAllLists(elmnt) {
      /*cerrar todas las listas de autocompletar en el documento,
       excepto el que pasó como argumento:*/
      var x = document.getElementsByClassName("autocomplete-items");
      for (var i = 0; i < x.length; i++) {
        if (elmnt != x[i] && elmnt != inp) {
        x[i].parentNode.removeChild(x[i]);
      }
    }
  }
  /*ejecutar una función cuando alguien hace clic en el documento:*/
  document.addEventListener("click", function (e) {
      closeAllLists(e.target);
  });
  } 

var matriculas = [];
var i = 0;
for (i; i<json.length; i++){
    matriculas.push(json[i].placa);
}
console.log(matriculas)






// Campos vehiculos
function PasarValorVehiculo()
{
  document.getElementById("id_vehiculo").value =document.getElementById("id_vehiculo").value.toUpperCase();
var captura = document.getElementById("id_vehiculo").value;
var i=0;
var marca="Esperando matricula...";
var modelo= marca;
var combustible = marca;
var color =marca;
var id_vehiculo = marca;
var tipo;
var franq;
var km_extra;

for (i; i<json.length; i++){
 
  if(captura == json[i].placa){
    
    
     marca =json[i].marca;
     modelo =json[i].modelo;
     combustible =json[i].combustible;
     color =json[i].color;
     id_vehiculo = json[i].id;
     tipo= json[i].tipo;
     

   
    if(combustible=='DSL'){
        combustible='DIESEL';
    }else if(combustible=='GAS'){
        combustible='GASOLINA';}else if(combustible=='HIB'){
          combustible='HIBRIDO';};
         
          if (tipo == 'TU'){
            franq =  document.getElementById('r_turismo').innerHTML;
            franq = Number.parseFloat(franq).toFixed(2);
            km_extra =  document.getElementById('r_km_turismo').innerHTML;
            
           
          
          }else if(tipo == 'FU'){
          
            franq =  document.getElementById('r_carga').innerHTML;
            franq = Number.parseFloat(franq).toFixed(2);
            km_extra =  document.getElementById('r_km_carga').innerHTML;
            
       
          
          };
          
    
   
      
   } ;
};
document.getElementsByName("marca")[0].value = marca;
document.getElementsByName("modelo")[0].value = modelo;
document.getElementsByName("t_combustible")[0].value = combustible;
document.getElementsByName("color")[0].value = color;
document.getElementsByName("id_vehiculo")[0].value = id_vehiculo;
document.getElementById('id_franquicia').value = franq;
document.getElementById('id_km_extra').value = km_extra;
 

};


var conductores = [];
var i = 0;
for (i; i<jsonCliente.length; i++){
    if (jsonCliente[i].tipo != "C.I.F."){ conductores.push(jsonCliente[i].n_id);
};};
console.log(conductores);
var clientes = [];
var i = 0;
for (i; i<jsonCliente.length; i++){
  clientes.push(jsonCliente[i].n_id);
};




function PasarValorCliente()
{
  document.getElementById("id_cliente").value =document.getElementById("id_cliente").value.toUpperCase();
var capturaCliente = document.getElementById("id_cliente").value;
var i=0;
var c_nombre="Esperando Cliente...";
var c_apellido= c_nombre;
var c_direccion= c_nombre;
var c_provincia = c_nombre;
var c_poblacion= c_nombre;
var c_pais= c_nombre;
var c_movil= c_nombre;
var c_telefono= c_nombre;

var c_negra;
var c_cp= c_nombre;
var c_id;




for (i; i<jsonCliente.length; i++){
 
  if(capturaCliente == jsonCliente[i].n_id){
    console.log('el Cliente existe');
    
     c_nombre =jsonCliente[i].nombre;
     c_apellido =jsonCliente[i].apellido;   
     c_direccion =jsonCliente[i].direccion;   
     c_poblacion =jsonCliente[i].poblacion;   
     c_provincia =jsonCliente[i].provincia;   
     c_pais =jsonCliente[i].pais;   
     c_movil =jsonCliente[i].movil;   
     c_telefono =jsonCliente[i].telefono;   
     c_cp = jsonCliente[i].cp;
     c_negra = jsonCliente[i].negra;
     c_id = jsonCliente[i].id;
     
    
   } ;
};
document.getElementsByName("c_nombre")[0].value = c_nombre;
document.getElementsByName("c_apellido")[0].value = c_apellido;
document.getElementsByName("c_direccion")[0].value = c_direccion;
document.getElementsByName("c_poblacion")[0].value = c_poblacion;
document.getElementsByName("c_provincia")[0].value = c_provincia;
document.getElementsByName("c_pais")[0].value = c_pais;
document.getElementsByName("c_movil")[0].value = c_movil;
document.getElementsByName("c_telefono")[0].value = c_telefono;
document.getElementsByName("c_cp")[0].value = c_cp;
document.getElementsByName("id_cliente")[0].value = c_id;

if (c_negra == true){
  document.getElementById("iconocliente").className = "fas fa-skull-crossbones";
  document.getElementById("titulocliente").className = "titulo";
}else if (c_negra == false){
  document.getElementById("iconocliente").className = "far fa-thumbs-up";
  document.getElementById("titulocliente").className = "";
};
console.log(c_id)

};



 

/*------ conceptos--------*/

function multiplicar(ncantidad,nprecio,ntotal){
  
  var cantidad = document.getElementsByName(ncantidad)[0].value;
  var precio = document.getElementsByName(nprecio)[0].value; 
  var total = cantidad * precio;
  total = Number.parseFloat(total).toFixed(2);

    document.getElementsByName(ntotal)[0].value = total;


};

function dividir(ncantidad,ntotal,nprecio){
  
  var cantidad = document.getElementsByName(ncantidad)[0].value;
  var total = document.getElementsByName(ntotal)[0].value;
  
  
 
  var precio = total / cantidad;
  precio = Number.parseFloat(precio).toFixed(2);
    document.getElementsByName(nprecio)[0].value = precio;


};

function totalAlquiler(){
  var a =  document.getElementsByName("total_c1")[0].value;
  var b =  document.getElementsByName("total_c2")[0].value;
  var c =  document.getElementsByName("total_c3")[0].value;
  var d =  document.getElementsByName("total_c4")[0].value;
 

  var totalar = Number(a)+Number(b)+Number(c)+Number(d);
  totalar = Number.parseFloat(totalar).toFixed(2);
  document.getElementsByName("total")[0].value =  totalar;
  console.log(totalar)
}

function diasAlquilado(){
  var a = document.getElementsByName("f_inicio")[0].value;
  var b = document.getElementsByName("f_fin")[0].value;
  a = new Date(a);
  b = new Date(b)
  var resta = b.getTime()-a.getTime();
  resta = Math.round(resta/ (1000*60*60*24));
  if(resta == 1){
  document.getElementById("dias").innerHTML = 'alquiler: ' + resta + ' dia';
  document.getElementsByName("cantidad_c1")[0].value = resta;
}
  else if(resta > 1){
    document.getElementById("dias").innerHTML = 'alquiler: ' + resta + ' dias';
    document.getElementsByName("cantidad_c1")[0].value = resta;

  
  }else{
    document.getElementById("dias").innerHTML = 'La fecha de devolucón no es valida';
    document.getElementsByName("cantidad_c1")[0].value = 0;

  }
}