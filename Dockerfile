FROM continuumio/miniconda3:4.9.2-alpine
COPY main.py /opt/main.py
ENTRYPOINT ["python", "/opt/main.py"]