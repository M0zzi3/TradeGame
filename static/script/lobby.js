var socketio = io();
socketio.on("message", (data) => {
    console.log(data);
    if ((data.action = "STARTGAME")) {
        startGame();
    };
});
function startGame() {
    const divGame = document.getElementById("game");
    divGame.innerHTML = `
        magiczna gra właśnie sie zaczeła
        <img src="https://media2.giphy.com/media/v1.Y2lkPTc5MGI3NjExYjExZTQ5ZGY4OTY2Nzc4Njc2MTc2YjJhMzc3YjEzYjhlYjI5YTEwMCZjdD1z/atgjIXHBJNaSGcwm7r/giphy.gif">`;
  };