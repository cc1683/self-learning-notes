import React from 'react';
// import Hello from './sayHello';
import Tweet from './Tweet';
import State from './State';

function App() {

  //* logic before the render element

  return(
    <div>
      <h1>Hello React</h1>
      <p>This is app component</p>
      <Tweet name="John Doe" message="The true king is me!" likes="40k"></Tweet>
      <Tweet name="Steve Smith" message="lorem lipsum dude" likes="140k"></Tweet>
      <Tweet name="John Snow" message="Learn React!" likes="4k"></Tweet>
      <State></State>
    </div>
  );
}

export default App;