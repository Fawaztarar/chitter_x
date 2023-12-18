-- The job of this script is to create a 'users' table in the database.
-- This table will store information about the users including their name, username, password, and email.
-- This script ensures that our application has a dedicated structure for user data management.

-- First, we must check if a 'users' table already exists, and drop it if it does
DROP TABLE IF EXISTS users CASCADE;

-- Then, we create the 'users' table
CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    username VARCHAR(50) NOT NULL UNIQUE,
    password VARCHAR(100) NOT NULL,
    email VARCHAR(100) NOT NULL UNIQUE
);

-- Note: In real-world applications, it's crucial to store passwords securely.
-- This often involves hashing the password before storing it in the database.


-- Inserting random data into the 'users' table
INSERT INTO users (name, username, password, email) VALUES ('Alice Smith', 'alice2023', 'hashed_password123', 'alice.smith@example.com');
INSERT INTO users (name, username, password, email) VALUES ('Bob Johnson', 'bobj2023', 'hashed_password456', 'bob.johnson@example.com');
