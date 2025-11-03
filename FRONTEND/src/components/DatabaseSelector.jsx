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
      
      <button 
        className={activeDb === 'postgresql' ? 'active' : ''}
        onClick={() => onSelectDb('postgresql')}
      >
        PostgreSQL
      </button>

      <button 
        className={activeDb === 'graphql' ? 'active' : ''}
        onClick={() => onSelectDb('graphql')}
      >
        Graphql
      </button>
      
    </div>
  );
}

export default DatabaseSelector;
