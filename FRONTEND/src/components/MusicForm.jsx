import '../styles/Dashboard.css';

function MusicForm({ formData, onSubmit, onChange, onCancel, isEditing }) {
  return (
    <div className="form-section">
      <h2>{isEditing ? 'Editar Canción' : 'Agregar Canción'}</h2>
      <form onSubmit={onSubmit}>
        <div className="form-group">
          <label>Título:</label>
          <input
            type="text"
            name="title"
            value={formData.title}
            onChange={onChange}
            placeholder="Nombre de la canción"
            required
          />
        </div>
        <div className="form-group">
          <label>Artista:</label>
          <input
            type="text"
            name="artist"
            value={formData.artist}
            onChange={onChange}
            placeholder="Nombre del artista"
            required
          />
        </div>
        <div className="form-group">
          <label>Género:</label>
          <input
            type="text"
            name="genre"
            value={formData.genre}
            onChange={onChange}
            placeholder="Rock, Pop, Jazz, etc."
            required
          />
        </div>
        <div className="form-buttons">
          <button type="submit" className="btn-primary">
            {isEditing ? 'Actualizar' : 'Agregar'}
          </button>
          {isEditing && (
            <button type="button" onClick={onCancel} className="btn-secondary">
              Cancelar
            </button>
          )}
        </div>
      </form>
    </div>
  );
}

export default MusicForm;
