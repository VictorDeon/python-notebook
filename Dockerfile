FROM jupyter/minimal-notebook
ADD requirements.txt /home/jovyan/work
RUN pip install -r /home/jovyan/work/requirements.txt
