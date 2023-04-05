var socketio = io();
let goldValue = [];
walletGold = 0;
socketio.on("userStartGame", (data) => {
  console.log("stargGame");
  document.getElementById("lobby").style.display = "none";
  document.getElementById("game").style.display = "block";
  document.getElementById("money").innerHTML = data.moneyOnStart + "$";
});
socketio.on("updateWallet", (data) => {
  document.getElementById("money").innerHTML = data.money + "$";
  document.getElementById("wallet-gold").innerHTML = data.wallet.gold;
  walletGold = data.wallet.gold;
  updatePotentialGoldValue();
});
function buyGold() {
  socketio.emit("buy", { whatBuy: "Gold" });
}
function sellGold() {
  socketio.emit("sell", { whatSell: "Gold" });
}

function updatePotentialGoldValue() {
  document.getElementById("potential-gold-value").innerHTML =
    walletGold * goldValue[goldValue.length - 1] + "$";
}
socketio.on("updateValue", (data) => {
  goldValue.push(data.gold);
  if (goldValue.length > 30) {
    goldValue.shift();
  }
  console.log(goldValue);
  document.getElementById("gold-value").innerHTML = data.gold;
  updatePotentialGoldValue();
});
