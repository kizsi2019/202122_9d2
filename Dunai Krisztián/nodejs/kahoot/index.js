var Kahoot = require('kahoot.js');
var client = new Kahoot;
var NameGenerator = require('nodejs-randomnames');
var randomName = NameGenerator.getRandomName();
var game_pin = 4446423;
var randomnumber = Math.round(Math.random() * 3);

console.log("Belépés ");
client.join(game_pin, randomName);
client.on("joined", () => {
    console.log("sikeresen beléptem");
});
client.on("questionStart", question => {
    console.log("a kérdés elkezdődött, megválaszolás");
    question.answer(randomnumber);
    randomnumber = Math.floor(Math.random() * 3);
});
client.on("quizEnd", () => {
    console.log("a játék véget ért");
});