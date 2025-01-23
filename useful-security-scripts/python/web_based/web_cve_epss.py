from flask import Flask, render_template, request, jsonify
import requests
import logging

app = Flask(__name__)

# Configure logging for debugging
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

@app.route('/')
def index():
    app.logger.info("Rendering index.html")
    return render_template('index.html')

@app.route('/lookup', methods=['POST'])
def lookup():
    app.logger.info("Received POST request on /lookup")
    cve = request.form.get('cve')
    app.logger.debug(f"User input CVE: {cve}")
    
    if not cve:
        app.logger.error("No CVE identifier provided.")
        return jsonify({'error': 'No CVE identifier provided.'}), 400

    # Construct the URL using the provided CVE identifier
    base_url = "https://cvedb.shodan.io/cve"
    url = f"{base_url}/{cve}"
    app.logger.debug(f"Constructed URL for API: {url}")

    try:
        # Send a GET request to the URL
        response = requests.get(url)
        response.raise_for_status()
        app.logger.info("Successfully retrieved response from CVE API")

        data = response.json()
        app.logger.debug(f"API Response Data: {data}")

        # Calculate EPSS and Ranking EPSS as percentages
        epss_percentage = round(data.get('epss', 0) * 100, 2)
        ranking_epss_percentage = round(data.get('ranking_epss', 0) * 100, 2)

        app.logger.debug(f"EPSS Percentage: {epss_percentage}, Ranking EPSS Percentage: {ranking_epss_percentage}")

        # Return the results to the template
        return render_template(
            'results.html',
            cve_id=data.get('cve_id', 'N/A'),
            summary=data.get('summary', 'N/A'),
            cvss_version=data.get('cvss_version', 'N/A'),
            cvss_v2=data.get('cvss_v2', 'N/A'),
            cvss_v3=data.get('cvss_v3', 'N/A'),
            epss=epss_percentage,
            ranking_epss=ranking_epss_percentage,
            references=data.get('references', []),
            published_time=data.get('published_time', 'N/A')
        )
    except requests.RequestException as e:
        app.logger.error(f"Failed to retrieve data for CVE: {cve}")
        app.logger.debug(f"RequestException: {e}")
        return render_template('error.html', error="Failed to retrieve data for the provided CVE.", details=str(e))

if __name__ == '__main__':
    app.run(debug=True)
