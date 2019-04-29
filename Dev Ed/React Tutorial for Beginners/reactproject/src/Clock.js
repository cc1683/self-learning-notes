import React from 'react';

// function Clock(props) {
//   return(
//     <div>
//       <p>It is {props.date.toLocaleTimeString()}</p>
//     </div>
//   )
// }

  //! Converting a function to class

class Clock extends React.Component{
  render() {
    return(
      <div>
        <p>It is {this.props.date.toLocaleTimeString()}</p>
      </div>
    )
  }
}

export default Clock;