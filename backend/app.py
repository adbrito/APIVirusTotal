from flask import Flask, request, jsonify
import requests,os
from dotenv import load_dotenv
from flask_cors import CORS



app = Flask(__name__)
CORS(app)  # Configurar CORS para todas las rutas

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
        
        try:
            
            results = domain_data["data"]["attributes"]["last_analysis_results"]
            
            
            # Ensure results is a dictionary
            if not isinstance(results, dict):
                raise ValueError("Unexpected results structure, expected a dictionary.")
            
            
            voto = domain_data["data"]["attributes"]["last_analysis_stats"]["malicious"]
            esMaliciosa = "Si" if voto > 0 else "No"

            # Ensure each result is a dictionary with a "result" key
            for provider, result in results.items():
                if not isinstance(result, dict) or "result" not in result:
                    raise ValueError(f"Unexpected result structure for provider {provider}: {result}")
            
            # Get malicious and clean providers
            malicious_providers = {provider: result["result"] for provider, result in results.items() if result["result"] == "malicious"}
            clean_providers = {provider: result["result"] for provider, result in results.items() if result["result"] == "clean"}
            
            # Slice the dictionaries
            malicious_providers = dict(list(malicious_providers.items())[:5])
            clean_providers = dict(list(clean_providers.items())[:5])
            
            # Prepare JSON data
            json_data = {
                "malicioso": malicious_providers,
                "no_malicioso": clean_providers,
                "voto": voto,
                "es_maliciosa": esMaliciosa
            }
            
            return jsonify(json_data), 200
        except Exception as e:
            
            return jsonify({"error": str(e)}), 500
    else:
        return jsonify({'error': 'No se pudo obtener la información del dominio'}), response.status_code

if __name__ == '__main__':
    
    app.run(debug=True, host='0.0.0.0', port=5000)
