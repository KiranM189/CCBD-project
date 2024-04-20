FROM python:3.9-slim

RUN pip install requests beautifulsoup4 pandas

#Fill in the required commands. Clue: Refer to DockerFile of client
COPY server.py /app/server.py

WORKDIR /app

CMD ["python", "server.py"]
