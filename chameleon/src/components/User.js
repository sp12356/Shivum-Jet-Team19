import React, { useState, useEffect } from "react";
import './UserPage.css'; // Import CSS file
import MultiStepModal from './InfoModalUser'; // Import MultiStepModal component

function UserPage() {
  const [data, setData] = useState({
    name: "",
    age: 0,
    date: "",
    programming: "",
  });
  const [inputCode, setInputCode] = useState('');
  const [output, setOutput] = useState('');

  useEffect(() => {
    // Using fetch to fetch the API from the Flask server
    fetch("http://127.0.0.1:5000/data")
      .then((res) => {
        if (!res.ok) {
          throw new Error(`HTTP error! status: ${res.status}`);
        }
        return res.json();
      })
      .then((data) => {
        // Setting the data from API
        setData({
          name: data.Name,
          age: data.Age,
          date: data.Date,
          programming: data.programming,
        });
      })
      .catch((error) => {
        console.error('Error:', error);
      });
  }, []);

  const handleOptimize = async () => {
    try {
      const response = await fetch('http://127.0.0.1:5000/run-script', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({
          original_html: inputCode,
          improved_html: '', // Add improved HTML if you have it
        }),
      });

      if (!response.ok) {
        throw new Error(`HTTP error! status: ${response.status}`);
      }

      const data = await response.json();
      setOutput(JSON.stringify(data, null, 2));
    } catch (error) {
      console.error('Error:', error);
      setOutput('An error occurred while processing your request.');
    }
  };

  return (
    <div className="split-screen">
      <div className="left-panel">
        <MultiStepModal /> {/* Add MultiStepModal here */}
        <textarea
          placeholder="Enter code here..."
          className="code-input"
          value={inputCode}
          onChange={(e) => setInputCode(e.target.value)}
        />
        <button onClick={handleOptimize}>Optimize</button>
      </div>
      <div className="right-panel">
        <textarea
          className="code-input"
          value={output}
          readOnly
        />
        <p>Name: {data.name}</p>
      </div>
    </div>
  );
}

export default UserPage;
