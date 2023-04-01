var socketio = io();
let goldValue = [];
socketio.on("userStartGame", (data) => {
  const divLobby = document.getElementById("lobby");
  divLobby.innerHTML = "";
  const divGame = document.getElementById("game");
  divGame.innerHTML = `
        <h1>GAME</h1>
        <h2> Gold: <h2> 
        <div id="gold">
        </div>`;
});

socketio.on("updateValue", (data) => {
  goldValue.push(data.gold);
  if (goldValue.length > 30) {
    goldValue.shift();
  }
  console.log(goldValue);
  console.log(data.gold);
  document.getElementById("gold").innerHTML = data.gold;
});
