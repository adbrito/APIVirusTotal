from flask import Flask, request, jsonify
import requests
import os
from dotenv import load_dotenv

app = Flask(__name__)
load_dotenv()

VIRUSTOTAL_API_KEY = os.getenv('VIRUSTOTAL_API_KEY')

@app.route('/check_domain/<domain>', methods=['GET'])
def check_domain(domain):
    if not domain:
        return jsonify({'error': 'No se proporcionó el dominio'}), 400
    
    url = f'https://www.virustotal.com/api/v3/domains/{domain}'
    headers = {'x-apikey': VIRUSTOTAL_API_KEY}  
    
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
          domain_data = response.json()

          # Obtener los resultados del análisis
          results = domain_data["data"]["attributes"]["last_analysis_results"]

          # Obtener los proveedores que consideran el dominio malicioso
          malicious_providers = {provider: result["result"] for provider, result in results.items() if result["result"] != "clean"}

          # Obtener los proveedores que consideran el dominio inofensivo
          clean_providers = {provider: result["result"] for provider, result in results.items() if result["result"] == "clean"}

          # Ordenar los proveedores por score si es malicioso
          sorted_malicious_providers = sorted(malicious_providers.items(), key=lambda x: x[1], reverse=True)

          # Preparar los datos para devolver en formato JSON
          json_data = {
          "malicious_providers": dict(sorted_malicious_providers[:5]),
          "clean_providers": dict(clean_providers)
          }

      # Devolver los datos en formato JSON con código de estado 200
          return jsonify(json_data), 200
    else:
        return jsonify({'error': 'No se pudo obtener la información del dominio'}), response.status_code


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
