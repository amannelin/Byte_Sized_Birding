// TODO: stop redirect if ebird call returns nothing
// TODO: WAITING MESSAGE
// let autocomplete;

function initMap() {
    const map = new google.maps.Map(document.getElementById("map"), {
      zoom: 8,
      center: { lat: 44.977753, lng: -93.2650108 },
    });
      let autocomplete = new google.maps.places.Autocomplete(
        document.getElementById("address"),
      );
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
        $.post('/ebird-call', data, (res, status) =>{
            alert(res);
        $.get('/flickr-call', (res) => {
            alert(res);
        $.get('/xeno-canto-call', (res) => {
          alert(res);
          $.get('/save-birds', (res) =>{
              alert(res);
              window.location.replace('/bird-list');
            });
          });
        });
      })
    }
      else {
        alert("Geocode was not successful for the following reason: " + status);
      }

    });
  }
  