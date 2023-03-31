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
  divGame.innerHTML = `magiczna gra właśnie sie zaczeła a ty jesteś jej hostem`;
}

socketio.on("message", (data) => {
  if (data.action == "ADDUSER") {
    addUser(data.name);
  } else {
    return;
  }
});
