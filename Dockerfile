FROM ubuntu:latest
RUN apt-get update -y
RUN apt-get install -y python3-pip python-dev build-essential
RUN pip install Flask==1.0.2

ENV FLASK_APP hello.py

COPY . /app
WORKDIR /app

ENTRYPOINT ["flask"]
CMD ["run", "--host=0.0.0.0"]
