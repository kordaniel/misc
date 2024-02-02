FROM python:3.10-slim

RUN apt-get update && apt-get install -y ffmpeg
# RUN apt-get clean # cache

WORKDIR /usr/src/app

COPY requirements.txt ./

RUN pip3 install --no-cache-dir -r requirements.txt

COPY main.py ./

CMD [ "python", "./main.py" ]

