import React from 'react';

function sayHello(){

  function sayHello() {
    return console.log('Hello World!');
  }

  return(
    <div>
      <h2>This is say Hello component</h2>
      <button onClick={sayHello}>Click and say hello!</button>
    </div>
  )
}

export default sayHello;