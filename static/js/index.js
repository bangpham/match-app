

function setTime(id){
    var xhr = new XMLHttpRequest();
    xhr.open('GET', 'time');
    xhr.send(null);

    xhr.onreadystatechange = function() {
        if(xhr.readyState === 4){
            if(xhr.status === 200){
                var json = JSON.parse(xhr.responseText);
                document.getElementById("time").innerHTML = moment.utc(json.current).local();
            } else {
                console.log('Error: ' + xhr.status);
            }
        }
    }
}

window.onload = function() {
    setTime("time")
}