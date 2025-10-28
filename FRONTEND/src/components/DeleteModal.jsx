import '../styles/Modal.css';

function DeleteModal({ music, onClose, onConfirm, isLoading }) {
  if (!music) return null;

  return (
    <div className="modal-overlay" onClick={onClose}>
      <div className="modal-content modal-delete" onClick={(e) => e.stopPropagation()}>
        <div className="modal-header">
          <h2>Eliminar Canción</h2>
          <button className="close-button" onClick={onClose}>×</button>
        </div>
        
        <div className="modal-body">
          <div className="delete-warning">
            <div className="warning-icon"> </div>
            <p className="warning-text">
              ¿Estás seguro de que deseas eliminar esta canción?
            </p>
          </div>

          <div className="music-info-card">
            <div className="info-row">
              <span className="info-label"> Título:</span>
              <span className="info-value">{music.title}</span>
            </div>
            <div className="info-row">
              <span className="info-label"> Artista:</span>
              <span className="info-value">{music.artist}</span>
            </div>
            <div className="info-row">
              <span className="info-label"> Género:</span>
              <span className="info-value">{music.genre}</span>
            </div>
          </div>

          <p className="delete-note">
            Esta acción no se puede deshacer.
          </p>
        </div>

        <div className="modal-footer">
          <button 
            type="button" 
            className="btn-cancel" 
            onClick={onClose}
            disabled={isLoading}
          >
            No, Cancelar
          </button>
          <button 
            type="button" 
            className="btn-delete-confirm"
            onClick={onConfirm}
            disabled={isLoading}
          >
            {isLoading ? ' Eliminando...' : ' Sí, Eliminar'}
          </button>
        </div>
      </div>
    </div>
  );
}

export default DeleteModal;
