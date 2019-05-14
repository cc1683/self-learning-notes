import React from 'react'

// function Greet() {
//   return <h1>Hello Matthew</h1>
// }

//! arrow function

// const Greet  = ({ age, job }) => {
//   return(
//     <div>
//       <h1>Hello Matthew</h1>
//       <p>I am { age } years old</p>
//       <p>My job is { job }</p>
//     </div>
//   )
// }

const Greet  = (props) => {
  return(
    <div>
      <h1>Hello Matthew</h1>
      <p>{ props.children }</p>
      <p>I am { props.age } years old</p>
      <p>My job is { props.job }</p>
    </div>
  )
}
export default Greet;
