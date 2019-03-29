var express = require('express');

var app = express();
app.use(express.static("images"));


app.get('/accueil', function(req, res) {

    res.setHeader('Content-Type', 'text/html');

    res.render('accueil.ejs');

})

app.listen(8080);

