import AuthPage from 'pages/auth';
import GeneratePage from 'pages/generate';
import ProfilePage from 'pages/profile';
import { BrowserRouter, Route, Routes } from 'react-router-dom';
import ProtectedRoutes from './ProtectedRoutes';

const Router = () => {
  return (
    <BrowserRouter>
      <Routes>
        <Route path="/auth" element={<AuthPage />} />
        <Route element={<ProtectedRoutes />}>
          <Route path="/generate" element={<GeneratePage />} />
          <Route path="/profile" element={<ProfilePage />} />
        </Route>
      </Routes>
    </BrowserRouter>
  );
};

export default Router;
