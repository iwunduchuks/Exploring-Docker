# Project 02

Steps to use.

1. Make sure you are on Project02 working directory

2. Build Docker image (You only need to do this once unless you update docker file)

    ```bash
    docker build -t docker/project02:1.0 .
    ```

3. Run docker container on default. This would load the data into the SQLite database

    ```bash
    docker run --name project02 docker/project02:1.0
    ```

4. Run docker container to overide default and load to csv file instead

    ```bash
    docker run --name project02.1 docker/project02:1.0 pipline_csv.py
    ```
