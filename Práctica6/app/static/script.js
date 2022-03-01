// ------------------------------------------------------------
// FUNCIONES PARA CAMBIAR A MODO NOCTURNO
// ------------------------------------------------------------

const btnSwitch = document.querySelector('#switch');

btnSwitch.addEventListener('click', () => {
    document.body.classList.toggle('dark');
    btnSwitch.classList.toggle('active');

    // Guardamos el modo en localstorage.
    if(document.body.classList.contains('dark')){
        localStorage.setItem('dark-mode', 'true');
    } else {
        localStorage.setItem('dark-mode', 'false');
    }
});

// Obtenemos el modo actual.
if(localStorage.getItem('dark-mode') === 'true'){
    document.body.classList.add('dark');
    btnSwitch.classList.add('active');
} else {
    document.body.classList.remove('dark');
    btnSwitch.classList.remove('active');
}

// ------------------------------------------------------------
// FUNCIONES PARA AUMENTAR Y DISMINUIR EL TAMAÑO DE LA LETRA
// ------------------------------------------------------------

var sizes = ["f0", "f1", "f2", "f3", "f4", "f5"];
var sizeIndex = localStorage.getItem('size');

// Aumentamos el tamaño de la letra
document.getElementById('aumentar').addEventListener('click', function() {
    let previousSize = sizeIndex;
    sizeIndex++;
    sizeIndex = (sizeIndex == sizes.length) ? sizes.length - 1 : sizeIndex;
    changeClass(previousSize, sizeIndex);
});

// Disminuimos el tamaño de la letra
document.getElementById('disminuir').addEventListener('click', function () {
    let previousSize = sizeIndex;
    sizeIndex--;
    sizeIndex = (sizeIndex < 0) ? 0 : sizeIndex;
    changeClass(previousSize, sizeIndex);
});

// Efectuamos el cambio de letra
function changeClass(anterior, siguiente) {
    if(anterior != siguiente) {
      var htmlElement = document.querySelector('html')
      htmlElement.classList.remove(sizes[anterior]);
      htmlElement.classList.add(sizes[siguiente]);
    }

    // Guardamos el el tamaño de letra actual en localstorage.
    localStorage.setItem('size', siguiente);
    localStorage.getItem('isSized', 'true');
}

// Obtenemos el tamaño de letra actual.
var htmlElement = document.querySelector('html')
htmlElement.classList.remove(sizes[2]);
htmlElement.classList.add(sizes[localStorage.getItem('size')]);
  

// ------------------------------------------------------------
// FUNCIÓN PARA MOSTRAR LA TABLA DE EPISODIOS
// ------------------------------------------------------------

function mostrar(respuesta) {

  $.each(respuesta, function(key, value) {

    // Guardamos los valores del episodio actuals
    let episodio = [value['name'], value['id'], value['url'], value['season'], value['number'], value['airdate'], value['airtime'], value['airstamp'], value['runtime'], value['summary'] ];

    // Añadimos a la tabla los datos de cada episodio y un botón para modificar y para eliminar
    $("tbody").append(`<tr>
      <td>${value['name']}</td>
      <td>${value['id']}</td>
      <td><a href='${value['url']}'>${value['url']}</a></td>
      <td>${value['season']}</td>
      <td>${value['number']}</td>
      <td>${value['airdate']}</td>
      <td>${value['airtime']}</td>
      <td>${value['airstamp']}</td>
      <td>${value['runtime']}</td>
      <td>${value['summary']}</td>
      <td>
      <center>
      <a class="btn btn-warning btn-sm" id="modifyEpisodeBtn" onclick="actualizarFormularioModificar('${episodio[0]}','${episodio[1]}','${episodio[2]}','${episodio[3]}','${episodio[4]}','${episodio[5]}','${episodio[6]}','${episodio[7]}','${episodio[8]}')">Modificar</a>
      </center>
      </td>  
      <td> 
      <center>
      <a class="btn btn-danger btn-sm" onclick="Eliminar('${value.id}')">Eliminar</a>
      </center>
      </td>
      </tr>`)
  });
}


// ------------------------------------------------------------
// CRUD PARA LA BASE DE DATOS DE FRIENDS MEDIANTE JQUERY Y AJAX
// ------------------------------------------------------------

// ------------------- AÑADIR EPISODIO ------------------------
$(function(){

  $('#btn_add_episode').click(

    function(){
        // Guardamos todos los datos introducidos en el formulario
        const nameInputText = document.getElementById("add-name");
        const idInputText = document.getElementById("add-id");
        const urlInputText = document.getElementById("add-url");
        const seasonInputText = document.getElementById("add-season");
        const numberInputText = document.getElementById("add-number");
        const airdateInputText = document.getElementById("add-airdate");
        const airtimeInputText = document.getElementById("add-airtime");
        const airstampInputText = document.getElementById("add-airstamp");
        const runtimeInputText = document.getElementById("add-runtime");
        const summaryInputText = document.getElementById("add-summary");
        
        const item_name= nameInputText.value;
        const item_id = (idInputText.value);
        const item_url = urlInputText.value;
        const item_season = (seasonInputText.value);
        const item_number = (numberInputText.value);
        const item_airdate = (airdateInputText.value);
        const item_airtime = (airtimeInputText.value);
        const item_airstamp = (airstampInputText.value);
        const item_runtime = (runtimeInputText.value);
        const item_summary = (summaryInputText.value);
        
        let urlApi = '/api/episodios';

        // Petición AJAX tipo POST para añadir un episodio
        $.ajax({
            url: urlApi,
            type: 'POST',
            dataType: "json",
            data: {
              name: item_name,
              id: item_id,
              url: item_url,
              season: item_season,
              number: item_number,
              airdate: item_airdate,
              airtime: item_airtime,
              airstamp: item_airstamp,
              runtime: item_runtime,
              summary: item_summary,
              image: ""
            },
        });


        // Refrescamos la página con el nuevo episodio añadido
        $("tbody").empty();
        $.getJSON('/api/episodios').done(mostrar);

        document.getElementById("addEpisode").style.display = "none";

      }
  )
});

// ------------------ CONSULTAR EPISODIOS ----------------------
$(function() {
  $.getJSON('/api/episodios').done(mostrar);
  $("#buscar_name").change(function() {
    let value = $(this).val();
    console.log(value);
    $("tbody").empty();
    $.getJSON('/api/episodios', {
        name: value
    }).done(mostrar);
  });
  $("#buscar_id").change(function() {
    let value = $(this).val();
    console.log(value);
    $("tbody").empty();
    $.getJSON('/api/episodios', {
        id: value
    }).done(mostrar);
  });
  $("#buscar_url").change(function() {
    let value = $(this).val();
    console.log(value);
    $("tbody").empty();
    $.getJSON('/api/episodios', {
        URL: value
    }).done(mostrar);
  });
  $("#buscar_season").change(function() {
      let value = $(this).val();
      console.log(value);
      $("tbody").empty();
      $.getJSON('/api/episodios', {
          season: value
      }).done(mostrar);
  });
  $("#buscar_number").change(function() {
      let value = $(this).val();
      console.log(value);
      $("tbody").empty();
      $.getJSON('/api/episodios', {
          number: value
      }).done(mostrar);
  });
  $("#buscar_airdate").change(function() {
      let value = $(this).val();
      console.log(value);
      $("tbody").empty();
      $.getJSON('/api/episodios', {
          airdate: value
      }).done(mostrar);
  });
  $("#buscar_airtime").change(function() {
    let value = $(this).val();
    console.log(value);
    $("tbody").empty();
    $.getJSON('/api/episodios', {
        airdate: value
    }).done(mostrar);
  });
  $("#buscar_airstamp").change(function() {
    let value = $(this).val();
    console.log(value);
    $("tbody").empty();
    $.getJSON('/api/episodios', {
        airstamp: value
    }).done(mostrar);
  });
  $("#buscar_runtime").change(function() {
    let value = $(this).val();
    console.log(value);
    $("tbody").empty();
    $.getJSON('/api/episodios', {
        runtime: value
    }).done(mostrar);
  });
  $("#buscar_summary").change(function() {
      let value = $(this).val();
      console.log(value);
      $("tbody").empty();
      $.getJSON('/api/episodios', {
          summary: value
      }).done(mostrar);
  });
});

// ------------------- MODIFICAR EPISODIO ----------------------

// Función para que al abrir el formulario de modificar aparezcan los datos del episodio escritos
function actualizarFormularioModificar(nombre,id,url,season,number,airdate,airtime,airstamp,runtime) {

  // Escribimos en cada uno de los campos del formulario los datos del episodio
  document.getElementById("modify-name").value = nombre;
  document.getElementById("modify-url").value = url;
  document.getElementById("modify-season").value = season;
  document.getElementById("modify-number").value = number;
  document.getElementById("modify-airdate").value = airdate;
  document.getElementById("modify-airtime").value = airtime;
  document.getElementById("modify-airstamp").value = airstamp;
  document.getElementById("modify-runtime").value = runtime;
  document.getElementById("modify-id").value = id;

  // Abrimos el modal de modificar episodio
  document.getElementById("modifyEpisode").style.display = "block";
 
}

$(function(){         

  // Al clickear en el botón de modificar un episodio
  $('#btn_modify_episode').click(

    function(){

      // Recogemos los datos modificados del episodio
      const idInputText = document.getElementById("modify-id");
      const nameInputText = document.getElementById("modify-name");
      const urlInputText = document.getElementById("modify-url");
      const seasonInputText = document.getElementById("modify-season");
      const numberInputText = document.getElementById("modify-number");
      const airdateInputText = document.getElementById("modify-airdate");
      const airtimeInputText = document.getElementById("modify-airtime");
      const airstampInputText = document.getElementById("modify-airstamp");
      const runtimeInputText = document.getElementById("modify-runtime");
      
      const item_id = idInputText.value;
      const item_name = nameInputText.value;
      const item_url = urlInputText.value;
      const item_season = (seasonInputText.value);
      const item_number = (numberInputText.value);
      const item_airdate = (airdateInputText.value);
      const item_airtime = (airtimeInputText.value);
      const item_airstamp = (airstampInputText.value);
      const item_runtime = (runtimeInputText.value);
      
      let urlApi = '/api/episodios/' + item_id;

      // Petición AJAX de tipo PUT para modificar un episodio
      $.ajax({
          url: urlApi,
          type: 'PUT',
          dataType: "json",
          data: {
            name: item_name,
            url: item_url,
            season: item_season,
            number: item_number,
            airdate: item_airdate,
            airtime: item_airtime,
            airstamp: item_airstamp,
            runtime: item_runtime,
          },
      });

      // Refrescamos la tabla de episodios con el episodio modificado
      $("tbody").empty();
      $.getJSON('/api/episodios').done(mostrar);

      // Cerramos el modal
      document.getElementById("modifyEpisode").style.display = "none";
    }
  )
});


// ------------------- ELIMINAR EPISODIO ----------------------
function Eliminar(id) {

  let urlApi = '/api/episodios/' + id

  $(function() {
      console.log(urlApi)

      // Petición AJAX para eliminar un episodio
      $.ajax({
          url: urlApi,
          type: 'DELETE',
      });

      // Refrescamos la página sin el nuevo episodio eliminado
       $("tbody").empty();
      $.getJSON('/api/episodios').done(mostrar);
  });
}





// ------------------------------------------------------------
// FUNCIONES PARA LOS MODALS
// ------------------------------------------------------------

// ---------------------- SEARCH MODAL ------------------------

// Obtenemos el modal
var modalSearch = document.getElementById("searchEpisode");

// Obtenemos el botón que abre el modal
var btnSearch = document.getElementById("searchEpisodeBtn");

// Obtenemos el span que cierra el modal
var spanSearch = document.getElementsByClassName("close")[0];

// Cuando el usuario pulsa, se abre el modal
btnSearch.onclick = function() {
  modalSearch.style.display = "block";
}

// Cuando el usuario pulsa <span> (x), se cierra el modal
spanSearch.onclick = function() {
  modalSearch.style.display = "none";
}


// ---------------------- ADD MODAL ---------------------------

// Obtenemos el modal
var modalAdd = document.getElementById("addEpisode");

// Obtenemos el botón que abre el modal
var btnAdd = document.getElementById("addEpisodeBtn");

// Obtenemos el span que cierra el modal
var spanAdd = document.getElementsByClassName("close")[1];

// Cuando el usuario pulsa, se abre el modal
btnAdd.onclick = function() {
  modalAdd.style.display = "block";
}

// Cuando el usuario pulsa <span> (x), se cierra el modal
spanAdd.onclick = function() {
  modalAdd.style.display = "none";
}

// ---------------------- MODIFY MODAL ------------------------

// Obtenemos el span que cierra el modal
var spanModify = document.getElementsByClassName("close")[2];

// Cuando el usuario pulsa <span> (x), se cierra el modal
spanModify.onclick = function() {
  document.getElementById("modifyEpisode").style.display = "none";
}


// ----------------------- ALL MODALS -------------------------

// Cuando el usuario pulsa fuera del modal se cierra
window.onclick = function(event) {
  if (event.target == modalAdd) {
    modalAdd.style.display = "none";
  }
  else if (event.target == modalSearch){
    modalSearch.style.display = "none";
  }
  else if (event.target == document.getElementById("modifyEpisode")){
    document.getElementById("modifyEpisode").style.display = "none";
  }
}