var express = require('express');


var app = express();

/*
app.get('/', function(req, res) {

    res.setHeader('Content-Type', 'text/plain');

    res.send('Vous êtes à l\'accueil, que puis-je pour vous ?');

})


.get('/sous-sol', function(req, res) {

    res.setHeader('Content-Type', 'text/plain');

    res.send('Vous êtes dans la cave à vins, ces bouteilles sont à moi !');

})


.get('/etage/1/chambre', function(req, res) {

    res.setHeader('Content-Type', 'text/plain');

    res.send('Hé ho, c\'est privé ici !');

})

.use(function(req, res, next){

    res.setHeader('Content-Type', 'text/plain');

    res.status(404).send('Page introuvable !');

});

*/
/*
app.get('/etage/:etagenum/chambre', function(req, res) {

    res.render('chambre.ejs', {etage: req.params.etagenum});

    //res.end('Vous êtes à la chambre de l\'étage n°' + req.params.etagenum);

}); */

app.get('/compter/:nombre', function(req, res) {

    var noms = ['Robert', 'Jacques', 'David'];

    res.render('page.ejs', {compteur: req.params.nombre, noms: noms});

});


app.listen(8080);app.get('/compter/:nombre', function(req, res) {

    var noms = ['Robert', 'Jacques', 'David'];

    res.render('page.ejs', {compteur: req.params.nombre, noms: noms});

});