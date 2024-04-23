import { Navigate, Outlet } from "react-router-dom";
import { queryClient } from "../react-query-client";

const ProtectedRoutes = () => {
  const data = queryClient.getQueryData(["userData"]);

  return data ? <Outlet /> : <Navigate to="/auth" />;
};

export default ProtectedRoutes;
