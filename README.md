# locationlocationlocation

A project for CodeADA 2022, a two day hackathon held by WCS.

Participants choice winner!

## Description
Some energy sources are better than others for certain amount of land. Different contexts of locations make a rapid 
clean energy transition more complicated.

`locationlocationlocation` is a data-driven solution that allows energy providers and community members to determine 
the best energy source for their area, with a simple and intuitive interface.

## Screenshots
![home page](https://i.imgur.com/xRH6ni5.png)

Select an area to analyze by clicking on the map to set a location, and using the slider to set a radius.

![input](https://i.imgur.com/Q6HNviW.png)

Click the `Location location location!` button to predict the amount of renewable energy the selected area can produce,
out of four common renewable energy sources, and a ranking of the recommended sources for maximum efficiency. 

![result](https://i.imgur.com/eco1yOq.png)

## Run on your device

Generate a Google Maps API key [here](https://console.cloud.google.com/google/maps-apis), and replace the placeholder 
API key on line `36` of `/frontend/src/App.js`.

Run `flask start` in the `/backend` directory, and run `npm start` in the `/frontend` directory to start the app!
