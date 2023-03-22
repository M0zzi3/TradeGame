function hostGame() {
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

            let joinGame = false;

            for (let gamecode in data) {
                console.log(gamecode);
                if (roomCode == gamecode) {
                    joinGame = true;
                    break;
                }
            }

            if (joinGame) {
                console.log("GAME JOIN")
                window.location.replace("/joinRoom");
                // const pageContent = document.getElementsByClassName("content")
                // pageContent.innerHTML = document.textContent("joinRoom.html")
            }

        } else {
            console.log(`Error: ${xhr.status}`);
        }
    }
}
