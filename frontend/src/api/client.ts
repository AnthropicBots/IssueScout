import axios, { AxiosError } from "axios";

const API_BASE_URL =
  import.meta.env.VITE_API_URL ?? "http://127.0.0.1:8000/api/v1";

export const api = axios.create({
  baseURL: API_BASE_URL,
  headers: {
    "Content-Type": "application/json",
  },
});

api.interceptors.response.use(
  (response) => response,
  (error: AxiosError<{ detail?: string }>) => {
    const detail = error.response?.data?.detail;

    if (detail) {
      error.message = detail;
    }

    return Promise.reject(error);
  }
);
