import getApiUrl from "@/utils/getApiUrl";
import axios from "axios";
import.meta.env.PROD;

const DEV_API_URL = "";
const PROD_API_URL = "";

const client = axios.create({
  baseURL: getApiUrl(),
});

export const request = async (options) => {
  let token;
  const state = store.getState();
  const userState = state?.user?.currentUser;
  if (userState === null) {
    token = "";
  } else {
    const { accessToken } = userState;
    token = accessToken;
  }
  // Set the authorization header
  token !== "" &&
    (client.defaults.headers.common.Authorization = `Bearer ${token}`);

  const onSuccess = (response) => {
    return response?.data?.data;
  };

  const onError = (error) => {
    return Promise.reject(error.response?.data);
  };

  return client(options).then(onSuccess).catch(onError);
};
