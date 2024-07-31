import React from 'react';
import './UserPage.css'; // Make sure to create and import the CSS file

function UserPage() {
  return (
    <div className="split-screen">
      <div className="left-panel">
        <div className = "input">Input Code</div>
        <textarea placeholder="Enter code here..." className="code-input" />
      </div>
      <div className="right-panel">
        <div className = "output">Output Code</div>

      </div>
    </div>
  );
}

export default UserPage;
