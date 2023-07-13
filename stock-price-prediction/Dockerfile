ARG BASE_IMAGE=python:3.8-buster
FROM $BASE_IMAGE


# install java and git
RUN apt-get update && apt-get install -y git
ENV JAVA_HOME "/usr/lib/jvm/default-java"


# install java
RUN apt-get update && apt-get install -y git
ENV JAVA_HOME "/usr/lib/jvm/default-java"
# install project requirements
COPY src/requirements.txt /tmp/requirements.txt
RUN pip install --no-cache -r /tmp/requirements.txt && rm -f /tmp/requirements.txt

# add kedro user
ARG KEDRO_UID=999
ARG KEDRO_GID=0
RUN groupadd -f -g ${KEDRO_GID} kedro_group && \
useradd -m -d /home/kedro_docker -s /bin/bash -g ${KEDRO_GID} -u ${KEDRO_UID} kedro_docker

WORKDIR /home/kedro_docker
USER kedro_docker

# copy the whole project except what is in .dockerignore
ARG KEDRO_UID=999
ARG KEDRO_GID=0
COPY . .

EXPOSE 8888
EXPOSE 8501
EXPOSE 4141

CMD ["kedro", "run"]


