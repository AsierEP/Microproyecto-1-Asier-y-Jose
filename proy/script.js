let words = ["escritorio", "programa", "telefono", "bicicleta", "silla", "armario", "ventana", "puerta", "cartelera", "televisor",
"planta", "cuchara", "transporte", "cuchillo", "taza", "plato", "cargador", "pintura", "teclado", "raton",
"monitor", "pantalla", "bolso", "coche", "avion", "barco", "javascript", "autobus", "motocicleta",
"cuaderno", "helado", "pizza", "hamburguesa", "sandwich", "pastel", "chocolate", "heladera", "lavadora",
"secadora", "radio", "medalla", "guitarra", "piano", "violín", "flauta", "batería", "telescopio", "microscopio"]; // Lista de palabras

let word = words[Math.floor(Math.random() * words.length)]; // Elegir una palabra al azar
let guessedLetters = new Array(word.length).fill('_');
let failedAttempts = [];
let wins = 0;
let losses = 0;
let keyboardButtons = [];

// Mostrar la palabra a adivinar con espacios en blanco al inicio
document.getElementById("wordToGuess").innerText = guessedLetters.join(' ');

// Generar los botones del teclado
let keyboard = document.getElementById("keyboard");
let alphabet = 'abcdefghijklmnopqrstuvwxyz';
alphabet.split('').forEach(letter => {
  let button = document.createElement('button');
  button.textContent = letter;
  button.classList.add('keyboard-button');
  button.addEventListener('click', function() {
    if (word.includes(letter)) {
      for(let i=0; i<word.length; i++) {
        if(word[i] === letter) guessedLetters[i] = letter;
      }
      document.getElementById("wordToGuess").innerText = guessedLetters.join(' ');
      if (!guessedLetters.includes('_')) {
        wins++;
        document.getElementById("gameStatus").innerText = "¡Has ganado!";
        document.getElementById("score").innerText = "Victorias: " + wins + ", Derrotas: " + losses;
        keyboardButtons.forEach(b => b.disabled = true);
        document.getElementById("newWordButton").disabled = false;
      }
    } else {
      failedAttempts.push(letter);
      document.getElementById("failedAttempts").innerText = "Intentos fallidos: " + failedAttempts.join(', ');
      if (failedAttempts.length >= 7) {
        losses++;
        document.getElementById("gameStatus").innerText = "Has perdido. La palabra era: " + word;
        document.getElementById("score").innerText = "Victorias: " + wins + ", Derrotas: " + losses;
        keyboardButtons.forEach(b => b.disabled = true);
        document.getElementById("newWordButton").disabled = false;
      }
    }
    this.disabled = true; // Desactivar el botón después de hacer clic en él
  });
  keyboard.appendChild(button);
  keyboardButtons.push(button); // Añadir el botón a la lista de botones del teclado
});

// Añadir un clic al evento al botón de nueva palabra
document.getElementById("newWordButton").addEventListener('click', function() {
  word = words[Math.floor(Math.random() * words.length)];
  guessedLetters = new Array(word.length).fill('_');
  failedAttempts = [];
  document.getElementById("wordToGuess").innerText = guessedLetters.join(' ');
  document.getElementById("failedAttempts").innerText = "";
  document.getElementById("gameStatus").innerText = "";
  keyboardButtons.forEach(b => {
    b.disabled = false; // Reactivar todos los botones del teclado
    b.textContent = b.textContent.toLowerCase(); // Restaurar el texto del botón a minúsculas
  });
  this.disabled = true; // Desactivar el botón de nueva palabra hasta que el juego termine
});