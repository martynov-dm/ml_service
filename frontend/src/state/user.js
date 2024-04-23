import Cookies from "js-cookie";
import { proxy } from "valtio";

export const userState = proxy({
  isLoggedIn: false,
  username: "",
  email: "",

  checkAuth: () => {
    const token = Cookies.get("image_prediction_app");

    console.log(token);

    userState.isLoggedIn = !!token;
  },
});
