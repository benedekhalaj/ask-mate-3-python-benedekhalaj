CREATE TABLE user_question(user_id INTEGER, question_id INTEGER);
CREATE TABLE user_answer(user_id INTEGER, answer_id INTEGER);
CREATE TABLE user_comment(user_id INTEGER, comment_id INTEGER);

ALTER TABLE ONLY user_question ADD CONSTRAINT fk_question_id FOREIGN KEY(question_id) REFERENCES question(id) ON DELETE CASCADE;

ALTER TABLE ONLY user_answer ADD CONSTRAINT fk_answer_id FOREIGN KEY(answer_id) REFERENCES answer(id) ON DELETE CASCADE;

ALTER TABLE ONLY user_comment ADD CONSTRAINT fk_comment_id FOREIGN KEY(comment_id) REFERENCES comment(id) ON DELETE CASCADE;
