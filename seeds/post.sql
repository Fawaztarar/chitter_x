-- The job of this script is to create a 'posts' table in the database.
-- This table will store information about posts including the message, user id (as a foreign key), and timestamp.
-- This script ensures that our application has a dedicated structure for post data management.

-- First, we must check if a 'posts' table already exists, and drop it if it does
DROP TABLE IF EXISTS posts;

-- Then, we create the 'posts' table
CREATE TABLE posts (
    id SERIAL PRIMARY KEY,
    message TEXT NOT NULL,
    user_id INT NOT NULL,
    timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (user_id) REFERENCES users(id)
);

-- Note: The 'user_id' column is a foreign key that references the 'id' column of the 'users' table.
-- This ensures data integrity by linking each post to an existing user.

-- Inserting random data into the 'posts' table
-- Note: Ensure that the user_id values correspond to actual user ids in your 'users' table

INSERT INTO posts (message, user_id) VALUES ('This is a test post from user 1', 1);
INSERT INTO posts (message, user_id) VALUES ('Another example post from user 2', 2);
