var socketio = io();

const usersInLobby = document.getElementById("usersInLobby");
const divGame = document.getElementById("game");

let users = [];

const addUser = (userName) => {
  let content = "";
  users.push(userName);
  for (var i = 0; i < users.length; i++) {
    content += `
    <div class="user">
      <strong>${users[i]}</strong>
    </div>`;
  }
  usersInLobby.innerHTML = content;
};

function startGame() {
  socketio.emit("startGame", { data: "Test" });
  document.getElementById("lobby").innerHTML = "";
  divGame.innerHTML = `
  You Are Host
    <div class="timer">
      <span id="countdown">15</span>
    </div>`;
  var countdownTimer = setInterval("countdown()", 1000); // Tu jeszcze do poprawy
}

var seconds = 15; // Tu jeszcze do poprawy
function countdown() {
  // Tu jeszcze do poprawy
  seconds = seconds - 1;
  if (seconds < 0) {
    clearInterval(countdownTimer);
  } else {
    document.getElementById("countdown").innerHTML = seconds;
  }
}

socketio.on("message", (data) => {
  if (data.action == "ADDUSER") {
    addUser(data.name);
  } else {
    return;
  }
});
