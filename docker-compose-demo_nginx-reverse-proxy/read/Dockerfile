FROM       python:3-alpine

WORKDIR    /usr/src/app
COPY       requirements.txt ./
RUN        pip install -r requirements.txt

COPY       read.py ./

RUN        chmod a+x read.py

ENTRYPOINT ["python","read.py"]
