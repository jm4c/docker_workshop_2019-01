FROM       python:3-alpine

WORKDIR    /usr/src/app
COPY       requirements.txt ./
RUN        pip install -r requirements.txt

COPY       write.py ./

RUN        chmod a+x write.py

ENTRYPOINT ["python","write.py"]
