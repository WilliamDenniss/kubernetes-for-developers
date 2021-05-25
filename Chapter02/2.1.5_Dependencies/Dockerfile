FROM python:3
RUN apt-get update
RUN apt-get install -y mariadb-client
COPY . /app
WORKDIR /app 
CMD python3 hello.py
