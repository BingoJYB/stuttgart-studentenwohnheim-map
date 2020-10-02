let moveMapToPos = (map, latitude, longitude) => {
  map.setCenter({ lat: latitude, lng: longitude });
  map.setZoom(12);
};

let onError = (error) => {
  alert(error.message);
};

//Step 1: initialize communication with the platform
let platform = new H.service.Platform({
  apikey: api_key,
});
let defaultLayers = platform.createDefaultLayers();

//Step 2: initialize a map - this map is centered over Europe
let map = new H.Map(
  document.getElementById("map"),
  defaultLayers.vector.normal.map,
  {
    center: { lat: 50, lng: 5 },
    zoom: 4,
    pixelRatio: window.devicePixelRatio || 1,
  }
);
// add a resize listener to make sure that the map occupies the whole container
window.addEventListener("resize", () => map.getViewPort().resize());

//Step 3: make the map interactive
let behavior = new H.mapevents.Behavior(new H.mapevents.MapEvents(map));

// Create the default UI components
let ui = H.ui.UI.createDefault(map, defaultLayers);

// Get an instance of the geocoding service:
let service = platform.getSearchService();

service.geocode(
  {
    q: "Stuttgart",
  },
  (result) => {
    console.log(result);
    moveMapToPos(
      map,
      result.items[0].position.lat,
      result.items[0].position.lng
    );
  },
  onError
);
