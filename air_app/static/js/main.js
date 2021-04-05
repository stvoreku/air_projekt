function showLocation(data){
    document.getElementById("output").innerHTML = data.coords;

}



function localization() {
    if (window.navigator.geolocation) {
        window.navigator.geolocation
            .getCurrentPosition(showLocation, showLocation);
    } else {
        console.log("LOCATION FAIL")
    }
}