var express = require('express');
const fs = require('fs')
const path = require('path')
var port = 8080

var liste5elem;
var liste;

var app = express();
app.use(express.static(path.join(__dirname,'public')));
app.set('views', __dirname+"/views")
app.set('view engine', 'ejs');

const spawn = require("child_process").spawn;

const init = spawn('python3', [path.join(__dirname,"python/launch.py")]);

init.stdout.on('data', (data) => {
    console.log("initialisation terminée");
});
init.stderr.on('data', (data) => {
    console.error(`${data}`);
});
init.on('close', (code) => {
    console.log(`child proc init terminé avec code ${code}`)
});
const pythonProcess = spawn('python3', [path.join(__dirname,"python/script.py"), "liste5"]);
pythonProcess.stdout.on('data', function (data) {
    liste5elem = JSON.parse(data.toString());
    // console.log(liste5elem[0]);
    // console.log(liste5elem[1]);
              // var liste1 = liste.replace("\"", "'");


    console.log(data.toString());

});

pythonProcess.stderr.on('data', (data) => {
    console.log(`stderr: ${data}`);
});

pythonProcess.on('close', (code) => {
    console.log(`child process exited with code ${code}`);
});

const pythonProcess2 = spawn('python3', [path.join(__dirname,"python/script.py"), "liste"]);

pythonProcess2.stdout.on('data', function (data) {
    liste = data.toString();
    //console.log( typeof liste)
    // console.log(data.toString());
});

pythonProcess2.stderr.on('data', (data) => {
    console.log(`stderr: ${data}`);
});

pythonProcess2.on('close', (code) => {
    console.log(`child process exited with code ${code}`);
});









app.get('/', function (req, res) {

    res.setHeader('Content-Type', 'text/html');
    res.render('accueil.ejs',{liste5elem : liste5elem,liste : liste});

}).get('/listeStructures', function (req, res) {

    res.setHeader('Content-Type', 'text/html');
    res.render('liste.ejs', { liste: liste5elem });

})

.get("/structure", function (req, resp) {
        if (resp.statusCode != 200) {
            resp.send("bruh");
        }
        else {
            resp.render("structure.ejs", {});
        }


})
.get("/rechercher", function (req, resp) {

        if (resp.status == 200) {
            resp.render("rechercheRes.ejs", { nombre: 42 });
        }
        else {
            console.log("erreur: " + resp.message);
        }
});


app.listen(port, () => console.log(`serveur en ecoute sur le port ${port} !`));

