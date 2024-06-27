CREATE USER python WITH PASSWORD 'python';

CREATE DATABASE python_db ENCODING utf8;

ALTER DATABASE python_db OWNER TO python;

GRANT ALL ON DATABASE python_db TO python;