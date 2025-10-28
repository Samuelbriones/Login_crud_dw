import '../styles/Dashboard.css';

function ErrorMessage({ message, onClose }) {
  if (!message) return null;

  return (
    <div className="error-message">
      {message}
      {onClose && (
        <button className="error-close" onClick={onClose}>
          ×
        </button>
      )}
    </div>
  );
}

export default ErrorMessage;
