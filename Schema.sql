-- Simple Customer Feedback database
-- One table only - perfect for beginners

CREATE DATABASE IF NOT EXISTS feedback_db;
USE feedback_db;

CREATE TABLE IF NOT EXISTS feedback (
    id         INT AUTO_INCREMENT PRIMARY KEY,
    name       VARCHAR(100),
    rating     INT NOT NULL CHECK (rating BETWEEN 1 AND 5),
    comment    TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Optional: example data
INSERT INTO feedback (name, rating, comment) VALUES
('Anna', 5, 'Great service!'),
('Mike', 3, 'It was okay, but delivery was slow'),
(NULL, 4, 'Anonymous but happy');
