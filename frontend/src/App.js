import {Wrapper, Status} from '@googlemaps/react-wrapper';
import {useState, useRef, useEffect} from 'react';
import './App.css';

const App = () => {
	const [data, setData] = useState(null);
	const [radius, setRadius] = useState(1000);
	const [energyReport, setEnergyReport] = useState(null);
	const [loading, setLoading] = useState(false);

	const render = (status) => {
		if (status !== Status.SUCCESS)
			return 'loading';
	}

	const sendData = async () => {
		console.log('generating report');
		setLoading(true);

		let url = 'http://localhost:5000/locationlocationlocation';
		url += '?lat=' + data.position.lat();
		url += '&lng=' + data.position.lng();
		url += '&rad=' + radius;
		const response = await fetch(url);
		const report = await response.json();

		console.log(report);
		setLoading(false);
		setEnergyReport(report);
	}

	return (
		<div className='App'>
			<Loading active={loading} />
		    <div className={energyReport && 'scoot-left'}>
		        <Wrapper apiKey={'AIzaSyBZUH8Ld_4GB9ct-Vc-rLDV_fBMQFm2pKs'} render={render}>
                    <Map setData={setData}/>
                    {data && <Marker data={data} radius={radius}/>}
                </Wrapper>
		    </div>
			<div className='input'>
				Slide to set radius: {radius} meters
				<input type='range'
				       id='radius-slider'
				       max={16000}
				       value={radius}
				       step={100}
				       onInput={(ev) => {
					       setRadius(ev.target.value);
				       }}
				/>
				Area: {(radius * radius * 3.14).toLocaleString('en-US', {
				maximumSignificantDigits: 3,
			})} square meters<br/>
				<button onClick={sendData} disabled={!data}>
					{data ? 'Location location location!' : 'Click map to set location'}
				</button>
			</div>
			<Result report={energyReport}/>
		</div>
	);
}

const Map = ({setData}) => {
	const ref = useRef();

	useEffect(() => {
		if (ref.current) {
			const map = new window.google.maps.Map(ref.current, {
				center: {lat: 40.1138069, lng: -88.2270992}, //UIUC coordinates
				zoom: 13,
			});
			map.addListener('click', (ev) => {
				setData({map, position: ev.latLng});
			});
		} else {
			console.warn('not loaded');
		}
	}, [setData]);

	return <div ref={ref} id='map'/>
}

const Marker = ({data, radius}) => {
	useEffect(() => {
		const marker = new window.google.maps.Marker();
		marker.setOptions(data);

		const circle = new window.google.maps.Circle({
			strokeColor: '#EA4335',
			strokeOpacity: 0.9,
			strokeWeight: 2,
			fillColor: '#EA4335',
			fillOpacity: 0.25,
			map: data.map,
			center: data.position,
			radius: parseInt(radius),
		});

		return () => {
			if (marker)
				marker.setMap(null);
			if (circle)
				circle.setMap(null);
		}
	}, [data, radius]);
}

const Result = ({report}) => {
	if (!report)
		return false;

	const {ranking, ...data} = report;

	return (
		<div className='output'>
			<div>{data && ranking.map((energySource, index) => {
                console.log(index === 0);
                return (
                    <div className={(index === 0 ? 'best-option ' : '') + 'energy-card'} key={index}>
                        <img src={'/' + energySource + '.png'} className='icon' alt={energySource}/>
                        <div>
                            <div className='big-text'>
                                {energySource.charAt(0).toUpperCase() + energySource.slice(1)} power
                            </div>
                            {data[energySource].toLocaleString('en-US', {
                                maximumSignificantDigits: 3,
                            })} megawatts
                        </div>
                    </div>
                )
            })}</div>
		</div>
	)
}

const Loading = ({active}) => {
	return (active && <div className='loading'>
		<img src='/loading.gif' alt='loading'/>
	</div>);
}

export default App;
