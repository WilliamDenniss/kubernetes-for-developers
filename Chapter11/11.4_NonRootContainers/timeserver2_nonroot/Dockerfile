FROM python:3
COPY . /app
WORKDIR /app 
RUN mkdir logs
RUN chgrp -R 0 logs && chmod -R g+rwX logs
CMD python3 server.py
