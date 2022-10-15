import {Wrapper, Status} from '@googlemaps/react-wrapper';
import {useState, useRef, useEffect} from 'react';

// get latitude with markerData.position.lat();
// get longitiude with markerData.position.lng();

const LocationPage = () => {
  const [markerData, setMarkerData] = useState(null);

  const render = (status) => {
    if (status !== Status.SUCCESS)
      return 'loading';
  }

  return (
    <Wrapper apiKey={'AIzaSyBZUH8Ld_4GB9ct-Vc-rLDV_fBMQFm2pKs'} render={render}>
      Click to set location <br/><br/>
      <Map setMarkerData={setMarkerData}/>
      {markerData && <Marker data={markerData}/>}
    </Wrapper>
  );
}

const Map = ({setMarkerData}) => {
  const ref = useRef();

  useEffect(() => {
    if (ref.current) {
      const map = new window.google.maps.Map(ref.current, {
        center: {lat: 40.1138069, lng: -88.2270992}, //UIUC coordinates
        zoom: 3.5,
      });
      map.addListener('click', (e) => {
        setMarkerData({map, position: e.latLng});
      });
    } else {
      console.warn('not loaded');
    }
  }, [setMarkerData]);

  return <div ref={ref} id='map'/>
}

const Marker = ({data}) => {
  useEffect(() => {
    const marker = new window.google.maps.Marker();
    marker.setOptions(data);

    return () => {
      if (marker)
        marker.setMap(null);
    }
  }, [data]);
}

export default LocationPage;
