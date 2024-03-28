import axios from 'axios';

// ログイン用のaxiosインスタンス
const loginClient = axios.create({
  baseURL: 'http://0.0.0.0:8000/', // mac
  // baseURL: "http://127.0.0.1:8000/", // windows
  withCredentials: false,
  headers: {
    Accept: 'application/json',
    'Content-Type': 'application/json',
  },
});

// サインアップ用のaxiosインスタンス
const signupClient = axios.create({
  baseURL: 'http://0.0.0.0:8000/api', // mac
  // baseURL: "http://127.0.0.1:8000/api", //windows
  headers: {
    'Content-Type': 'application/json',
  },
});

// API用のaxiosインスタンス
const apiClient = axios.create({
  baseURL: 'http://0.0.0.0:8000/api', // mac
  // baseURL: "http://127.0.0.1:8000/api", //windows
  headers: {
    'Content-Type': 'application/json',
  },
});

// リクエストを送信する前に実行されるインターセプターを追加
apiClient.interceptors.request.use(
  (config) => {
    const token = window.localStorage.getItem('token');
    if (token) {
      config.headers.Authorization = `Token ${token}`; // トークンを動的に設定
    }
    return config;
  },
  (error) => {
    return Promise.reject(error);
  },
);

type LoginInfo = {
  username: string;
  password: string;
};

type SignupInfo = {
  username: string;
  email: string;
  password: string;
};

type ProfileInfo = {
  id: string;
  username: string;
  email: string;
};

export default {
  submitLogin(logininfo: LoginInfo) {
    return loginClient.post('api-token-auth/', logininfo);
  },
  submitSignup(signupinfo: SignupInfo) {
    return signupClient.post('member/', signupinfo);
  },
  updateProfile(id: string, profileinfo: ProfileInfo) {
    return apiClient.patch(`member/${id}/`, profileinfo);
  },
  getComic(meta: string) {
    return apiClient.get(`comic/${meta}`);
  },
  getReviewMaster(id: string) {
    return apiClient.get(`review/master/?member_id=${id}`);
  },
};
