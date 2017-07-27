/* displays the map centered at Australia */

function myMap() {
    var mapOptions = {
        center: new google.maps.LatLng(-29, 137.77),
        zoom: 4,
        mapTypeId: google.maps.MapTypeId.ROADMAP
    }
    var map = new google.maps.Map(document.getElementById("map"), mapOptions);
}