import requests

def extract(url, headers):
    try:
        response = requests.get(url, headers=headers)
        print('Data extraction sucessful')
        return response
    except Exception:
        print(f"Error: Unable to fetch data.")
        return None