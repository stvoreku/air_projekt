function showLocation(data){
    outputElement.innerHTML = data;

}



function localization() {
    if (window.navigator.geolocation) {
        window.navigator.geolocation
            .getCurrentPosition(showLocation, showLocation);
    } else {
        console.log("LOCATION FAIL")
    }
}