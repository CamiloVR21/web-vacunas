const formulario = document.getElementById('formulario');
const inputs = document.querySelectorAll('#formulario input');

const expresiones = {
	usuario: /^[a-zA-Z0-9\_\-]{4,16}$/, // Letras, numeros, guion y guion_bajo
	nombre_l: /^[a-zA-ZÀ-ÿ\s]{1,40}$/, // Letras y espacios, pueden llevar acentos.
	Contraseña_l: /^.{4,12}$/, // 4 a 12 digitos.
	correo: /^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$/,
	telefono: /^\d{7,14}$/ // 7 a 14 numeros.
}

const campos = {
	usuario: false,
	nombre_l: false,
	Contraseña_l: false,
	correo: false,
	telefono: false
}

const validarFormulario = (e) => {
	switch (e.target.name) {
		case "usuario":
			validarCampo(expresiones.usuario, e.target, 'usuario');
		break;
		case "nombre_l":
			validarCampo(expresiones.nombre_l, e.target, 'nombre_l');
		break;
		case "Contraseña_l":
			validarCampo(expresiones.Contraseña_l, e.target, 'Contraseña_l');
			validarContraseña2_l();
		break;
		case "Contraseña2_l":
			validarContraseña2_l();
		break;
		case "correo":
			validarCampo(expresiones.correo, e.target, 'correo');
		break;
		case "telefono":
			validarCampo(expresiones.telefono, e.target, 'telefono');
		break;
	}
}

const validarCampo = (expresion, input, campo) => {
	if(expresion.test(input.value)){
		document.getElementById(`grupo__${campo}`).classList.remove('formulario__grupo-incorrecto');
		document.getElementById(`grupo__${campo}`).classList.add('formulario__grupo-correcto');
		document.querySelector(`#grupo__${campo} i`).classList.add('fa-check-circle');
		document.querySelector(`#grupo__${campo} i`).classList.remove('fa-times-circle');
		document.querySelector(`#grupo__${campo} .formulario__input-error`).classList.remove('formulario__input-error-activo');
		campos[campo] = true;
	} else {
		document.getElementById(`grupo__${campo}`).classList.add('formulario__grupo-incorrecto');
		document.getElementById(`grupo__${campo}`).classList.remove('formulario__grupo-correcto');
		document.querySelector(`#grupo__${campo} i`).classList.add('fa-times-circle');
		document.querySelector(`#grupo__${campo} i`).classList.remove('fa-check-circle');
		document.querySelector(`#grupo__${campo} .formulario__input-error`).classList.add('formulario__input-error-activo');
		campos[campo] = false;
	}
}

const validarContraseña_2 = () => {
	const inputContraseña_l = document.getElementById('Contraseña_l');
	const inputContraseña_2 = document.getElementById('Contraseña_2');

	if(inputContraseña_l.value !== inputContraseña_2.value){
		document.getElementById(`grupo__Contraseña2_l`).classList.add('formulario__grupo-incorrecto');
		document.getElementById(`grupo__Contraseña2_l`).classList.remove('formulario__grupo-correcto');
		document.querySelector(`#grupo__Contraseña2_l i`).classList.add('fa-times-circle');
		document.querySelector(`#grupo__Contraseña2_l i`).classList.remove('fa-check-circle');
		document.querySelector(`#grupo__Contraseña2_l .formulario__input-error`).classList.add('formulario__input-error-activo');
		campos['Contraseña_l'] = false;
	} else {
		document.getElementById(`grupo__Contraseña2_l`).classList.remove('formulario__grupo-incorrecto');
		document.getElementById(`grupo__Contraseña2_l`).classList.add('formulario__grupo-correcto');
		document.querySelector(`#grupo__Contraseña2_l i`).classList.remove('fa-times-circle');
		document.querySelector(`#grupo__Contraseña2_l i`).classList.add('fa-check-circle');
		document.querySelector(`#grupo__Contraseña2_l .formulario__input-error`).classList.remove('formulario__input-error-activo');
		campos['Contraseña_l'] = true;
	}
}

inputs.forEach((input) => {
	input.addEventListener('keyup', validarFormulario);
	input.addEventListener('blur', validarFormulario);
});

formulario.addEventListener('submit', (e) => {
	e.preventDefault();

	const terminos = document.getElementById('terminos');
	if(campos.usuario && campos.nombre_l && campos.Contraseña_l && campos.correo && campos.telefono && terminos.checked ){
		formulario.reset();

		document.getElementById('formulario__mensaje-exito').classList.add('formulario__mensaje-exito-activo');
		setTimeout(() => {
			document.getElementById('formulario__mensaje-exito').classList.remove('formulario__mensaje-exito-activo');
		}, 5000);

		document.querySelectorAll('.formulario__grupo-correcto').forEach((icono) => {
			icono.classList.remove('formulario__grupo-correcto');
		});
	} else {
		document.getElementById('formulario__mensaje').classList.add('formulario__mensaje-activo');
	}
});