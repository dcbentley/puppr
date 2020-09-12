import React from 'react';

import { Fragment } from 'react';
import {
	Collapse,
	Navbar,
	NavbarToggler,
	NavbarBrand,
	Nav,
	NavItem,
	NavLink,
	UncontrolledDropdown,
	DropdownToggle,
	DropdownMenu,
	DropdownItem,
} from 'reactstrap';


class Navigation extends React.Component {
	constructor(props) {
		super(props);

		this.toggle = this.toggle.bind(this);
		this.state = {
			isOpen: false,
		};
	}
	toggle() {
		this.setState({
			isOpen: !this.state.isOpen,
		});
	}

	render() {
		return (
			<div>
				<Fragment>
					<Navbar color='light' light expand='md'>
						<NavbarBrand href='/'>Puppr.me</NavbarBrand>
						<NavbarToggler onClick={this.toggle} />
						<Collapse isOpen={this.state.isOpen} navbar>
							<Nav className='ml-auto' navbar>
								<NavItem>
									<NavLink href='/components/'>Components</NavLink>
								</NavItem>
								<NavItem>
									<NavLink href='https://github.com/dcbentley/puppr'>
										GitHub
									</NavLink>
								</NavItem>
								<UncontrolledDropdown nav inNavbar>
									<DropdownToggle nav caret>
										Options
									</DropdownToggle>
									<DropdownMenu right>
										<DropdownItem>User Profile based on state</DropdownItem>
										<DropdownItem divider />
										<DropdownItem>Sign Out</DropdownItem>
									</DropdownMenu>
								</UncontrolledDropdown>
							</Nav>
						</Collapse>
					</Navbar>
				</Fragment>
			</div>
		);
	}
}

export default Navigation;