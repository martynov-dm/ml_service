import { BrowserRouter, Navigate, Route, Routes } from "react-router-dom";
import AuthPage from "../pages/auth/index";
import GeneratePage from "../pages/generate/index";
import NotFound from "../pages/not_found";
import ProfilePage from "../pages/profile/index";
import ProtectedRoute from "./ProtectedRoute";

const Router = () => {
  return (
    <BrowserRouter>
      <Routes>
        <Route path="/" element={<Navigate to="/generate" />} />
        <Route
          path="/generate"
          element={
            <ProtectedRoute>
              <GeneratePage />
            </ProtectedRoute>
          }
        />
        <Route path="/profile" element={<ProfilePage />} />
        <Route path="/auth" element={<AuthPage />} />
        <Route path="/*" element={<NotFound />} />
      </Routes>
    </BrowserRouter>
  );
};

export default Router;
