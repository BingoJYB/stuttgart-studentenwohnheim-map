// Initialize the platform object:
let platform = new H.service.Platform({
  apikey: "IguusxFixBkAf3lKQdEyISmOGXvITFpQuiap17xkWb8",
});

// Obtain the default map types from the platform object
var maptypes = platform.createDefaultLayers();

// Instantiate (and display) a map object:
var map = new H.Map(
  document.getElementById("map"),
  maptypes.vector.normal.map,
  {
    zoom: 10,
    center: { lng: 13.4, lat: 52.51 },
  }
);
