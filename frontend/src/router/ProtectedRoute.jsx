import { Center, Spinner } from "@chakra-ui/react";
import { Navigate } from "react-router-dom";
import useAuth from "../hooks/useAuth";

// eslint-disable-next-line react/prop-types
const ProtectedRoute = ({ children }) => {
  const { user, isLoading } = useAuth();
  console.log(user);

  if (isLoading) {
    return (
      <Center h="100vh">
        <Spinner size="xl" />
      </Center>
    );
  }

  return user ? children : <Navigate to="/auth" />;
};

export default ProtectedRoute;
