import React, { useState } from 'react';
import axios from 'axios';

function App() {
  const [input, setInput] = useState('');
  const [response, setResponse] = useState(null);
  const [selectedOptions, setSelectedOptions] = useState([]);
  const [error, setError] = useState('');

  const handleSubmit = async () => {
    setError('');
    setResponse(null);

    try {
      const jsonInput = JSON.parse(input);
      const res = await axios.post('https://bajaj-finserv-health-e23e6e05a62b.herokuapp.com/', jsonInput);
      setResponse(res.data);
    } catch (err) {
      setError('Invalid JSON input');
    }
  };

  const handleChange = (event) => {
    setSelectedOptions(Array.from(event.target.selectedOptions, option => option.value));
  };

  const renderResponse = () => {
    if (!response) return null;
    const { numbers, alphabets, highest_lowercase_alphabet } = response;
    const result = {};
    
    if (selectedOptions.includes('Numbers')) result.numbers = numbers;
    if (selectedOptions.includes('Alphabets')) result.alphabets = alphabets;
    if (selectedOptions.includes('Highest lowercase alphabet')) result.highest_lowercase_alphabet = highest_lowercase_alphabet;
    
    return <pre>{JSON.stringify(result, null, 2)}</pre>;
  };

  return (
    <div className="App">
      <h1>Frontend Application</h1>
      <input
        type="text"
        value={input}
        onChange={(e) => setInput(e.target.value)}
        placeholder='Enter JSON data'
      />
      <button onClick={handleSubmit}>Submit</button>
      {error && <div style={{ color: 'red' }}>{error}</div>}
      <select multiple onChange={handleChange}>
        <option value="Alphabets">Alphabets</option>
        <option value="Numbers">Numbers</option>
        <option value="Highest lowercase alphabet">Highest lowercase alphabet</option>
      </select>
      {renderResponse()}
    </div>
  );
}

export default App;
