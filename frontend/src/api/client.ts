import axios, { AxiosError } from "axios";

import { API_BASE_URL } from "../config/constants";

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
