FROM gcr.io/tensorflow/tensorflow:latest-py3

RUN pip install tflearn
RUN pip install keras
RUN pip install jupyterhub