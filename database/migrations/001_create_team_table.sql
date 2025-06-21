CREATE TABLE team (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    city VARCHAR(100),
    state VARCHAR(100),
    type VARCHAR(100),
    conference VARCHAR(100),
    division VARCHAR(100)
);