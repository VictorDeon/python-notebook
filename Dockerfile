FROM jupyter/minimal-notebook

USER root

RUN apt-get update && apt-get install -y vim

USER $NB_UID
