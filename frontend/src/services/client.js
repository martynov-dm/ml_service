import getApiUrl from "@/utils/getApiUrl";
import axios from "axios";
import.meta.env.PROD;

const axiosClient = axios.create({
  baseURL: getApiUrl(),
  headers: {
    "Content-type": "application/json",
  },
});

export default axiosClient