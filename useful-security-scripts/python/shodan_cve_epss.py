import requests
import math
from termcolor import colored

def main():
    # Prompt the user to input the CVE identifier
    cve = input("Enter the CVE identifier (e.g., CVE-2023-12345): ").strip()
    if not cve:
        print("No CVE identifier provided. Please run the script again and provide a valid CVE.")
        return

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

        # Define a helper function for color-coded output
        def color_output(label, value):
            if value <= 30:
                print(colored(f"{label}: {value}%", "green"))
            elif value <= 69:
                print(colored(f"{label}: {value}%", "yellow"))
            else:
                print(colored(f"{label}: {value}%", "red"))

        # Output specific fields in a readable format with color-coded EPSS
        print(colored(f"Response for CVE: {cve}", "cyan"))
        print(colored("=============================", "cyan"))
        print(f"CVE ID: {data.get('cve_id', 'N/A')}")
        print(f"Summary: {data.get('summary', 'N/A')}")
        print(f"CVSS Version: {data.get('cvss_version', 'N/A')}")
        print(f"CVSS v2: {data.get('cvss_v2', 'N/A')}")
        print(f"CVSS v3: {data.get('cvss_v3', 'N/A')}")
        color_output("EPSS", epss_percentage)
        color_output("Ranking EPSS", ranking_epss_percentage)
        print("References:")
        for ref in data.get('references', []):
            print(f"- {ref}")
        print(f"Published Time: {data.get('published_time', 'N/A')}")
        print(colored("=============================", "cyan"))

    except requests.RequestException as e:
        print(colored(f"Failed to retrieve data for CVE: {cve}. Please check the CVE identifier and try again.", "red"))
        print(colored(str(e), "red"))

if __name__ == "__main__":
    main()
