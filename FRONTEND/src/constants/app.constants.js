// API Configuration
export const API_BASE_URL = 'http://localhost:8000';

export const API_ENDPOINTS = {
  AUTH: {
    REGISTER: '/api/users/register',
    LOGIN: '/api/users/login'
  },
  MUSIC: {
    MONGODB: '/api/mongodb/music',
    POSTGRESQL: '/api/postgresql/music'
  }
};

// Database Types
export const DB_TYPES = {
  MONGODB: 'mongodb',
  POSTGRESQL: 'postgresql'
};

// Local Storage Keys
export const STORAGE_KEYS = {
  TOKEN: 'token'
};

// Form Initial States
export const INITIAL_MUSIC_FORM = {
  title: '',
  artist: '',
  genre: ''
};

export const INITIAL_LOGIN_FORM = {
  email: '',
  password: ''
};

export const INITIAL_REGISTER_FORM = {
  name: '',
  email: '',
  password: ''
};

// Validation Rules
export const VALIDATION = {
  PASSWORD_MIN_LENGTH: 8,
  EMAIL_REGEX: /^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$/
};

// Messages
export const MESSAGES = {
  SUCCESS: {
    REGISTER: 'Registro exitoso! Ahora puedes iniciar sesión',
    CREATE: 'Canción creada exitosamente',
    UPDATE: 'Canción actualizada exitosamente',
    DELETE: 'Canción eliminada exitosamente'
  },
  ERROR: {
    LOAD: 'Error al cargar música',
    CREATE: 'Error al crear música',
    UPDATE: 'Error al actualizar música',
    DELETE: 'Error al eliminar música',
    LOGIN: 'Error al iniciar sesión',
    REGISTER: 'Error al registrar usuario',
    GENERIC: 'Ha ocurrido un error'
  }
};
