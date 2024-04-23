import axiosClient from "./client";

class AuthService {
  async register(body) {
    return axiosClient.post("/auth/register", body);
  }
}

export default new AuthService();
