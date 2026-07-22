const   express = require("express")
const   app = express();
const   http = require("http");
const   server = http.createServer(app)
const   { Server } = require("socket.io")
const   io = new Server(server)

app.get("/" , (req,res) => {
    res.sendFile(__dirname + "/index.html"); // ไม่จำเป็นต้องใส่ path ที่อยู่เลย ใส่ไฟล์ที่ต้องการอ่านได้เลย
});

io.on("connection" , (socket) => {
    console.log("a user connection");

    socket.on("disconnect",() =>{
    // socket.on("disconnect", (socket) => {
        console.log("user disconnect");
    });
});

server.listen(3000, () => {
    console.log("listening on *:3000");
});