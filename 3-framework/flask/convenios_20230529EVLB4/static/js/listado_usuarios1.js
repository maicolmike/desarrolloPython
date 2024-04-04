$("#btn1").click(function(){
    alert("prueba");
});

(function () {

    const btnsEditar = document.querySelectorAll('.btnEditar');
    
    let idSeleccionado = null;
    let userSeleccionado = null;
    let tippoSeleccionado = null;

    const csrf_token = document.querySelector("[name='csrf-token']").value;
    
    btnsEditar.forEach((btn) => {
        btn.addEventListener('click', function () {
            idSeleccionado = this.id; // tome el id del btn
            userSeleccionado = this.value; // tome el value del btn
            tippoSeleccionado = this.name; // tome el name del btn
            console.log(idSeleccionado); // imprimir en consola
            console.log(userSeleccionado); // imprimir en consola
            console.log(tippoSeleccionado); // imprimir en consola
            confirmarComprar();
        });
    });

    const confirmarComprar = () => {
            Swal.fire({
            title: 'Actualizar contraseña',
            //input: 'text',
            html:   '<div class="form-inline col-sm-12 mt-3">' +
                    '<label class="control-label col-sm-4" for="UserName">Usuario</label>' +
                    '<input required="" class="form-control col-sm-7" id="UserName" name="usuario" type="text" autofocus style="color: #2e7d32;">'+
                    '</div>' +
                    '<div class="form-inline col-sm-12 mt-3">' +
                    '<label class="control-label col-sm-4" for="UserPass">Contraseña</label>' +
                    '<input required="" class="form-control col-sm-7" id="UserPass" name="clave" type="password" style="color: #2e7d32;">' +
                    '</div>',
            inputAttributes: {
                autocapitalize: 'off'
            },
            showCancelButton: true,
            confirmButtonText: 'Guardar',
            showLoaderOnConfirm: true,
            preConfirm: async () => {
                // console.log(window.origin);
                return await fetch(`${window.origin}/listarUsuarios`, {
                    method: 'POST',
                    mode: 'same-origin',
                    credentials: 'same-origin',
                    headers: {
                        'Content-Type': 'application/json',
                        'X-CSRF-TOKEN': csrf_token
                    },
                    
    onOpen: (modal) => {
      confirmOnEnter = (event) => {
        if (event.keyCode === 13) {
          event.preventDefault();
          modal.querySelector(".swal2-confirm").click();
        }
      };
      modal.querySelector("#UserName").addEventListener("keyup", confirmOnEnter);
      modal.querySelector("#UserPass").addEventListener("keyup", confirmOnEnter);
    },
                    body: JSON.stringify({
                        'id json': idSeleccionado,
                        'user json': userSeleccionado
                    })
                }).then(response => {
                    if (!response.ok) {
                        notificacionSwal('Error', response.statusText, 'error', 'Cerrar');
                    }
                    return response.json();
                }).then(data => {
                    if (data.exito) {
                        notificacionSwal('¡Éxito!', 'Actualizacion realizada', 'success', '¡Ok!');
                    } else {
                        notificacionSwal('¡Alerta!', data.mensaje, 'warning', 'Ok');
                    }
                }).catch(error => {
                    notificacionSwal('Error', error, 'error', 'Cerrar');
                });
            },
            allowOutsideClick: () => false,
            allowEscapeKey: () => false
        });
    };

})();