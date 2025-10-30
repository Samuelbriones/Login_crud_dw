import '../styles/Dashboard.css';

function DatabaseSelector({ activeDb, onSelectDb }) {
  return (
    <div className="db-selector">
      <button 
        className={activeDb === 'mongodb' ? 'active' : ''}
        onClick={() => onSelectDb('mongodb')}
      >
        MongoDB
      </button>
      
    </div>
  );
}

export default DatabaseSelector;
