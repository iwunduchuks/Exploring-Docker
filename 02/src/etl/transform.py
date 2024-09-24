import datetime

def transform(response):
    if response is not None:
        data = response.json()
        dt   = datetime.strptime(data['time'], "%Y-%m-%dT%H:%M:%S.%f0Z")
        return data, dt
    else:
        pass