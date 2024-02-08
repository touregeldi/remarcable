import React from 'react';
import { BrowserRouter as Router, Route, Routes } from 'react-router-dom';
import ProductList from './components/ProductList';

function App() {
  return (
    <Router>
      <div>
        <Routes>
          <Route path="/" element={<ProductList/>}/>
        </Routes>
      </div>
    </Router>
  );
}

export default App;
