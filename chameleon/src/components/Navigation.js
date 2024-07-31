// src/components/Navigation.js
import './Navigation.css'; // Import the new CSS file
import React from 'react';
import { Link } from 'react-router-dom';

function Navigation() {
  return (
    <nav>
      <ul>
        <li><Link to="/">Home</Link></li>
        <li><Link to="/user">User</Link></li>
      </ul>
    </nav>
  );
}

export default Navigation;
