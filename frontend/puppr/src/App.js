import React, { Component, Fragment } from 'react';
import Navigation from './Navigation'
import Signup from './Signup';
import './App.css';
import MainFeed from './MainFeed';

class App extends Component {
  constructor(props){
    super(props);
  }
  render() {
    return (
			<div>
				<Navigation />
				Landing Page
        <MainFeed/>
			</div>
		);
  }
}

export default App;
