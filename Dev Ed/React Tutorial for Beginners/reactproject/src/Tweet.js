import React from 'react';
import './App.css'

function Tweet({name, message, likes}) {
  return(
    <div className="tweet">
      <h3>Name: { name }</h3>
      <p>{ message }</p>
      <h4>Number of likes: { likes }</h4>
    </div>
  );
}

export default Tweet;