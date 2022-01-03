DROP TABLE IF EXISTS user_account;

CREATE TABLE user_account(
    id INTEGER PRIMARY KEY,
    username TEXT,
    email TEXT,
    password TEXT,
    registration_date DATE,
    admin BOOLEAN
);
