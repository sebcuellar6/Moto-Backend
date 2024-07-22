-- settings.sql
CREATE DATABASE moto;
CREATE USER sebastiancuellar WITH PASSWORD '1Password2';
GRANT ALL PRIVILEGES ON DATABASE moto TO sebastiancuellar;
ALTER DATABASE moto OWNER TO sebastiancuellar;