import React from 'react'; 
import { BrowserRouter as Router, Route, Routes } from 'react-router-dom'; 

import LandingPage from './pages/LandingPage';
import LoginPage from './pages/LoginPage';
import RegisterPage from './pages/RegisterPage';
import Dashboard from './pages/Dashboard';

import './App.css'
import CreatePost from './pages/CreatePost';



function App() {
  return (
    <Router>
      <Routes> {/* Use Routes instead of Switch */}
        <Route path="/" element={<LandingPage/>} /> {/* Use element prop instead of component */}
        <Route path="/signup" element={<RegisterPage/>} />
        <Route path="/signin" element={<LoginPage />} />
        <Route path="/dashboard" element={<Dashboard />} />
        <Route path="/createpost" element={<CreatePost/>} />
      </Routes>
    </Router>
  );
}

export default App;