function hostGame() {
  window.location.replace("/host");
}

function joinGame() {
  const divv = document.getElementById("content");
  divv.innerHTML = `<form method="post" class="buttons">
    <h1>Name</h1>
    <input type="text" placeholder="Pick a name!" name="name" value="" />
    <h1>Room Code</h1>
    <input
        type="text"
        placeholder="Type Room Code"
        name="code"
        value=""
    /><button type="submit" name="join">Join a Room</button>
</form>`;
}
