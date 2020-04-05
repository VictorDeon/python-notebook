FROM jupyter/minimal-notebook

USER root

RUN apt-get update && apt-get install -y \
    mysql-server

USER $NB_UID