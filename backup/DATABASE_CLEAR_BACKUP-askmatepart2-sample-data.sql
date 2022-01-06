--
-- PostgreSQL database dump
--

-- Dumped from database version 9.5.6
-- Dumped by pg_dump version 9.5.6

ALTER TABLE IF EXISTS ONLY public.question DROP CONSTRAINT IF EXISTS pk_question_id CASCADE;
ALTER TABLE IF EXISTS ONLY public.answer DROP CONSTRAINT IF EXISTS pk_answer_id CASCADE;
ALTER TABLE IF EXISTS ONLY public.answer DROP CONSTRAINT IF EXISTS fk_question_id CASCADE;
ALTER TABLE IF EXISTS ONLY public.comment DROP CONSTRAINT IF EXISTS pk_comment_id CASCADE;
ALTER TABLE IF EXISTS ONLY public.comment DROP CONSTRAINT IF EXISTS fk_question_id CASCADE;
ALTER TABLE IF EXISTS ONLY public.comment DROP CONSTRAINT IF EXISTS fk_answer_id CASCADE;
ALTER TABLE IF EXISTS ONLY public.question_tag DROP CONSTRAINT IF EXISTS pk_question_tag_id CASCADE;
ALTER TABLE IF EXISTS ONLY public.question_tag DROP CONSTRAINT IF EXISTS fk_question_id CASCADE;
ALTER TABLE IF EXISTS ONLY public.tag DROP CONSTRAINT IF EXISTS pk_tag_id CASCADE;
ALTER TABLE IF EXISTS ONLY public.question_tag DROP CONSTRAINT IF EXISTS fk_tag_id CASCADE;

DROP TABLE IF EXISTS public.question;
CREATE TABLE question (
    id serial NOT NULL,
    submission_time timestamp without time zone,
    view_number integer,
    vote_number integer,
    title text,
    message text,
    image text
);

DROP TABLE IF EXISTS public.answer;
CREATE TABLE answer (
    id serial NOT NULL,
    submission_time timestamp without time zone,
    vote_number integer,
    accepted bool,
    question_id integer,
    message text,
    image text
);

DROP TABLE IF EXISTS public.comment;
CREATE TABLE comment (
    id serial NOT NULL,
    question_id integer,
    answer_id integer,
    message text,
    submission_time timestamp without time zone,
    edited_count integer
);


DROP TABLE IF EXISTS public.question_tag;
CREATE TABLE question_tag (
    question_id integer NOT NULL,
    tag_id integer NOT NULL
);

DROP TABLE IF EXISTS public.tag;
CREATE TABLE tag (
    id serial NOT NULL,
    name text
);


ALTER TABLE ONLY answer
    ADD CONSTRAINT pk_answer_id PRIMARY KEY (id);

ALTER TABLE ONLY comment
    ADD CONSTRAINT pk_comment_id PRIMARY KEY (id);

ALTER TABLE ONLY question
    ADD CONSTRAINT pk_question_id PRIMARY KEY (id);

ALTER TABLE ONLY question_tag
    ADD CONSTRAINT pk_question_tag_id PRIMARY KEY (question_id, tag_id);

ALTER TABLE ONLY tag
    ADD CONSTRAINT pk_tag_id PRIMARY KEY (id);

ALTER TABLE ONLY comment
    ADD CONSTRAINT fk_answer_id FOREIGN KEY (answer_id) REFERENCES answer(id) ON DELETE CASCADE;

ALTER TABLE ONLY answer
    ADD CONSTRAINT fk_question_id FOREIGN KEY (question_id) REFERENCES question(id) ON DELETE CASCADE;

ALTER TABLE ONLY question_tag
    ADD CONSTRAINT fk_question_id FOREIGN KEY (question_id) REFERENCES question(id) ON DELETE CASCADE;

ALTER TABLE ONLY comment
    ADD CONSTRAINT fk_question_id FOREIGN KEY (question_id) REFERENCES question(id) ON DELETE CASCADE;

ALTER TABLE ONLY question_tag
    ADD CONSTRAINT fk_tag_id FOREIGN KEY (tag_id) REFERENCES tag(id) ON DELETE CASCADE;


-- Recreate user account table
ALTER TABLE IF EXISTS ONLY user_account DROP CONSTRAINT IF EXISTS pk_account_id CASCADE;

DROP TABLE IF EXISTS user_account;
CREATE TABLE user_account(
    id SERIAL NOT NULL,
    username TEXT,
    email TEXT,
    password TEXT,
    registration_date TIMESTAMP,
    admin BOOLEAN,
    UNIQUE (email),
    UNIQUE (username)
);
ALTER TABLE ONLY user_account ADD CONSTRAINT pk_account_id PRIMARY KEY (id);

-- Recreate user relation tables
ALTER TABLE IF EXISTS ONLY user_question DROP CONSTRAINT IF EXISTS fk_question_id CASCADE;
ALTER TABLE IF EXISTS ONLY user_answer DROP CONSTRAINT IF EXISTS fk_answer_id CASCADE;
ALTER TABLE IF EXISTS ONLY user_comment DROP CONSTRAINT IF EXISTS fk_comment_id CASCADE;
ALTER TABLE IF EXISTS ONLY user_reputation DROP CONSTRAINT IF EXISTS fk_user_id CASCADE;

DROP TABLE IF EXISTS user_question;
CREATE TABLE user_question(
    user_id INTEGER,
    question_id INTEGER
);

DROP TABLE IF EXISTS user_answer;
CREATE TABLE user_answer(
    user_id INTEGER,
    answer_id INTEGER
);

DROP TABLE IF EXISTS user_comment;
CREATE TABLE user_comment(
    user_id INTEGER,
    comment_id INTEGER
);

DROP TABLE IF EXISTS user_reputation;
CREATE TABLE user_reputation(
    user_id INTEGER,
    reputation INTEGER
);

ALTER TABLE ONLY user_question ADD CONSTRAINT fk_question_id FOREIGN KEY(question_id) REFERENCES question(id) ON DELETE CASCADE;

ALTER TABLE ONLY user_answer ADD CONSTRAINT fk_answer_id FOREIGN KEY(answer_id) REFERENCES answer(id) ON DELETE CASCADE;

ALTER TABLE ONLY user_comment ADD CONSTRAINT fk_comment_id FOREIGN KEY(comment_id) REFERENCES comment(id) ON DELETE CASCADE;

ALTER TABLE ONLY user_reputation ADD CONSTRAINT fk_user_id FOREIGN KEY (user_id) REFERENCES user_account(id) ON DELETE CASCADE;



