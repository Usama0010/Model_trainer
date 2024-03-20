# Example makefile for Docker project

# Define tasks
build:
    docker build -t titanic-predictor .

run:
    docker run -d -p 5000:5000 titanic-predictor

test:
    echo "Running tests..."

clean:
    # Add commands to clean up project (e.g., remove Docker images/containers)
    docker stop $(docker ps -a -q)
    docker rm $(docker ps -a -q)
    docker rmi $(docker images -q)

# Set the default task to build
.DEFAULT_GOAL := build

