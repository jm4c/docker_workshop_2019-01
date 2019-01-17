# From a base image
FROM    python:3-alpine

# Sets an environment variable
ENV     TEST="an useless environment var"

# Sets a working directory (default: ~) 
WORKDIR /usr/src/app

# Copies the file requirements.txt from the host
COPY    requirements.txt ./

# Installs the requirements through pip
RUN     pip install -r requirements.txt

# Copies all python files into the working directory
COPY    *.py ./

# Sets permissions 
RUN     chmod a+x *.py

# Makes the container listen the port 5000 when it is running
EXPOSE 5000


# Configures the container to run as an executable (default: /bin/sh)
ENTRYPOINT ["python"]

# Default argument if no arguments are given when starting the container
CMD ["server.py"]
