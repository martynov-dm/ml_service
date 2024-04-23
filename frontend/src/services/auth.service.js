import axiosClient from "./client";

class AuthService {
  async signUp(body) {
    return axiosClient.post("/auth", body);
  }
}

export default new AuthService();
