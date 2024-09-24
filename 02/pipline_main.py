from src.etl import extract, transform, load
import time

def run_pipleine():
    url = "https://rest.coinapi.io/v1/exchangerate/BTC/USD"
    headers = {'X-CoinAPI-Key': '0A4EC419-E056-44E2-B22B-CEDDB3C09AC0'}
    
    start_time = time.time()
    duration = 2 * 60 # 2 min in seconds

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
            load.load(data, dt)
        else:
            break

if __name__ == '__main__':
    run_pipleine()