import '../styles/Dashboard.css';

function MusicCard({ music, onEdit, onDelete }) {
  return (
    <div className="music-card">
      <h3>{music.title}</h3>
      <p><strong>Artista:</strong> {music.artist}</p>
      <p><strong>Género:</strong> {music.genre}</p>
      <div className="music-actions">
        <button onClick={() => onEdit(music)} className="btn-edit">
          Editar
        </button>
        <button onClick={() => onDelete(music)} className="btn-delete">
          Eliminar
        </button>
      </div>
    </div>
  );
}

export default MusicCard;
