var socketio = io();
socketio.on("message", (data) => {
  console.log(data);
  if ((data.action = "STARTGAME")) {
    startGame();
  }
});
function startGame() {
  const divGame = document.getElementById("game");
  divGame.innerHTML = `
        magiczna gra właśnie sie zaczeła
        Gold: 
        <div id="gold">
        </div>`;
}

socketio.on("updateValue", (data) => {
  console.log("catch");
  document.getElementById("gold").innerHTML = data.gold;
});
