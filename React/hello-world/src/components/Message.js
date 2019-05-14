import React, { Component } from 'react';

class Message extends Component {

  constructor() {
    super()
    this.state = {
      message: 'Welcome Visitor'
    }
  }

  changeName() {
    this.setState({
      message: 'You have changed the name!'
    })
  }

  render() {
    return(
      <div>
        <p>{ this.state.message }</p>
        <button onClick={ () => {this.changeName()} }>Change visitor name</button>
      </div>
    )
  }
}

export default Message;