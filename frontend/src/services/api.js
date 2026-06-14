import axios from "axios";

const API_URL = "http://127.0.0.1:8000";

export const uploadPDF = async (file) => {
  const formData = new FormData();
  formData.append("file", file);

  return axios.post(
    `${API_URL}/upload-pdf`,
    formData
  );
};

export const uploadPPT = async (file) => {
  const formData = new FormData();
  formData.append("file", file);

  return axios.post(
    `${API_URL}/upload-ppt`,
    formData
  );
};

export const addWebsite = async (url) => {
  return axios.post(
    `${API_URL}/add-website`,
    { url }
  );
};

export const addYoutube = async (url) => {
  return axios.post(
    `${API_URL}/add-youtube`,
    { url }
  );
};

export const askQuestion = async (question) => {
  return axios.post(
    `${API_URL}/ask`,
    { question }
  );
};