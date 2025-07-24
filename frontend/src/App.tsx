import React from 'react';
import { BrowserRouter, Routes, Route } from 'react-router-dom';
import PatientRegistration from './pages/PatientRegistration';
import PatientDashboard from './pages/PatientDashboard';

interface AppProps {}

const App: React.FC<AppProps> = () => {
  return (
    <BrowserRouter>
      <Routes>
        <Route path="/register" element={<PatientRegistration />} />
        <Route path="/dashboard" element={<PatientDashboard />} />
        {/* Add more routes here */}
      </Routes>
    </BrowserRouter>
  );
};

export default App;