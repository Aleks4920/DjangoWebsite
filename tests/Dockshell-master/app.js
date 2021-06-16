var express = require("express");
var http = require("http");
var path = require("path");
var server = require("socket.io");
var pty = require("pty.js");

var opts = require("optimist")
    .options({
        port: {
            demand: true,
            alias: "p",
            description: "Dockshell listen port"
        },
    }).boolean("allow_discovery").argv;

process.on("uncaughtException", function(e) {
    console.error("Error: " + e);
});

var app = express();
app.use("/", express.static(path.join(__dirname, "public")));

var httpserv = http.createServer(app).listen(opts.port, function() {
    console.log("Serving dockshell on port " + opts.port);
});

var io = server(httpserv, {
    path: "/dockshell/socket.io",
    pingTimeout: 5000
});

io.on("connection", function(socket){

    var term = pty.spawn("/bin/bash", [], {
        name: "xterm-256color",
        cols: 80,
        rows: 30
    });

    console.log(`Started new session with PID: ${term.pid}`);
    term.on("data", function(data) {
        socket.emit("output", data);
    });
    term.on("exit", function(code) {
        console.log(`Session with PID ${term.pid} ended`);
    });
    socket.on("resize", function(data) {
        term.resize(data.col, data.row);
    });
    socket.on("input", function(data) {
        term.write(data);
    });
    socket.on("disconnect", function() {
        term.end();
    });
})
