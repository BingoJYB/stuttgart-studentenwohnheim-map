let addMarkerToGroup = (group, coordinate, html) => {
  let marker = new H.map.Marker(coordinate);
  // add custom data to the marker
  marker.setData(html);
  group.addObject(marker);
};

let addInfoBubble = (results) => {
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

  // iterate over results and add each bubble info
  for (let result of results) {
    let name = result["wohnung"][0];
    let address = result["wohnung"][1];
    let detail_url = result["wohnung"][2];

    addMarkerToGroup(
      group,
      {
        lat: result["geo"].items[0].position.lat,
        lng: result["geo"].items[0].position.lng,
      },
      "<a href=" +
        detail_url +
        ' target="_blank">' +
        "<div>" +
        name +
        "</div><div>" +
        address +
        "</div></a>"
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
for (let wohnung of wohnungen) {
  promises.push(
    service
      .geocode({
        q: wohnung[1],
      })
      .then((result) => {
        return { geo: result, wohnung: wohnung };
      })
  );
}

Promise.all(promises).then((results) => {
  addInfoBubble(results);
});

// move to Stuttgart
service.geocode(
  {
    q: "Stuttgart",
  },
  moveMapToCity,
  onError
);
