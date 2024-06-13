import React from 'react';

const TableComponent = ({ data }) => {
  if (!data) {
    return <div>No hay datos disponibles.</div>;
  }

  const { es_maliciosa, malicioso, no_malicioso, voto } = data;

  return (
    <div>
      <h2>Resultados</h2>
      <p>¿Es maliciosa? {es_maliciosa}</p>
      <p>Voto: {voto}</p>
      <table>
        <thead>
          <tr>
            <th>Fuente</th>
            <th>Resultado</th>
          </tr>
        </thead>
        <tbody>
          {Object.entries(malicioso).map(([source, result], index) => (
            <tr key={index}>
              <td>{source}</td>
              <td>{result}</td>
            </tr>
          ))}
          {Object.entries(no_malicioso).map(([source, result], index) => (
            <tr key={index}>
              <td>{source}</td>
              <td>{result}</td>
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  );
};

export default TableComponent;
