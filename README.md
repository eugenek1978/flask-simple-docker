
# Simple flask docker project on docker

The project has implementation of simple flask service.</br>
The project show how to run project in docker

## Development instruction
### Create and  activate virtual environment with required dependencies
1. `python3 -m venv venv`
2. `. venv/bin/activate`
3. `pip install -r requirements.txt`
4. After work done with dev env `deactivate`

###



## To run application in Docker

1. To build docker image `docker build -t flask-simple-docker:latest .`
2. To run the docker container `docker run -d -p 5000:8888 --name flask-p flask-simple-docker`

## To invoke application apis on host

1. curl http://localhost:5000 - return "Hello World!"
2. curl http://localhost:5000/Yevgeniy - return "Hello Yevgeniy"

