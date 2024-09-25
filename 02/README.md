# Project 02

Steps to use.

1. Make sure you are on Project02 working directory in a bash terminal.

2. Create Docker volume that would be used to persistently store the database and csv file

    ```bash
    docker volume create \
    --label description='docker volume for project02' \
    project02_volume
    ```

    To inspect the created volume, run the command

    ```bash
    docker volume inspect project02_volume
    ```

3. Build Docker image (You only need to do this once unless you update docker file)

    ```bash
    docker build -t docker/project02:1.0 .
    ```

4. Run docker container on default. This would load the data into the SQLite database

    ```bash
    docker run \
    --name project02 \
    --mount type=volume,source=project02_volume,target=/usr/src/app \
    docker/project02:1.0
    ```

5. Run docker container to overide default and load to csv file instead

    ```bash
    docker run \
    --name project02.1 \
    --mount type=volume,source=project02_volume,target=/usr/src/app \
    docker/project02:1.0 pipline_csv.py
    ```

6. Alternatively you can overide default by a change in the environment variable 'LOAD_ROUTE'. Variable is set to default 'database' and loads to database. Change to 'csv' and it loads to the csv file. to do this run the command.

    ```bash
    docker run \
    --name project02 \
    --env LOAD_ROUTE='csv' \
    --mount type=volume,source=project02_volume,target=/usr/src/app \
    docker/project02:1.0    
    ```

7. To remove container and volume run the following commands

    ```bash
    docker rm project02
    ```

    ```bash
    docker volume rm project02_volume
    ```
