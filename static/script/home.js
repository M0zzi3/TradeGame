
function hostGame() {
    console.log("asdasdasdasd")
    window.location.replace("/host");
}





function joinGame() {
    var roomCode = document.getElementsByClassName("room code")[0].value;
    console.log("JSON REQUEST")

    var xhr = new XMLHttpRequest();
    xhr.open("GET", "/getGames");
    xhr.send();
    xhr.responseType = "json";

    xhr.onload = () => {
    if (xhr.readyState == 4 && xhr.status == 200) {
        const data = xhr.response;
        console.log(data);



    } else {
        console.log(`Error: ${xhr.status}`);
    }

};




}
