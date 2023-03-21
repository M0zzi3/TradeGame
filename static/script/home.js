
function hostGame() {
    console.log("asdasdasdasd")
    window.location.replace("/host");
}





function joinGame() {
    const divv = document.getElementById("content");
    divv.innerHTML = `<form method="post" class="buttons">
    <label>Name:</label>
    
    <input type="text" placeholder="Pick a name!" name="name" value="" />
    
    <button type="submit" name="join">Join a Room</button>
</form>`;
}
