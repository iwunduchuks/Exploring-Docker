-- Use or create a database (uncomment the next line if needed)
-- CREATE DATABASE my_database;

-- Select the database where the table will be created
USE my_database;

-- Create a new table
CREATE TABLE employees (
    id INT AUTO_INCREMENT PRIMARY KEY,
    first_name VARCHAR(50),
    last_name VARCHAR(50),
    position VARCHAR(100),
    salary DECIMAL(10, 2),
    hire_date DATE
);

-- Insert some data into the table
INSERT INTO employees (first_name, last_name, position, salary, hire_date)
VALUES 
    ('John', 'Doe', 'Software Engineer', 75000.00, '2020-06-15'),
    ('Jane', 'Smith', 'Data Scientist', 85000.00, '2021-01-20'),
    ('Robert', 'Brown', 'DevOps Engineer', 90000.00, '2019-03-10');

-- Query the table to view the inserted data
SELECT * FROM employees;
