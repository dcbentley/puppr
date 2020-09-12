import React, { Component } from 'react';
import { render } from 'react-dom';

class MainFeed extends Component {
	constructor(props) {
		super(props);
		this.state = {
			posts: [],
		};
	}
	async componentDidMount() {
		// Local API request
		const URL = '/posts/';

		const headers = {
			'Content-Type': 'application/json',
		};

		// Fetch
		await fetch(URL, {
			method: 'GET',
			headers: headers,
		})
			// setState for posts
			.then((res) => res.json())
			.then((res) => {
				console.log(res);
				this.setState({ posts: res });
			});
	}
	setAllUserPosts = (posts) => {
		this.setState({ posts: posts });
	};

	render() {
        let allUserPosts = this.state.posts;
        console.log(allUserPosts)
		return (
			<div>
				{allUserPosts.map((post, index) => {
					return post.post;
				})}
			</div>
		);
	}
}

export default MainFeed;
