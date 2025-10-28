import { useState } from 'react';
import { useNavigate } from 'react-router-dom';
import { authService } from '../services/auth.service';
import { useMusicManager } from '../hooks/useMusicManager';
import DashboardHeader from '../components/DashboardHeader';
import DatabaseSelector from '../components/DatabaseSelector';
import ErrorMessage from '../components/ErrorMessage';
import MusicForm from '../components/MusicForm';
import MusicList from '../components/MusicList';
import DeleteModal from '../components/DeleteModal';
import '../styles/Dashboard.css';

function Dashboard() {
  const [activeDb, setActiveDb] = useState('mongodb');
  const [formData, setFormData] = useState({ title: '', artist: '', genre: '' });
  const [editingId, setEditingId] = useState(null);
  const [musicToDelete, setMusicToDelete] = useState(null);
  const [isDeleting, setIsDeleting] = useState(false);
  const navigate = useNavigate();
  
  const { musics, loading, error, setError, createMusic, updateMusic, deleteMusic, getMusicId } = useMusicManager(activeDb);

  const handleSubmit = async (e) => {
    e.preventDefault();
    
    if (editingId) {
      await updateMusic(editingId, formData);
    } else {
      await createMusic(formData);
    }
    
    setFormData({ title: '', artist: '', genre: '' });
    setEditingId(null);
  };

  const handleChange = (e) => {
    setFormData({
      ...formData,
      [e.target.name]: e.target.value
    });
  };

  const handleEdit = (music) => {
    setFormData({
      title: music.title,
      artist: music.artist,
      genre: music.genre
    });
    setEditingId(getMusicId(music));
  };

  const handleDeleteClick = (music) => {
    setMusicToDelete(music);
  };

  const handleConfirmDelete = async () => {
    if (!musicToDelete) return;
    
    setIsDeleting(true);
    const id = getMusicId(musicToDelete);
    await deleteMusic(id);
    setIsDeleting(false);
    setMusicToDelete(null);
  };

  const handleLogout = () => {
    authService.logout();
    navigate('/login');
  };

  const handleCancel = () => {
    setFormData({ title: '', artist: '', genre: '' });
    setEditingId(null);
  };

  return (
    <div className="dashboard-container">
      <DashboardHeader onLogout={handleLogout} />
      
      <DatabaseSelector 
        activeDb={activeDb} 
        onSelectDb={setActiveDb} 
      />

      <ErrorMessage 
        message={error} 
        onClose={() => setError('')} 
      />

      <div className="dashboard-content">
        <MusicForm
          formData={formData}
          onSubmit={handleSubmit}
          onChange={handleChange}
          onCancel={handleCancel}
          isEditing={!!editingId}
        />

        <MusicList
          musics={musics}
          loading={loading}
          activeDb={activeDb}
          onEdit={handleEdit}
          onDelete={handleDeleteClick}
        />
      </div>

      <DeleteModal
        music={musicToDelete}
        onClose={() => setMusicToDelete(null)}
        onConfirm={handleConfirmDelete}
        isLoading={isDeleting}
      />
    </div>
  );
}

export default Dashboard;
