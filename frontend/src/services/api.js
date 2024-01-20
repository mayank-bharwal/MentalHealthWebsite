import axios from 'axios';

const API = axios.create({ baseURL: 'http://localhost:5000' });

export const loginUser = (userData) => API.post('/login', userData);
export const registerUser = (userData) => API.post('/register', userData);
export const postJournalEntry = (entryData) => API.post('/journal', entryData, { headers: {/* Authorization header */}});
export const getJournalEntries = () => API.get('/journal', { headers: {/* Authorization header */}});
export const sendMessageToChatbot = (message) => API.post('/chatbot', { message });

export default API;
