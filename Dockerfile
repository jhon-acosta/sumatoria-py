FROM python:3.9

WORKDIR /app

COPY . .

RUN pip install opencv-python-headless

EXPOSE 9090

CMD ["python", "server.py"]
