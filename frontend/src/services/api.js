import axios from 'axios';

const API_URL = 'http://127.0.0.1:5000/api';

export const getMarks = async () => {
  try {
    const response = await axios.get('http://127.0.0.1:5000/api/marks');
    return response; // Return the full response object
  } catch (error) {
    console.error('Error fetching marks from backend:', error);
    throw error; // Ensure errors are propagated
  }
};

export const addMark = async (mark) => {
  try {
    const response = await axios.post(`${API_URL}/marks`, mark);
    return response.data;
  } catch (error) {
    console.error('Error adding mark:', error);
    throw error;
  }
};

export const deleteMark = async (assessmentName) => {
  try {
    const response = await axios.delete(`${API_URL}/marks/${assessmentName}`);
    return response.data;
  } catch (error) {
    console.error('Error deleting mark:', error);
    throw error;
  }
};
