FROM postgres:latest
ENV POSTGRES_PASSWORD=secret
ENV POSTGRES_USER=username
ENV POSTGRES_DB=database
# COPY create_table.sql /docker-entrypoint-initdb.d/create_table.sql
ADD create_table.sql /docker-entrypoint-initdb.d/
# CMD [“tail -f /dev/null”]