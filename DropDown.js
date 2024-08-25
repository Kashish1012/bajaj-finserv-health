import React from 'react';

const Dropdown = ({ options, onChange }) => {
  const handleOptionChange = (event) => {
    onChange(event.target.value);
  };

  return (
    <select multiple onChange={handleOptionChange}>
      {options.map((option) => (
        <option key={option} value={option}>
          {option}
        </option>
      ))}
    </select>
  );
};

export default Dropdown;