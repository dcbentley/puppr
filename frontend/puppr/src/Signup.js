import React, { Component } from 'react';
import { Button } from 'reactstrap';
import Features from './Features';

class Signup extends Component {
	render() {
		return (
			<div>
				<div className='.col-6'>
					<section>Puppr.me</section>
					<section>A social space for pups</section>
					<Button color='primary' size='md'>
						Signup
					</Button>{' '}
					<Button color='secondary' size='md'>
						Log-in
					</Button>
				</div>
                <Features/>
			</div>
		);
	}
}

export default Signup;
