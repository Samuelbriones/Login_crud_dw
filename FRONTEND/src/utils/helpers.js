/**
 * Obtiene el ID de una canción según el tipo de base de datos
 * @param {Object} music - Objeto de musica
 * @param {string} dbType - Tipo de base de datos ('mongodb' o 'postgresql')
 * @returns {string|number} ID de la cancion
 */
export const getMusicId = (music, dbType) => {
  return dbType === 'mongodb' ? music._id : music.id;
};

/**
 * Formatea un error de respuesta de API
 * @param {Error} error - Error capturado
 * @param {string} defaultMessage - Mensaje por defecto
 * @returns {string} Mensaje de error formateado
 */
export const formatError = (error, defaultMessage = 'Ha ocurrido un error') => {
  return error.response?.data?.detail || error.message || defaultMessage;
};

/**
 * Valida un email
 * @param {string} email - Email a validar
 * @returns {boolean} True si es válido
 */
export const isValidEmail = (email) => {
  const regex = /^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$/;
  return regex.test(email);
};

/**
 * Valida una contraseña
 * @param {string} password - Contraseña a validar
 * @param {number} minLength - Longitud mínima
 * @returns {boolean} True si es válida
 */
export const isValidPassword = (password, minLength = 8) => {
  return password.length >= minLength;
};

/**
 * Limpia un formulario (resetea valores)
 * @param {Object} initialState - Estado inicial del formulario
 * @returns {Object} Objeto con valores vacíos
 */
export const resetForm = (initialState) => {
  return Object.keys(initialState).reduce((acc, key) => {
    acc[key] = '';
    return acc;
  }, {});
};

/**
 * Debounce function para limitar llamadas
 * @param {Function} func - Función a ejecutar
 * @param {number} wait - Tiempo de espera en ms
 * @returns {Function} Función debounced
 */
export const debounce = (func, wait) => {
  let timeout;
  return function executedFunction(...args) {
    const later = () => {
      clearTimeout(timeout);
      func(...args);
    };
    clearTimeout(timeout);
    timeout = setTimeout(later, wait);
  };
};
