-- settings.sql
CREATE DATABASE waitlist;
CREATE USER waitlistuser WITH PASSWORD 'waitlist';
GRANT ALL PRIVILEGES ON DATABASE waitlist TO waitlistuser;