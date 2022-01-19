FROM postgres:latest
ENV POSTGRES_PASSWORD=secret
ENV POSTGRES_USER=username
ENV POSTGRES_DB=database
# RUN postgres -c config_file=/etc/postgresql.conf
# RUN echo "listen_addresses='*'" >> /etc/postgresql/9.3/main/postgresql.conf
COPY create_db.sql /docker-entrypoint-initdb.d/create_db.sql
