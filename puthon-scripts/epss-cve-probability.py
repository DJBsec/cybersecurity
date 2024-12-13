import requests
import json

def fetch_epss_data(cve, date):
    """
    Fetch EPSS data from the API for a specific CVE and date.

    Parameters:
        cve (str): The CVE identifier (e.g., CVE-2022-26332).
        date (str): The date in YYYY-MM-DD format (e.g., 2022-03-05).

    Returns:
        dict: The JSON response from the API, or an error message.
    """
    url = f"https://api.first.org/data/v1/epss?envelope=true&pretty=true&cve={cve}&date={date}"
    
    try:
        response = requests.get(url)
        response.raise_for_status()  # Raise an HTTPError for bad responses (4xx or 5xx)
        return response.json()
    except requests.exceptions.RequestException as e:
        return {"error": str(e)}

if __name__ == "__main__":
    # Get user input for CVE and date
    cve = input("Enter the CVE (e.g., CVE-2022-26332): ").strip()
    date = input("Enter the date (YYYY-MM-DD): ").strip()

    # Fetch data from the API
    result = fetch_epss_data(cve, date)

    # Print the result
    if "error" in result:
        print(f"Error: {result['error']}")
    else:
        print("API Response:")
        print(json.dumps(result, indent=4))
