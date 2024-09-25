from src.etl import extract, transform, load
import time
import yaml

import os

# Get an environment variable
Load_route = os.getenv('LOAD_ROUTE', 'database')
print(f"LOAD_ROUTE: {Load_route}")


# Load the YAML file
with open("Config.yaml", "r") as file:
    data = yaml.safe_load(file)

url = data['url']
headers = data['headers']

def run_pipleine():
    start_time = time.time()
    duration = 30 # seconds

    while True:
        current_time = time.time()
        if current_time - start_time < duration:
            # Extract data
            response = extract.extract(url, headers)
            if response == None:
                continue

            # Transform data
            data, dt = transform.transform(response)

            # Load data
            if Load_route == 'database':
                load.load(data, dt)
            elif Load_route == 'csv':
                load.load_to_csv(data, dt)                
        else:
            break

if __name__ == '__main__':
    run_pipleine()