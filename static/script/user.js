var socketio = io();
let goldValue = [];
socketio.on("userStartGame", (data) => {
  const divLobby = document.getElementById("lobby");
  divLobby.innerHTML = "";
  const divGame = document.getElementById("game");
  divGame.innerHTML = `
        <h1>GAME</h1>
        <h2> Money: </h2>
        <div id="money"></div>
        <h2> Wallet </h2>
        <div id="wallet">Pusto Brachu</div>
        <h2> Gold: </h2> 
        <div id="goldvalue"></div>
        <button class="buy" onclick="buyGold()">Buy Gold</button>
        `;
  document.getElementById("money").innerHTML = data.moneyOnStart;
});
socketio.on("updateWallet", (data) => {
  document.getElementById("money").innerHTML = data.money;
  document.getElementById("wallet").innerHTML = data.wallet.gold;
  // console.log();
});
function buyGold() {
  socketio.emit("buy", { whatBuy: "Gold" });
}
socketio.on("updateValue", (data) => {
  goldValue.push(data.gold);
  if (goldValue.length > 30) {
    goldValue.shift();
  }
  console.log(goldValue);
  console.log(data.money);
  document.getElementById("goldvalue").innerHTML = data.gold;
});
