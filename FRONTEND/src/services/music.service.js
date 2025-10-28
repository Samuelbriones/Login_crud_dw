import axios from 'axios';
import { authService } from './auth.service';

const getAuthHeader = () => ({
  headers: {
    'Authorization': `Bearer ${authService.getToken()}`
  }
});

export const musicService = {
  // MongoDB endpoints
  mongodb: {
    async getAll() {
      const response = await axios.get('http://localhost:8000/api/mongodb/music/', getAuthHeader());
      return response.data;
    },
    async create(music) {
      const response = await axios.post('http://localhost:8000/api/mongodb/music/', music, getAuthHeader());
      return response.data;
    },
    async update(id, music) {
      const response = await axios.put(`http://localhost:8000/api/mongodb/music/${id}`, music, getAuthHeader());
      return response.data;
    },
    async delete(id) {
      const response = await axios.delete(`http://localhost:8000/api/mongodb/music/${id}`, getAuthHeader());
      return response.data;
    }
  },

  // PostgreSQL endpoints
  postgresql: {
    async getAll() {
      const response = await axios.get('http://localhost:8000/api/postgresql/music/', getAuthHeader());
      return response.data;
    },
    async create(music) {
      const response = await axios.post('http://localhost:8000/api/postgresql/music/', music, getAuthHeader());
      return response.data;
    },
    async update(id, music) {
      const response = await axios.put(`http://localhost:8000/api/postgresql/music/${id}`, music, getAuthHeader());
      return response.data;
    },
    async delete(id) {
      const response = await axios.delete(`http://localhost:8000/api/postgresql/music/${id}`, getAuthHeader());
      return response.data;
    }
  }
};
