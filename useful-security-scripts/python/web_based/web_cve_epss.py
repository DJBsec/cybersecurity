from flask import Flask, render_template, request
import requests

app = Flask(__name__)

def get_color_class(score):
    """Return a color class based on the score percentage."""
    if score <= 35:
        return 'green'
    elif score <= 70:
        return 'yellow'
    else:
        return 'red'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/lookup', methods=['POST'])
def lookup():
    cve = request.form.get('cve')  # Retrieve CVE input from the form
    if not cve:
        return render_template('error.html', error="No CVE identifier provided.")

    base_url = "https://cvedb.shodan.io/cve"
    url = f"{base_url}/{cve}"

    try:
        # Fetch data from the CVE API
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()

        # Calculate EPSS and Ranking EPSS percentages
        epss_percentage = round(data.get('epss', 0) * 100, 2)
        ranking_epss_percentage = round(data.get('ranking_epss', 0) * 100, 2)

        # Determine color classes based on the score percentages
        epss_color = get_color_class(epss_percentage)
        ranking_epss_color = get_color_class(ranking_epss_percentage)

        # Render the results page with the data
        return render_template(
            'results.html',
            cve_id=data.get('cve_id', 'N/A'),
            summary=data.get('summary', 'N/A'),
            cvss=data.get('cvss', 'N/A'),
            cvss_version=data.get('cvss_version', 'N/A'),
            cvss_v2=data.get('cvss_v2', 'N/A'),
            cvss_v3=data.get('cvss_v3', 'N/A'),
            epss=epss_percentage,
            epss_color=epss_color,
            ranking_epss=ranking_epss_percentage,
            ranking_epss_color=ranking_epss_color,
            references=data.get('references', []),
            published_time=data.get('published_time', 'N/A')
        )
    except requests.RequestException as e:
        return render_template('error.html', error="Failed to retrieve data for the provided CVE.", details=str(e))

if __name__ == '__main__':
    app.run(debug=True)
