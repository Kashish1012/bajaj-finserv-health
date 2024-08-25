import React from 'react';

const TextInput = ({ value, onChange }) => {
  const handleInputChange = (event) => {
    try {
      JSON.parse(event.target.value);
      onChange(event);
    } catch (error) {
      console.error('Invalid JSON input');
    }
  };

  return (
    <input
      type="text"
      value={value}
      onChange={handleInputChange}
      placeholder="Enter JSON input"
    />
  );
};

export default TextInput;