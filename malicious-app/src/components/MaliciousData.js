import React, { useState } from 'react';
import axios from 'axios';
import TableComponent from './TableComponent';

const MaliciousData = () => {
  const [domain, setDomain] = useState('');
  const [data, setData] = useState(null);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState(null);

  const handleInputChange = (event) => {
    setDomain(event.target.value);
  };

  const handleSearch = () => {
    setLoading(true);
    setError(null);

    console.log(`Fetching data for domain: ${domain}`);

    axios.get(`http://127.0.0.1:5000/check_domain/${domain}`)
      .then(response => {
        console.log("Data received from API:", response.data);
        setData(response.data);
        setLoading(false);
      })
      .catch(error => {
        console.error("Error fetching data:", error);
        setError(error);
        setLoading(false);
      });
  };

  return (
    <div>
      <h2>Verificar Dominio</h2>
      <input
        type="text"
        value={domain}
        onChange={handleInputChange}
        placeholder="Ingresa el dominio"
      />
      <button onClick={handleSearch}>Buscar</button>

      {loading && <p>Loading...</p>}
      {error && <p>Error loading data</p>}

      {data && <TableComponent data={data} />}
    </div>
  );
};

export default MaliciousData;
