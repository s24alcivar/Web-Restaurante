let menuVisible = false;
//Función que oculta o muestra el menu
function mostrarOcultarMenu(){
    if(menuVisible){
        document.getElementById("nav").classList ="";
        menuVisible = false;
    }else{
        document.getElementById("nav").classList ="responsive";
        menuVisible = true;
    }
}
function seleccionar(){
    //oculto el menu una vez que selecciono una opcion
    document.getElementById("nav").classList = "";
    menuVisible = false;
}

function verMasPlato(plato) {
    // Actualiza el contenido del modal con los detalles del plato
    $("#platoDetalle").html(`
        <h2>${plato.nombre}</h2>
        <p>${plato.descripcion}</p>
        <p>Precio: $${plato.precio}</p>
        <button onclick="comprarPlato(${plato.id})">Comprar</button>
    `);

    // Abre el modal
    $("#myModal").show();
}
function comprarPlato(platoId) {
    // Aquí puedes implementar la lógica para procesar la compra
    alert(`¡Plato ${platoId} comprado!`);
    // Cierra el modal después de la compra
    cerrarModal();
}
