from flask import Flask, render_template, request, jsonify
import requests

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/lookup', methods=['POST'])
def lookup():
    cve = request.form.get('cve')
    if not cve:
        return jsonify({'error': 'No CVE identifier provided.'}), 400

    # Construct the URL using the provided CVE identifier
    base_url = "https://cvedb.shodan.io/cve"
    url = f"{base_url}/{cve}"

    try:
        # Send a GET request to the URL
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()

        # Calculate EPSS and Ranking EPSS as percentages
        epss_percentage = round(data.get('epss', 0) * 100, 2)
        ranking_epss_percentage = round(data.get('ranking_epss', 0) * 100, 2)

        # Return the results in JSON format
        return jsonify({
            'cve_id': data.get('cve_id', 'N/A'),
            'summary': data.get('summary', 'N/A'),
            'cvss_version': data.get('cvss_version', 'N/A'),
            'cvss_v2': data.get('cvss_v2', 'N/A'),
            'cvss_v3': data.get('cvss_v3', 'N/A'),
            'epss': epss_percentage,
            'ranking_epss': ranking_epss_percentage,
            'references': data.get('references', []),
            'published_time': data.get('published_time', 'N/A')
        })
    except requests.RequestException as e:
        return jsonify({'error': 'Failed to retrieve data for the provided CVE.', 'details': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)