// src/App.js
import React from "react";
import { BrowserRouter as Router, Routes, Route } from "react-router-dom";
import HomePage from './components/Home'; // Adjust the path if needed
import UserPage from './components/User';
import Navigation from './components/Navigation'; // Import Navigation component
import './App.css';

function App() {
  return (
    <Router>
      <div className="App">
        <Navigation/> 
        <Routes>
          <Route path="/" element={<HomePage />} />
          <Route path="/user" element={<UserPage />} />
        </Routes>
      </div>
    </Router>
  );
}

export default App;
