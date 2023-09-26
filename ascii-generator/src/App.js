import React, { useState, useEffect } from 'react';
import './App.css';
import { useTheme } from './ThemeContext';
import axios from 'axios';

function App() {
  const [inputText, setInputText] = useState('');
  const [asciiOutput, setAsciiOutput] = useState('');
  const { theme, setTheme } = useTheme();

  useEffect(() => {
    if (theme === 'dark') {
      document.body.style.backgroundColor = '#2c3e50';
      document.body.style.color = '#ecf0f1';
    } else {
      document.body.style.backgroundColor = '#ecf0f1';
      document.body.style.color = '#2c3e50';
    }
  }, [theme]);

  const toggleTheme = () => {
    setTheme(prevTheme => prevTheme === 'dark' ? 'light' : 'dark');
  };

  const handleSubmit = (e) => {
    e.preventDefault();
    axios.post('http://localhost:5000/generate-ascii', { text: inputText })
        .then(response => {
            const asciiResult = response.data.result;
            setAsciiOutput(asciiResult);
        })
        .catch(error => {
            console.error("Error generating ASCII:", error);
        });
};

  return (
    <div className={`App ${theme}`}>
      <button className="lightmode" onClick={toggleTheme}>
         {theme === 'dark' ? 'Light' : 'Dark'} Mode
      </button>
      <h1>ASCII Generator</h1>
      <form onSubmit={handleSubmit}>
        <textarea 
          value={inputText} 
          onChange={(e) => setInputText(e.target.value)} 
          placeholder="Enter text here..."
        />
        <button type="submit">Generate ASCII</button>
      </form>
      <pre>{asciiOutput}</pre>
    </div>
  );
}

export default App;
