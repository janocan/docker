FROM debian:buster
# USER root
WORKDIR /app
COPY . /app
RUN apt-get update -y && \
    apt-get install -y postgresql libsasl2-dev python-dev \
    libpq-dev libldap2-dev libssl-dev libsnmp-dev \
    python3 python3-pip curl
RUN pip3 install sqlalchemy psycopg2 flask flask_restful
# CMD ["python3", "dbconn.py"]
# CMD ["bash"]
