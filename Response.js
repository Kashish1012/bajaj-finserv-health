import React from 'react';

const Response = ({ data }) => {
  return (
    <ul>
      {data.map((item) => (
        <li key={item}>{item}</li>
      ))}
    </ul>
  );
};

export default Response;