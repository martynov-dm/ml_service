import axiosClient from "./axios-client";

class GenerateService {
  async generate(body) {
    return axiosClient.post("/generate", body);
  }
}

export default new GenerateService();
