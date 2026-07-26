import axios from "axios";

const api = axios.create({
    baseURL: "https://mini-content-engine-j7wd.onrender.com",
});

export default api;