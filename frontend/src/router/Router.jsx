import { BrowserRouter, Navigate, Route, Routes } from "react-router-dom";
import AuthPage from "../pages/auth/index";
import GeneratePage from "../pages/generate/index";
import ProfilePage from "../pages/profile/index";
import Authenticator from "./Authenticator";

const Router = () => {
  return (
    <BrowserRouter>
      <Routes>
        <Route element={<Authenticator />}>
          {/* <Route path="/" element={<RedirectFromRoot />} /> */}
          <Route path="/generate" element={<GeneratePage />} />
          <Route path="/profile" element={<ProfilePage />} />
          <Route path="/auth" element={<AuthPage />} />
          <Route path="/" element={<Navigate to="/generate" />} />
          <Route path="/*" element={<Navigate to="/auth" />} />
        </Route>
      </Routes>
    </BrowserRouter>
  );
};

export default Router;
