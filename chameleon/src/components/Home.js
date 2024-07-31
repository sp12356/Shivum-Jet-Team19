import React from 'react';

function HomePage() {
  return (
    <div className="App">
      <header className="App-header">
        <h1>Chameleon</h1>
        <form>
          <h5>Username</h5>
          <textarea name="User" cols="30" rows="2"></textarea>
        </form>
        <form>
          <h5>Password</h5>
          <textarea name="Password" cols="30" rows="2"></textarea>
        </form>
      </header>
    </div>
  );
}

export default HomePage;
