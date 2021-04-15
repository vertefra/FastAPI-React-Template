import React, { useState } from 'react';
import { Link } from 'react-router-dom';
import { Row, Col, Card, Container, TextInput, Button } from 'react-materialize';
import { signup, login } from '../../actions/user';
import { User } from '../../interfaces/User';

const Signup = () => {
	const [user, updateUser] = useState<User>({
		username: '',
		email: '',
		password: '',
	});

	const handleSignup = async (ev: React.MouseEvent) => {
		ev.preventDefault();
		const registeredUser: User = await signup(user);
		const loggedInUser: User = await login(user);
		console.log(loggedInUser);
	};

	const handleChange = (ev: React.ChangeEvent<HTMLInputElement>) => {
		updateUser({
			...user,
			[ev.target.id]: ev.target.value,
		});
	};

	return (
		<Container>
			<Row>
				<Col m={6} s={12} offset='m3'>
					<Card
						actions={[
							<Link to='/login' key='1'>
								Already Registered? Login
							</Link>,
						]}
						className='blue-grey darken-1'
						textClassName='white-text'
						title='Signup'
					>
						<Row>
							<TextInput
								id='username'
								label='username'
								onChange={handleChange}
								value={user.username}
							/>
						</Row>
						<Row>
							<TextInput id='email' label='email' value={user.email} onChange={handleChange} />
						</Row>
						<Row>
							<TextInput
								id='password'
								label='Password'
								password
								value={user.password}
								onChange={handleChange}
							/>
						</Row>
						<Row>
							<Button waves='light' onClick={handleSignup}>
								Signup
							</Button>
						</Row>
					</Card>
				</Col>
			</Row>
		</Container>
	);
};

export { Signup };
