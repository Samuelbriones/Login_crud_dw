import '../styles/Dashboard.css';

function DashboardHeader({ onLogout }) {
  return (
    <header className="dashboard-header">
      <h1>Gestión de Música</h1>
      <button onClick={onLogout} className="btn-logout">
        Cerrar Sesión
      </button>
    </header>
  );
}

export default DashboardHeader;
