function hostGame() {
  window.location.replace("/host");
}

function joinGame() {
  const divv = document.getElementById("content");
  divv.innerHTML = `<form method="post" class="buttons">
    <label>Name:</label
    ><input type="text" placeholder="Pick a name!" name="name" value="" /><input
        type="text"
        placeholder="Room Code"
        name="code"
        value=""
    /><button type="submit" name="join">Join a Room</button>
</form>`;
}
