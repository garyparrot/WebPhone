window.onload = function() {
    document.querySelector("#display").addEventListener("click", onDisplayClicked)
    setInterval(updateDisplay, 2000);
}

function onDisplayClicked(e) {
    const image = document.querySelector("#display")
    const X = image.naturalWidth  * (e.offsetX / image.width);
    const Y = image.naturalHeight * (e.offsetY / image.height);
    const payload = { X, Y };
    console.log(e);
    console.log("Sending Click Request", JSON.stringify(payload));

    fetch('/api/phone/click', {
        body: JSON.stringify(payload),
        cache: 'no-cache',
        method: 'POST',
        headers: {
            'content-type': 'application/json'
        }
    }).then(function(response){ return response.json(); })
      .then(function(result){console.log(result)})
      .catch(function(_){console.error("Failed")})
}

function updateDisplay() {
    const img = document.querySelector("#display");
    img.src = "/api/phone/display?" + Math.random();
    console.log("Triggered");
}
