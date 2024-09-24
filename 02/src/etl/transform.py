from datetime import datetime

def transform(response):
    if response is not None and response.status_code == 200:
        data = response.json()
        dt   = datetime.strptime(data['time'], "%Y-%m-%dT%H:%M:%S.%f0Z")
        print('Data transformation successful')
        return data, dt
    else:
        pass