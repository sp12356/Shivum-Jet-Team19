// src/components/UserPage.js
import React from 'react';
import './UserPage.css'; // Import CSS file
import MultiStepModal from './InfoModalUser'; // Import MultiStepModal component

function UserPage() {
  return (
    <div className="split-screen">
      <div className="left-panel">
        <MultiStepModal /> {/* Add MultiStepModal here */}
        <textarea placeholder="Enter code here..." className="code-input" />
      </div>
      <div className="right-panel">
        <div className="output">Output Code</div>
      </div>
    </div>
  );
}

export default UserPage;
