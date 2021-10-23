var Kahoot = require('kahoot.js');
var kliens = new Kahoot;
var nevgenerator = require('nodejs-randomnames');
var randomnevek = nevgenerator.getRandomName();
var jatekpin = "jatekpin";
var randomszam = Math.round(Math.random() * 3);

console.log("Belépés ");
kliens.join(jatekpin, randomnevek);
kliens.on("joined", () => {
    console.log("sikeresen beléptem");
});
kliens.on("questionStart", question => {
    console.log("a kérdés elkezdődött, megválaszolás");
    question.answer(randomszam);
    randomszam = Math.floor(Math.random() * 3);
});
kliens.on("quizEnd", () => {
    console.log("a játék véget ért");
});

// A hibátlan működéshez szükséges a selenium keretrendszer illetve a Kahoot.js telepítése (npm install kahoot.js).
// Írd be a játék pint a "jatekpin" mezőbe.