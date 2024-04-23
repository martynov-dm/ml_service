import { useQuery } from "@tanstack/react-query";
import { useEffect } from "react";
import { BrowserRouter, Navigate, Route, Routes } from "react-router-dom";
import AuthPage from "../pages/auth/index";
import GeneratePage from "../pages/generate/index";
import ProfilePage from "../pages/profile/index";
import authService from "../services/auth";
import ProtectedRoutes from "./ProtectedRoutes";

const Router = () => {
  const {
    data: userData,
    isLoading,
    isError,
  } = useQuery({
    queryKey: ["userData"],
    queryFn: authService.me,
    retry: 2,
    onSuccess: () => {},
  });

  useEffect(() => {
    if (isError) {
      // Redirect to auth page if there's an error fetching user data
      window.location.href = "/auth";
    }
  }, [isError]);

  if (isLoading) {
    // Show loading state while fetching user data
    return <div>Loading...</div>;
  }

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
