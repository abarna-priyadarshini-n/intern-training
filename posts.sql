--Create the posts table
CREATE TABLE posts (
    id SERIAL PRIMARY KEY,
    title VARCHAR(200) NOT NULL,
    content TEXT,
    user_id INT,
    FOREIGN KEY (user_id) REFERENCES users(id)
);
--Insert posts
INSERT INTO posts (title, content, user_id)
VALUES
('About Me', 'Hi I am Abarna from Chennai.', 1),
('Education', 'Completed BTech IT and working in IT.', 1),
('Introduction', 'This is Kutty, working in IT.', 2),
('About Me', 'Sanjay here and am pursuing M.Tech 3rd year.', 3),
('Introduction', 'My name is Janu and I just completed my 12th.', 4),
('About Me', 'Hey I am Sangeetha, completed BDS.', 5),
('Profession', 'Working as a dentist and soon opening my new clinic.', 5);
--update posts
UPDATE posts
SET title = 'Education and Profession'
WHERE id = 2;
--delete
DELETE FROM posts
WHERE id = 7;
--Inner Join
SELECT
    posts.id,
    posts.title,
    users.name
FROM posts
INNER JOIN users
ON posts.user_id = users.id;
--LEFT JOIN
SELECT
    users.id,
    users.name,
    posts.title
FROM users
LEFT JOIN posts
ON users.id = posts.user_id;
--GROUP BY
SELECT
    users.name,
    COUNT(posts.id) AS total_posts
FROM users
LEFT JOIN posts
ON users.id = posts.user_id
GROUP BY users.id, users.name
ORDER BY total_posts DESC;