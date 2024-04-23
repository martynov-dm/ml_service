import { useEffect } from "react";
import { BrowserRouter, Navigate, Route, Routes } from "react-router-dom";
import { useSnapshot } from "valtio";
import AuthPage from "../pages/auth/index";
import GeneratePage from "../pages/generate/index";
import ProfilePage from "../pages/profile/index";
import { store } from "../state";
import ProtectedRoutes from "./ProtectedRoutes";

const Router = () => {
  const { isLoggedIn, checkAuth } = useSnapshot(store.user);

  useEffect(() => {
    checkAuth();

    console.log(isLoggedIn);
  }, [checkAuth, isLoggedIn]);

  return (
    <BrowserRouter>
      <Routes>
        <Route
          path="/"
          element={
            isLoggedIn ? <Navigate to="/generate" /> : <Navigate to="/auth" />
          }
        />
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
