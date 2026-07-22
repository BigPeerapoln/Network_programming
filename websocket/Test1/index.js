const app = require('express')();
const http = require('http').Server(app);
const io = require('socket.io')(http);
const port = process.env.PORT || 3000;

app.get('/', (req, res) => {
    // ✅ แก้เป็น __dirname (ขีดล่าง 2 ตัว)
    res.sendFile(__dirname + '/index.html');
});

io.on('connection', (socket) => {
    console.log('a user connected');

    socket.on('chat message', msg => {
        console.log('message: ', msg);
        io.emit("chat message",msg);
    });

    socket.on('disconnect', () => {
        console.log('user disconnected');
    });
}); // ✅ ปิดบล็อก io.on ให้เรียบร้อยที่นี่

// ✅ ย้าย http.listen ออกมาอยู่นอกสุด และใช้ Backticks (`) ตรง ${port}
http.listen(port, () => {
    console.log(`Socket.IO server running at http://localhost:${port}/`);
});