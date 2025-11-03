import { useState, useEffect } from 'react';
import { musicService } from '../services/music.service';
import { musicGraphQLService } from '../services/music.graphql.service';

// Hook unificado para MongoDB, PostgreSQL y GraphQL
export const useMusicManager = (activeDb) => {
  const [musics, setMusics] = useState([]);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState('');

  // Selecciona el servicio según la base activa
  const getMusicService = () => {
    if (activeDb === 'graphql') return musicGraphQLService;
    if (activeDb === 'mongodb') return musicService.mongodb;
    return musicService.postgresql;
  };

  // Cargar todas las canciones
  const loadMusics = async () => {
    setLoading(true);
    setError('');
    try {
      const data = await getMusicService().getAll();
      setMusics(data);
    } catch (err) {
      setError('Error al cargar música');
      console.error(err);
    } finally {
      setLoading(false);
    }
  };

  // Crear nueva canción
  const createMusic = async (musicData) => {
    setError('');
    try {
      await getMusicService().create(musicData);
      await loadMusics();
      return { success: true };
    } catch (err) {
      const errorMsg = err.response?.data?.detail || 'Error al crear música';
      setError(errorMsg);
      return { success: false, error: errorMsg };
    }
  };

  // Actualizar canción existente
  const updateMusic = async (id, musicData) => {
    setError('');
    try {
      await getMusicService().update(id, musicData);
      await loadMusics();
      return { success: true };
    } catch (err) {
      const errorMsg = err.response?.data?.detail || 'Error al actualizar música';
      setError(errorMsg);
      return { success: false, error: errorMsg };
    }
  };

  // Eliminar canción
  const deleteMusic = async (id) => {
    setError('');
    try {
      await getMusicService().delete(id);
      await loadMusics();
      return { success: true };
    } catch (err) {
      const errorMsg = err.response?.data?.detail || 'Error al eliminar música';
      setError(errorMsg);
      return { success: false, error: errorMsg };
    }
  };

  // Obtener ID según tipo de fuente
  const getMusicId = (music) => {
    if (activeDb === 'graphql') return music.id;
    return activeDb === 'mongodb' ? music._id : music.id;
  };

  useEffect(() => {
    loadMusics();
  }, [activeDb]);

  return {
    musics,
    loading,
    error,
    setError,
    loadMusics,
    createMusic,
    updateMusic,
    deleteMusic,
    getMusicId
  };
};
