import React from 'react';
import { Row, Col, Card, Container, TextInput, Button } from 'react-materialize';

import { Link } from 'react-router-dom';
import { login } from '../../actions/user';
const Login = () => {
	const handleLogin = (ev: React.MouseEvent): void => {
		console.log(ev);
	};

	return (
		<Container>
			<Row>
				<Col m={6} s={12} offset='m3'>
					<Card
						actions={[
							<Link to='/signup' key='1'>
								Signup instead
							</Link>,
						]}
						className='blue-grey darken-1'
						textClassName='white-text'
						title='Login'
					>
						<Row>
							<TextInput id='TextInput-4' label='username' />
						</Row>
						<Row>
							<TextInput id='TextInput-4' label='Password' password />
						</Row>
						<Row>
							<Button waves='light' onClick={handleLogin}>
								Login
							</Button>
						</Row>
					</Card>
				</Col>
			</Row>
		</Container>
	);
};

export { Login };
