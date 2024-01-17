-- A script that creates the database hbtn_0d_usa
-- and the table states (in the database hbtn_0d_usa).
-- states description:
--	id INT unique, auto generated, can’t be null and is a primary key
--	name VARCHAR(256) can’t be null

CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;

-- Use the database we just created
USE hbtn_0d_usa;

-- Create table in this database
CREATE TABLE IF NOT EXISTS states(
	id INT UNIQUE AUTO_INCREMENT NOT NULL PRIMARY KEY,
	name VARCHAR(256) NOT NULL);