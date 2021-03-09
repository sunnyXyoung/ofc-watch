const express = require("express");
const app = express();
const http = require('http');
const cors = require('cors');
const path = require('path');

// middleware

const corsOptions = {
    origin: [
        'http://localhost:8080',
        'http://localhost:2100',
    ],
    methods: 'GET,HEAD,PUT,PATCH,POST,DELETE,OPTIONS',
    credentials: true,
    allowedHeaders: ['Content-Type', 'Authorization', 'X-CSRF-TOKEN'],
}

app.use(cors(corsOptions));
// route middleware
app.use(express.static(path.join(__dirname,'data')))

const history = require('connect-history-api-fallback');
app.use(history());
app.use(express.static(path.join(__dirname, 'dist')));


// start server
const server = http.createServer(app);


server.listen(3000, () => console.log('HTTP start on port:' + 3000));