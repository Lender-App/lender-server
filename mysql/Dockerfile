# Derived from official mysql image (our base image)
FROM mysql

# Add a database
ENV MYSQL_DATABASE lender

# Add the content of the sql-scripts/ directory to your image
COPY ./scripts/ /docker-entrypoint-initdb.d/A
