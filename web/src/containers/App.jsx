import React from 'react'
import { Link, browserHistory } from 'react-router'
import store from '../stores/store.js'


export default function App({ children }) {
	return (
		<div>
            <Link to="/air/disease-evolution">Disease Evolution</Link>
            <Link to="/air/air-pollution">Air Pollution</Link>
            <Link to="/air/predictions">Air Pollution</Link>
			{children}
		</div>
	)
}
