var express = require('express');
const fs = require('fs')
const path = require('path')


var liste5elem;

var app = express();
app.use(express.static("public"));

const spawn = require("child_process").spawn;
const pythonProcess = spawn('python3', ["./views/script.py", "liste5" ]);

pythonProcess.stdout.on('data', function (data) {
     liste5elem = JSON.parse(data.toString());
    // console.log(liste5elem[0]);
    // console.log(liste5elem[1]);

       //console.log(data.toString());
});

pythonProcess.stderr.on('data', (data) => {
    console.log(`stderr: ${data}`);
});

pythonProcess.on('close', (code) => {
    console.log(`child process exited with code ${code}`);
});

// const pythonProcess2 = spawn('python3', ["./views/script.py", "liste" ]);

// pythonProcess2.stdout.on('data', function (data) {
//     liste = JSON.parse(data.toString());
//       console.log(data.toString());
// });

// pythonProcess2.stderr.on('data', (data) => {
//    console.log(`stderr: ${data}`);
// });

// pythonProcess2.on('close', (code) => {
//    console.log(`child process exited with code ${code}`);
// });

//console.log(pythonProcess);
// ls.stdout.on('data', (data) => {
//     console.log(`stdout: ${data}`);
//   });
  
//   ls.stderr.on('data', (data) => {
//     console.log(`stderr: ${data}`);
//   });
  
//   ls.on('close', (code) => {
//     console.log(`child process exited with code ${code}`);
//   });







app.get('/accueil', function (req, res) {

    res.setHeader('Content-Type', 'text/html');
    res.render('accueil.ejs',{liste5elem : liste5elem});

})

// app.get('/liste', function (req, res) {

//     res.setHeader('Content-Type', 'text/html');
//     res.render('liste.ejs',{liste : liste});

// })

app.listen(8080);

