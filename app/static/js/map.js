let addMarkerToGroup = (group, coordinate, html) => {
  let marker = new H.map.Marker(coordinate);
  // add custom data to the marker
  marker.setData(html);
  group.addObject(marker);
};

let addInfoBubble = (wohnungen) => {
  let group = new H.map.Group();

  map.addObject(group);

  // add 'tap' event listener, that opens info bubble, to the group
  group.addEventListener(
    "tap",
    (event) => {
      // event target is the marker itself, group is a parent event target
      // for all objects that it contains
      let bubble = new H.ui.InfoBubble(event.target.getGeometry(), {
        // read custom data
        content: event.target.getData(),
      });
      // show info bubble
      ui.addBubble(bubble);
    },
    false
  );

  // iterate over wohnungen and add each bubble info
  for (let wohnung of wohnungen) {
    addMarkerToGroup(
      group,
      {
        lat: wohnung.items[0].position.lat,
        lng: wohnung.items[0].position.lng,
      },
      '<div><a href="http://www.mcfc.co.uk" target="_blank">Manchester City</a>' +
        "</div><div >City of Manchester Stadium<br>Capacity: 48,000</div>"
    );
  }
};

let moveMapToCity = (city) => {
  map.setCenter({
    lat: city.items[0].position.lat,
    lng: city.items[0].position.lng,
  });
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

// call geocoding service for each address
let promises = [];
for (let address of addresses) {
  promises.push(
    service.geocode({
      q: address,
    })
  );
}

Promise.all(promises).then((wohnungen) => {
  addInfoBubble(wohnungen);
});

// move to Stuttgart
service.geocode(
  {
    q: "Stuttgart",
  },
  moveMapToCity,
  onError
);
