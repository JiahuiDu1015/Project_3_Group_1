// script.js

// Initialize the map
const map = L.map('map').setView([ -33.865143, 151.209900], 4); // Center at [0,0] with zoom level 2

// Add a tile layer to the map
L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
    attribution: '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors'
}).addTo(map);

// Function to get coordinates for a given state using Nominatim
async function getCoordinates(stateName) {
    const response = await fetch(`https://nominatim.openstreetmap.org/search?q=${encodeURIComponent(stateName)}&format=json&limit=1`);
    const data = await response.json();
    if (data && data.length > 0) {
        const { lat, lon } = data[0];
        return [parseFloat(lat), parseFloat(lon)];
    }
    return null;
}

// Function to determine color based on depth
function getColorEQ(depth) {
    let color = "";
    if (depth>80){
            color =  '#800026';
    }
    else if(depth> 40){
            color =  '#BD0026';
    }
   else{
            color = '#FD8D3C';
    }
    console.log(color)
    return color;
}


//Adding legend to the map

function createLegend() {
    var legend = L.control({position: 'bottomright'});

    legend.onAdd = function () {
        var div = L.DomUtil.create('div', 'legend');
        var grades = [80,40];
        var labels = [];

        // Add legend title
        div.innerHTML += '<strong>State(Counts Job)</strong><br>';

        // Add legend color entries
        for (var i = 0; i < grades.length; i++) {
            div.innerHTML +=
                '<i style="background:' + getColorEQ(grades[i] + 1) + '"></i> ' +
                grades[i] + (grades[i + 1] ? '&ndash;' + grades[i + 1] + '<br>' : '+');
        }

        return div;
    };

    legend.addTo(map);
}

//Getting the earthquick data 
function init_get_data_visualize() {
// Load data
d3.csv("state_job_count.csv").then(async (jobData) => {
    // Convert CSV data to a more usable format
    const jobCounts = jobData.map(d => ({
        state: d.State,
        count: +d.count
    }));

    // Add bubbles to the map based on job counts
    for (const d of jobCounts) {
        const coordinates = await getCoordinates(d.state);
        if (coordinates) {
            const [lat, lon] = coordinates;
            const radius = Math.sqrt(d.count) * 10800; // Adjust size based on count

            L.circle([lat, lon], {
                color: getColorEQ(d.count),
                fillColor: getColorEQ(d.count),
                fillOpacity: 0.5,
                radius: radius
            }).addTo(map).bindPopup(`<b>${d.state}</b><br>Count: ${d.count}`);
        } else {
            console.warn(`No coordinates found for ${d.state}`);
        }
    }
        
});
  // Adding legend to the map
  createLegend();
}

//call the function to visualized

init_get_data_visualize()