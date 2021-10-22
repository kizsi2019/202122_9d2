const Kahoot = require("kahoot.js-republished");

const NameGenerator = require('nodejs-randomnames');
const app = require('express')();
const server = require('http').Server(app);
const io = require('socket.io')(server);

var client = []

server.listen(3000);

app.get('/', function (req, res) {
  res.sendFile(__dirname + '/index.html');
});

io.on('connection', function (socket) {
    console.log('connect')
    socket.on('kahoot', function(data){
        var amount = data.amount;
        var gamePin = data.pin;
        console.log(amount);
        for(var i=0; i<amount; i++){
            client[i] = new Kahoot;
        }
        
            for(var i=0; i<amount; i++){
                client[i].join(gamePin ,NameGenerator.getRandomName());
                
              
            }
            console.log("joined")
            
        
        client[0].on("questionStart", function(question){
        
            for(var i=0; i<client.length-1; i++){
        
                client[i].answerQuestion(0)
        
            }
            console.log("Answering");
           
        });
        
        client[0].on("quizEnd", () => {
            console.log("The quiz has ended.");
        });
        


    })
  
 
});












