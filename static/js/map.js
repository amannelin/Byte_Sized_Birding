function initMap() {
    const map = new google.maps.Map(document.getElementById("map"), {
      zoom: 8,
      center: { lat: 44.977753, lng: -93.2650108 },
    });
    const geocoder = new google.maps.Geocoder();
    document.getElementById("submit").addEventListener("click", () => {
      geocodeAddress(geocoder, map);
    });
  }
  
  function geocodeAddress(geocoder, resultsMap) {
    const address = document.getElementById("address").value;
    geocoder.geocode({ address: address }, (results, status) => {
      if (status === "OK") {
        resultsMap.setCenter(results[0].geometry.location);
        new google.maps.Marker({
          map: resultsMap,
          position: results[0].geometry.location,
        });
        let lat = results[0].geometry.location.lat();
        let lng = results[0].geometry.location.lng();
        let address = results[0].formated_address;
        let data = {lat:lat, lng:lng, addres:address}
        console.log(lat);
        console.log(lng);
        $.post('/ebird-call', data, (res) =>{
          alert(res);
        
      });}
      else {
        alert("Geocode was not successful for the following reason: " + status);
      }

    });
  }
  