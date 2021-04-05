

function localization() {
    if (window.navigator.geolocation) {
        window.navigator.geolocation
            .getCurrentPosition(console.log, console.log);
    } else {
        console.log("LOCATION FAIL")
    }
}