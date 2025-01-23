# CVE Lookup Tool with EPSS and CVSS Scoring

## Overview
This Flask-based web application allows users to search for detailed information about specific CVE (Common Vulnerabilities and Exposures) identifiers. It provides data such as CVSS scores, EPSS percentages, references, and the vulnerability summary retrieved from the [Shodan CVE Database](https://cvedb.shodan.io/).

The tool dynamically displays results with color-coded EPSS scores to indicate the severity of exploitation probabilities.

## Features
- **Search for CVE Details**: Enter a CVE ID (e.g., `CVE-2016-10087`) to retrieve:
  - CVSS Score
  - CVSS v2 and CVSS v3 Scores
  - EPSS (Exploit Prediction Scoring System) Percentage
  - Ranking EPSS Percentage
  - Vulnerability Summary
  - Published Time
  - References for further information
- **Color-Coded EPSS Scores**:
  - **Green**: Low probability (≤ 35%)
  - **Yellow**: Medium probability (36% - 70%)
  - **Red**: High probability (> 70%)
- **User-Friendly Interface**:
  - Responsive and simple web form to input CVE IDs.
  - Clean and formatted results page.
  - Error handling for invalid CVE IDs or connection issues.

## Dependencies
- **Python**: Version 3.6 or higher
- **Flask**: For building the web application
- **Requests**: For making HTTP requests to the Shodan CVE API

Install the required dependencies using:
```bash
python 3 -m pip install flask requests
```

Running Program
```bash
python3 web_cve_epss.py
```
Once script is running open your browser to
```bash
http://127.0.0.1:5000/
```