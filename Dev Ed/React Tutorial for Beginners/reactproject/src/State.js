import React, {useState} from 'react';

function State(){

  let state = false;

  let [count, setCount] = useState(0);
  let [isRed, setRed] = useState(state);

  function increment() {
    setCount(
      ++count
    );
  }

  function decrement() {
    setCount(
      --count
    );
  }

  function changeTextColor() {
    setRed(
      !isRed
    );
  }

  return(
    <div className="tweet">
      <p>{count}</p>
      <button onClick={increment} className="positive">Increment</button>
      <button onClick={decrement} className="negative">Decrement</button>
      <p className={isRed ? 'red-text' : ''}>Change my text color!</p>
      <button onClick={changeTextColor}>Change text color</button>
    </div>
  );
}

export default State;