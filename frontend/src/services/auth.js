import { store } from "../state";
import axiosClient from "./axios-client";

class AuthService {
  async register(body) {
    return axiosClient.post("/auth/register", body);
  }

  async login(body) {
    const formData = new FormData();
    formData.append("username", body.email);
    formData.append("password", body.password);

    return axiosClient.post("/auth/jwt/login", formData, {
      headers: {
        "Content-Type": "multipart/form-data",
      },
    });
  }

  async me() {
    return axiosClient.get("/users/me").then((res) => {
      console.log(res.data);
      store.user.setUser(res.data);
      return res;
    });
  }
}

export default new AuthService();
