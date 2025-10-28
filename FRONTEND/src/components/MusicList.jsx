import MusicCard from './MusicCard';
import '../styles/Dashboard.css';

function MusicList({ musics, loading, activeDb, onEdit, onDelete }) {
  return (
    <div className="music-list-section">
      <h2>Lista de Canciones ({activeDb === 'mongodb' ? 'MongoDB' : 'PostgreSQL'})</h2>
      
      {loading ? (
        <div className="loading-state">
          <p>Cargando...</p>
        </div>
      ) : musics.length === 0 ? (
        <div className="empty-state">
          <p>No hay canciones registradas</p>
        </div>
      ) : (
        <div className="music-grid">
          {musics.map((music) => (
            <MusicCard
              key={music._id || music.id}
              music={music}
              onEdit={onEdit}
              onDelete={onDelete}
            />
          ))}
        </div>
      )}
    </div>
  );
}

export default MusicList;
