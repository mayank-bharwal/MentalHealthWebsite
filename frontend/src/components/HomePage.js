import React from 'react';
import { Link } from 'react-router-dom';

const HomePage = () => {
  return (
    <div>
      <h1>Welcome to the Mental Wellness Website</h1>
      <p>This is a place where you can explore tools for mental well-being.</p>
      <Link to="/login">Login</Link> | <Link to="/register">Register</Link>
      {/* Other links or information can be added here */}
    </div>
  );
};

export default HomePage;
