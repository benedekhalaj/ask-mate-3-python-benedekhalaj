DROP TABLE IF EXISTS user_account;

CREATE TABLE user_account(
    id SERIAL NOT NULL,
    username TEXT,
    email TEXT,
    password TEXT,
    registration_date TIMESTAMP,
    admin BOOLEAN
);
