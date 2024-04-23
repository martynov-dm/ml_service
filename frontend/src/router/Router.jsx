import { Center, Spinner } from "@chakra-ui/react";
import { useQuery } from "@tanstack/react-query";
import { BrowserRouter, Route, Routes } from "react-router-dom";
import AuthPage from "../pages/auth/index";
import GeneratePage from "../pages/generate/index";
import ProfilePage from "../pages/profile/index";
import authService from "../services/auth";
import ProtectedRoutes from "./ProtectedRoutes";
import RedirectFromRoot from "./RedirectFromRoot";

const Router = () => {
  const { isLoading } = useQuery({
    queryKey: ["userData"],
    queryFn: authService.me,
    retry: 0,
    staleTime: 1000 * 60 * 60 * 4, // 4 hours
    meta: {
      persist: true,
    },
  });

  if (isLoading) {
    return (
      <Center h="100vh">
        <Spinner size="xl" />
      </Center>
    );
  }

  return (
    <BrowserRouter>
      <Routes>
        <Route path="/" element={<RedirectFromRoot />} />
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
