//maneja la logica de la musica o crud
import { useState, useEffect } from 'react';
import { musicService } from '../services/music.service';

export const useMusicManager = (activeDb) => {
  const [musics, setMusics] = useState([]);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState('');

  const getMusicService = () => {
    return activeDb === 'mongodb' ? musicService.mongodb : musicService.postgresql;
  };

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

  const getMusicId = (music) => {
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
