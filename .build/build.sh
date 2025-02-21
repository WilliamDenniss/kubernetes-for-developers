# build.sh
# Build and push docker images to DockerHub

cd ..

# Timeserver
docker build ./Chapter02/timeserver -t docker.io/wdenniss/timeserver:1 --push
docker build ./Chapter04/timeserver2 -t docker.io/wdenniss/timeserver:2 --push
docker build ./Chapter04/timeserver3 -t docker.io/wdenniss/timeserver:3 --push
docker build ./Chapter06/timeserver4 -t docker.io/wdenniss/timeserver:4 --push
docker build ./Chapter07/timeserver5 -t docker.io/wdenniss/timeserver:5 --push
docker build ./Chapter12/timeserver6 -t docker.io/wdenniss/timeserver:6 --push
docker build ./Chapter12/timeserver7 -t docker.io/wdenniss/timeserver:7 --push
docker tag docker.io/wdenniss/timeserver:7 docker.io/wdenniss/timeserver:latest
docker push docker.io/wdenniss/timeserver:latest

# Pi worker
docker build ./Chapter10/pi_worker -t docker.io/wdenniss/pi_worker:1 --push
docker build ./Chapter10/pi_worker2 -t docker.io/wdenniss/pi_worker:2 --push
docker build ./Chapter10/pi_worker3 -t docker.io/wdenniss/pi_worker:3 --push
docker build ./Chapter10/pi_worker4 -t docker.io/wdenniss/pi_worker:4 --push
docker tag docker.io/wdenniss/pi_worker:4 docker.io/wdenniss/pi_worker:latest
docker push docker.io/wdenniss/pi_worker:latest

