import { useQueryClient } from "@tanstack/react-query";
import { useEffect } from "react";
import { useNavigate } from "react-router-dom";

const RedirectFromRoot = () => {
  const navigate = useNavigate();
  const queryClient = useQueryClient();
  const queryCache = queryClient.getQueryCache();
  const userData = queryCache.find({ queryKey: ["userData"] });

  useEffect(() => {
    if (userData) {
      navigate("/generate");
    } else {
      navigate("/auth");
    }
  }, [userData, navigate]);

  return null;
};

export default RedirectFromRoot;
