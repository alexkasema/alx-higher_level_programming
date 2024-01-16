-- A script that creates a table second_table in the database
-- and add multiples rows.

CREATE TABLE IF NOT EXISTS second_table (id INT, name VARCHAR(256), score INT);

-- Query to insert first row to the table.
INSERT INTO second_table (id, name, score) VALUES (1, 'John', 10);

-- Query to insert second row to the table.
INSERT INTO second_table (id, name, score) VALUES (2, 'Alex', 3);

-- Query to insert third row to the table.
INSERT INTO second_table (id, name, score) VALUES (3, 'Bob', 14);

-- Query to insert second row to the table.
INSERT INTO second_table (id, name, score) VALUES (4, 'George', 8);
