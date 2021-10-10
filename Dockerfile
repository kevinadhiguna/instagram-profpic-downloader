## -- Note -- ##
# (1) First build the docker image :
# $ docker build -t <image-name>:<tag> .
# (example : $ docker build -t insta-profpic-dl:latest .)

# (2) Then run it :
# $ docker run -it -v "$(pwd):/app" <image-name>:<tag>
# (example : $ docker run -it -v "$(pwd):/app" insta-profpic-dl:latest)

FROM python:3.8-slim-buster

WORKDIR /app

COPY requirements.txt .

RUN pip3 install -r requirements.txt

COPY insta.py .

CMD ["python3", "insta.py"]
