var ganar = 0;
var perder = 0;

var n_errores = 7;

var wordDisplayLettersElement = document.getElementById("word-display-letters");
var lestrasadivinadas = document.getElementById("letras adivinadas");
var contadorerrores = document.getElementById("error count");
var contadorvictoria = document.getElementById("win count");
var contadorderrota = document.getElementById("loss count");

var blinkElements = document.getElementsByClassName("blinking");
var alertLineElements = document.getElementsByClassName("alert-line");

var letrasvalidas = [ 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z' ];


var juego = new Ahorcado();

document.onkeyup = function(event) {
	var usuario = event.key;

	if (!juego.finjuego) {
		if (letrasvalidas.includes(usuario) && !juego.letraadivinada.includes(usuario)) {
			juego.checkGuess(usuario);
		}
	} else {
		juego = new Ahorcado();
		juego.updatePageData();
	}
}

window.setInterval(function() {
	if (blinkElements.length > 0) {
		if (juego.letraadivinada.length === 0 || juego.finjuego) {
			if (blinkElements[0].style.opacity === "1") {
				for (var i = 0; i < blinkElements.length; i++) {
					blinkElements[i].style.opacity = "0";
				}
			} else {
				for (var i = 0; i < blinkElements.length; i++) {
					blinkElements[i].style.opacity = "1";
				}
			}
		} else {
			for (var i = 0; i < blinkElements.length; i++) {
				blinkElements[i].style.opacity = "0";
			}
		}
	}
}, 750);

function Ahorcado() {
    // Lista de palabras para el juego
    this.palabras = [
        "casas", "escuela", "puerta", "carro", "florero", "manzana", "amistad", 
        "lluvia", "cereza", "camisa", "zapato", "grama", "mariposa", "celular", 
        "bandera", "ventana", "soltero", "cocina", "sombrero", "barro", "reloj", 
        "fiesta", "lavabo", "aves", "martillo", "botella", "camino", "cuchara", 
        "lago", "guitarra", "bicicleta", "lampara", "suelo", "espacio", "cuaderno", 
        "playa", "cielo", "libro", "familia"
    ];

// Selecciona una palabra al azar de la lista
	this.palabra = this.palabras[Math.floor(Math.random() * this.palabras.length)];
	this.letradivinada = [];   // Letras adivinadas
    this.errores = 0;            // Conteo de errores
    this.verletra = [];   // Letras visibles en la palabra
    this.finjuego = false;      // Estado del juego
    this.alertaline = emptyAlert;   // Líneas de alerta

	// Inicializa las letras visibles como false
	for (var i = 0; i < this.palabra.length; i++) {
		this.verletra[i] = (false);
	}
}

Ahorcado.prototype.checkGuess = function(char) {
	this.letraadivinada.push(char);

	var esenpalabra = false;
	for (var i = 0; i < this.palabra.length; i++) {
		if (this.palabra.charAt(i) === char) {
			esenpalabra = true;
			this.verletra[i] = true;
		}
	}
	if (!esenpalabra) {
		this.errores++;
	}

	if (this.errores >= n_errores) {
		perder++;
		this.alertLines = youLose;
		this.finjuego = true;
	}

	if (!this.verletra.includes(false)) {
		ganar++;
		this.alertLines = youWin;
		this.finjuego = true;
	}

	juego.updatePageData();
};

Ahorcado.prototype.updatePageData = function() {
	var tempString = "";
	for (var i = 0; i < this.verletra.length; i++) {
		tempString += ((this.verletra[i] || this.finjuego) ? this.palabra.charAt(i).toUpperCase() : "_");
		if (i < (this.verletra.length - 1)) tempString += " ";
	}
	wordDisplayLettersElement.textContent = tempString;

	tempString = "";
	for (var i = 0; i < this.letraadivinada.length; i++) {
		tempString += (this.letraadivinada[i].toUpperCase());
		if (i < (this.letraadivinada.length - 1)) tempString += " ";
	}
	for (var i = tempString.length; i < 51; i++) {
		tempString += " ";
	}
	lestrasadivinadas.textContent = tempString;

	tempString = this.errores + " / " + n_errores;
	for (var i = tempString.length; i < 32; i++) {
		tempString += " ";
	}
	contadorerrores.textContent = tempString;

	tempString = ganar + "";
	for (var i = tempString.length; i < 45; i++) {
		tempString += " ";
	}
	contadorvictoria.textContent = tempString;

	tempString = perder + "";
	for (var i = tempString.length; i < 43; i++) {
		tempString += " ";
	}
	contadorderrota.textContent = tempString;

	for (var i = 0; i < blinkElements.length; i++) {
		blinkElements[i].textContent = (this.finjuego ? pressAnyKeyToReset[i] : pressAnyKeyToStart[i]);
	}

	for (var i = 0; i < alertLineElements.length; i++) {
		alertLineElements[i].textContent = (this.alertLines[i]);
	}
}

juego.updatePageData();
