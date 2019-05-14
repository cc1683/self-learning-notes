import React from 'react';
import logo from './logo.svg';
import './App.css';
import Greet from './components/Greet';
import Welcome from './components/Welcome'
import Message from './components/Message'

function App() {
  return (
    <div className="App">
      <Greet age="24" job="Web Developer">
        <p>This is Children props</p>
      </Greet>
      <Welcome name="John Doe"></Welcome>
      <Welcome name="Smith"></Welcome>
      <Welcome name="Tom"></Welcome>
      <br />
      <Message></Message>
    </div>
  );
}

export default App;
