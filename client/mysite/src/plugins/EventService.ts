import axios from "axios";

// ログイン用のaxiosインスタンス
const loginClient = axios.create({
  // baseURL: "http://0.0.0.0:8000/", // mac
  baseURL: "http://127.0.0.1:8000/", // windows
  withCredentials: false,
  headers: {
    Accept: "application/json",
    "Content-Type": "application/json",
  },
});

// API用のaxiosインスタンス
const apiClient = axios.create({
  baseURL: "http://0.0.0.0:8000/api", // mac
  // baseURL: "http://127.0.0.1:8000/api", //windows
  headers: {
    "Content-Type": "application/json",
  },
});

// リクエストを送信する前に実行されるインターセプターを追加
apiClient.interceptors.request.use((config) => {
  const token = window.localStorage.getItem("token");
  if (token) {
    config.headers.Authorization = `Token ${token}`; // トークンを動的に設定
  }
  return config;
}, (error) => {
  return Promise.reject(error);
});

interface LoginInfo {
  username: string;
  password: string;
}

export default {
  submitLogin(logininfo: LoginInfo) {
    return loginClient.post("api-token-auth/", logininfo);
  },
}