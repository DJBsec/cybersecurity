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

def get_color(percentile):
    """
    Determine the color for a percentile value.

    Parameters:
        percentile (float): The percentile value.

    Returns:
        str: The ANSI color code.
    """
    if percentile < 30:
        return "\033[32m"  # Green
    elif 30 <= percentile < 75:
        return "\033[33m"  # Yellow
    else:
        return "\033[31m"  # Red

if __name__ == "__main__":
    # Get user input for CVE and date
    cve = input("Enter the CVE (e.g., CVE-2022-26332): ").strip()
    date = input("Enter the date (YYYY-MM-DD): ").strip()

    # Fetch data from the API
    result = fetch_epss_data(cve, date)

    # Extract and process the EPSS and Percentile values
    if "error" in result:
        print(f"Error: {result['error']}")
    else:
        try:
            # Check if the data list is empty
            if not result["data"]:
                print(f"The CVE {cve} is not in the EPSS repository.")
            else:
                data = result["data"][0]  # Access the first item in the 'data' list
                epss = float(data["epss"]) * 100  # Convert to a float and multiply by 100
                percentile = float(data["percentile"]) * 100  # Convert to a float and multiply by 100

                color = get_color(percentile)  # Get the appropriate color for the percentile

                print(f"EPSS: {epss:.2f}% (Chance of it being exploited in the next 30 days)")
                print(f"{color}Percentile: {percentile:.2f}%\033[0m")  # Reset color with \033[0m
        except (KeyError, IndexError, ValueError) as e:
            print(f"Error processing API response: {e}")