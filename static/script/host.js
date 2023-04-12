var socketio = io();

const usersInLobby = document.getElementById("usersInLobby");

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
  socketio.emit("startGame", { setings: "setings" });
  document.getElementById("lobby").style.display = "none";
  document.getElementById("game").style.display = "block";
  var countdownTimer = setInterval("countdown()", 1000); // Tu jeszcze do poprawy
}

var seconds = 5; // Tu jeszcze do poprawy aby było zmienna też zapisana tam w html bo jakoś dziwnie się generauje

function countdown() {
  if (seconds <= 0) {
    seconds = 5;
    console.log("periodEnd");
    document.getElementById("countdown").innerHTML = seconds;
    periodEnd();
  } else {
    seconds = seconds - 1;
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
