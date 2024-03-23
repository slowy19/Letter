import axios from 'axios';

axios.defaults.baseURL = 'http://localhost:80';

const axiosInstance = axios.create({
    baseURL: "http://127.0.0.1:80"
});

export default axiosInstance;
