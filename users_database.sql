CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    email VARCHAR(255) UNIQUE NOT NULL
);

INSERT INTO users (name, email)
VALUES
('Abarna', 'abarnagmail.com'),
('Kutty', 'kutty@gmail.com'),
('Sanjay', 'sanjay@yahoo.com'),
('Janu', 'janu@yahoo.com'),
('Sangeetha', 'sangeetha@gmail.com');

SELECT * FROM users

SELECT *
FROM users
WHERE name LIKE 'A%'
ORDER BY id;

SELECT *
FROM users
WHERE name LIKE 'S%'
ORDER BY id;

SELECT *
FROM users
WHERE id > 2
ORDER BY id DESC;

SELECT *
FROM users
WHERE email LIKE '%gmail%'
ORDER BY name;

SELECT *
FROM users
WHERE email LIKE '%yahoo%'
ORDER BY name;
