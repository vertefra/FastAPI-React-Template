import * as React from 'react';
import { BrowserRouter as Router, Route, Switch } from 'react-router-dom';
import { Login } from './modules/login/Login';
import { Signup } from './modules/login/Signup';

import 'materialize-css';
import 'materialize-css/dist/css/materialize.min.css';
import './App.css';

export const App = () => {
	return (
		<div>
			<Router>
				<Switch>
					<Route path='/login' component={Login}></Route>
					<Route path='/signup' component={Signup}></Route>
				</Switch>
			</Router>
		</div>
	);
};
