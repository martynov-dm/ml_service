import { useQuery } from "@tanstack/react-query";
import { useSnapshot } from "valtio";
import authService from "../services/auth";
import { store } from "../state";

const useAuth = () => {
  const { user } = useSnapshot(store);

  const { isLoading, isError, refetch, data } = useQuery({
    queryKey: ["userData"],
    queryFn: authService.me,
    retry: 0,
    staleTime: 1000 * 60 * 60 * 4, // 4 hours
    meta: {
      persist: true,
    },
  });

  if (!user.isLoggedIn && !isError && data?.data) {
    user.setUser(data.data);
  }

  return {
    user,
    isLoading,
    isError,
    refetch,
  };
};

export default useAuth;
