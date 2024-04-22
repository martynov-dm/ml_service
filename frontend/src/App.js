import { ChakraProvider, theme } from '@chakra-ui/react';
import React from 'react';
import {
  BrowserRouter,
  Route,
  Routes
} from "react-router-dom";
import AuthPage from './pages/auth/index';
import GeneratePage from './pages/generate/index';
import ProfilePage from './pages/profile/index';

function App() {
  return (
    <ChakraProvider theme={theme}>
      <BrowserRouter>
        <Routes>
          <Route path="/auth" element={<AuthPage/>} />
          <Route path="/generate" element={<GeneratePage/>} />
          <Route path="/profile" element={<ProfilePage/>} />
        </Routes>
      </BrowserRouter>
    </ChakraProvider>
  );
}

export default App;