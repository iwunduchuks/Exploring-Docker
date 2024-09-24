import requests

def extract(url, headers):
    try:
        if response.status_code == 200:
            response = requests.get(url, headers=headers)
        return response
    except Exception:
        print(f"Error: Unable to fetch data. Status code: {response.status_code}")
        return None