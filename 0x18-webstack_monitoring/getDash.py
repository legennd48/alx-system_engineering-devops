import requests

# Datadog API base URL
BASE_URL = "https://api.datadoghq.com/api/v1/"

# Datadog API key and application key (replace with your own)
API_KEY = "caf668d26e946f843ab873cf1e91f1f4"
APP_KEY = "77d0b62a0eba0283001d0c660e241a4ba81d0b8b"

def get_dash():
    # Endpoint to retrieve dashboards
    endpoint = BASE_URL + "dashboards"

    # Parameters for the API request
    params = {
        "api_key": API_KEY,
        "application_key": APP_KEY
    }

    try:
        # Make the API request
        response = requests.get(endpoint, params=params)
        response.raise_for_status()

        # Parse the response JSON
        dashboards = response.json().get("dashboards", [])

        # Extract dashboard IDs and titles
        dashboard_ids = {dashboard["id"]: dashboard["title"] for dashboard in dashboards}

        return dashboard_ids
    except requests.exceptions.RequestException as e:
        print("Error:", e)

