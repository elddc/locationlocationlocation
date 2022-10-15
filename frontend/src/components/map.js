import {Wrapper, Status} from '@googlemaps/react-wrapper';
import {useState, useRef, useEffect} from 'react';

const Map = () => {
  const render = (status) => {
    if (status !== Status.SUCCESS)
      return 'loading';
  }

  return (
    <Wrapper apiKey={'AIzaSyBZUH8Ld_4GB9ct-Vc-rLDV_fBMQFm2pKs'} render={render}>
      Map:
      <MapInner />
    </Wrapper>
  );
}

const MapInner = () => {
  const ref = useRef();
  const center = { lat: 40.1138069, lng: -88.2270992 }; //UIUC coordinates
  const zoom = 3.5;

  useEffect(() => {
    if (ref.current)
      new window.google.maps.Map(ref.current, {center, zoom});
  });

  return <div ref={ref} id={'map'}/>
}

export default Map;
