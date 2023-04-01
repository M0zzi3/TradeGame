var socketio = io();

const usersInLobby = document.getElementById("usersInLobby");
const divGame = document.getElementById("game");

let users = [];

socketio.on("addUser", (data) => {
  users.push(data.name);
  udpateDisplayUserInLobby();
});

socketio.on("deleteUser", (data) => {
  users.splice(users.indexOf(data.name), 1);
  udpateDisplayUserInLobby();
});

function udpateDisplayUserInLobby() {
  let content = "";
  for (var i = 0; i < users.length; i++) {
    content += `
    <div class="user">
      <strong>${users[i]}</strong>
    </div>`;
  }
  usersInLobby.innerHTML = content;
}

function startGame() {
  socketio.emit("startGame", { data: "Test" });
  document.getElementById("lobby").innerHTML = "";
  divGame.innerHTML = `
    <h1>Trade Game</h1>
    <div class="timer">
      <span id="countdown"></span>
    </div>
    Gold:
    <div id="goldvalue"></div>
    `;
  var countdownTimer = setInterval("countdown()", 1000); // Tu jeszcze do poprawy
}

var seconds = 5; // Tu jeszcze do poprawy aby było zmienna też zapisana tam w html bo jakoś dziwnie się generauje

function countdown() {
  // Tu jeszcze do poprawy
  seconds = seconds - 1;
  if (seconds < 0) {
    seconds = 5;
    console.log("periodEnd");
    periodEnd();
  } else {
    document.getElementById("countdown").innerHTML = seconds;
  }
}

function periodEnd() {
  socketio.emit("periodEnd");
}

socketio.on("updateValue", (data) => {
  document.getElementById("goldvalue").innerHTML = data.gold;
  console.log(data.gold);
});
