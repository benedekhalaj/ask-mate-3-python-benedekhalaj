--
-- PostgreSQL database dump
--

-- Dumped from database version 12.9 (Ubuntu 12.9-0ubuntu0.20.04.1)
-- Dumped by pg_dump version 12.9 (Ubuntu 12.9-0ubuntu0.20.04.1)

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET xmloption = content;
SET client_min_messages = warning;
SET row_security = off;

--
-- Data for Name: question; Type: TABLE DATA; Schema: public; Owner: zsu
--

INSERT INTO public.question (id, submission_time, view_number, vote_number, title, message, image) VALUES (0, '2017-04-28 08:29:00', 31, 7, 'How to make lists in Python?', 'I am totally new to this, any hints?', NULL);
INSERT INTO public.question (id, submission_time, view_number, vote_number, title, message, image) VALUES (1, '2017-04-29 09:19:00', 17, 9, 'Wordpress loading multiple jQuery Versions', 'I developed a plugin that uses the jquery booklet plugin (http://builtbywill.com/booklet/#/) this plugin binds a function to $ so I cann call $(".myBook").booklet();

I could easy managing the loading order with wp_enqueue_script so first I load jquery then I load booklet so everything is fine.

BUT in my theme i also using jquery via webpack so the loading order is now following:

jquery
booklet
app.js (bundled file with webpack, including jquery)', 'images/image1.png');
INSERT INTO public.question (id, submission_time, view_number, vote_number, title, message, image) VALUES (7, '2021-12-09 11:25:34.796071', 13, 0, 'xxxxxx', 'xxxxx', NULL);
INSERT INTO public.question (id, submission_time, view_number, vote_number, title, message, image) VALUES (8, '2021-12-10 06:22:31.132152', 0, -1, 'ZSU', 'WHat is the name of Zsu:', NULL);
INSERT INTO public.question (id, submission_time, view_number, vote_number, title, message, image) VALUES (9, '2022-01-04 18:17:18.424678', 0, 0, 'Benike', 'Beni megcsinálta rendesen', NULL);
INSERT INTO public.question (id, submission_time, view_number, vote_number, title, message, image) VALUES (10, '2022-01-04 19:14:42.254878', 0, 0, 'HELP', 'Próbálkozom dolgokkal, tudnátok segíteni?', NULL);
INSERT INTO public.question (id, submission_time, view_number, vote_number, title, message, image) VALUES (11, '2022-01-04 19:20:22.928101', 0, 0, 'Help please!', 'Where is my wallet?', NULL);


--
-- Data for Name: answer; Type: TABLE DATA; Schema: public; Owner: zsu
--

INSERT INTO public.answer (id, submission_time, vote_number, question_id, message, image) VALUES (1, '2017-04-28 16:49:00', 4, 1, 'You need to use brackets: my_list = []', NULL);
INSERT INTO public.answer (id, submission_time, vote_number, question_id, message, image) VALUES (2, '2017-04-25 14:42:00', 35, 1, 'Look it up in the Python docs', 'images/image2.jpg');
INSERT INTO public.answer (id, submission_time, vote_number, question_id, message, image) VALUES (6, '2021-12-09 11:25:55.431779', 0, 7, 'bbbbbbbbbbbbbbbb', NULL);
INSERT INTO public.answer (id, submission_time, vote_number, question_id, message, image) VALUES (7, '2021-12-09 13:02:37.349644', 0, 7, 'vvvvvvvvv', NULL);
INSERT INTO public.answer (id, submission_time, vote_number, question_id, message, image) VALUES (9, '2022-01-04 15:31:57.890136', 0, 0, 'List = []', NULL);
INSERT INTO public.answer (id, submission_time, vote_number, question_id, message, image) VALUES (8, '2022-01-04 15:32:58.021804', 0, 8, 'Why is this funny??', NULL);
INSERT INTO public.answer (id, submission_time, vote_number, question_id, message, image) VALUES (10, '2022-01-04 18:28:37.959933', 0, 0, 'Do something', NULL);
INSERT INTO public.answer (id, submission_time, vote_number, question_id, message, image) VALUES (11, '2022-01-04 19:15:11.150495', 0, 10, 'Nem tudunk, kérdezz máshol..', NULL);
INSERT INTO public.answer (id, submission_time, vote_number, question_id, message, image) VALUES (12, '2022-01-04 19:15:22.497892', 0, 10, 'Miért vagy ilyen szemét?', NULL);
INSERT INTO public.answer (id, submission_time, vote_number, question_id, message, image) VALUES (13, '2022-01-04 19:21:00.036072', 0, 11, 'May be in your pocket..', NULL);
INSERT INTO public.answer (id, submission_time, vote_number, question_id, message, image) VALUES (14, '2022-01-04 19:21:14.697408', 0, 11, 'wattafukk', NULL);


--
-- Data for Name: comment; Type: TABLE DATA; Schema: public; Owner: zsu
--

INSERT INTO public.comment (id, question_id, answer_id, message, submission_time, edited_count) VALUES (1, 0, NULL, 'Please clarify the question as it is too vague!', '2017-05-01 05:49:00', NULL);
INSERT INTO public.comment (id, question_id, answer_id, message, submission_time, edited_count) VALUES (2, NULL, 1, 'I think you could use my_list = list() as well.', '2017-05-02 16:55:00', NULL);
INSERT INTO public.comment (id, question_id, answer_id, message, submission_time, edited_count) VALUES (13, 8, NULL, 'haha', '2021-12-10 06:23:08.929481', NULL);
INSERT INTO public.comment (id, question_id, answer_id, message, submission_time, edited_count) VALUES (14, 10, NULL, 'Nem, menj anyádba....', '2022-01-04 19:14:58.404581', NULL);
INSERT INTO public.comment (id, question_id, answer_id, message, submission_time, edited_count) VALUES (15, 11, NULL, 'WTF? Your wallet? ', '2022-01-04 19:20:41.969399', NULL);
INSERT INTO public.comment (id, question_id, answer_id, message, submission_time, edited_count) VALUES (16, NULL, 13, 'You are not so kind', '2022-01-04 19:21:44.58982', NULL);


--
-- Data for Name: tag; Type: TABLE DATA; Schema: public; Owner: zsu
--

INSERT INTO public.tag (id, name) VALUES (1, 'python');
INSERT INTO public.tag (id, name) VALUES (2, 'sql');
INSERT INTO public.tag (id, name) VALUES (3, 'css');
INSERT INTO public.tag (id, name) VALUES (5, 'Bu');


--
-- Data for Name: question_tag; Type: TABLE DATA; Schema: public; Owner: zsu
--

INSERT INTO public.question_tag (question_id, tag_id) VALUES (0, 1);
INSERT INTO public.question_tag (question_id, tag_id) VALUES (1, 3);
INSERT INTO public.question_tag (question_id, tag_id) VALUES (8, 1);
INSERT INTO public.question_tag (question_id, tag_id) VALUES (8, 5);
INSERT INTO public.question_tag (question_id, tag_id) VALUES (7, 5);


--
-- Data for Name: user_account; Type: TABLE DATA; Schema: public; Owner: zsu
--

INSERT INTO public.user_account (id, username, email, password, registration_date, admin) VALUES (1, 'Bendus', 'dudi@bende.hu', '$2b$12$ojSXtmgI3l0SMi4rKFbs5engkDrTnAUe9gZE4bXU6MQbZCZ956hWO', '2022-01-04 12:20:02.725685', false);
INSERT INTO public.user_account (id, username, email, password, registration_date, admin) VALUES (2, 'zsu', 'zsezsu6@gmail.com', '$2b$12$QaMov27jIvk2d0RX8Usauu83Vg3cqRpGS5jVhP6.QL3G8311pr/kW', '2022-01-04 14:55:47.641267', false);


--
-- Data for Name: user_answer; Type: TABLE DATA; Schema: public; Owner: zsu
--

INSERT INTO public.user_answer (user_id, answer_id) VALUES (2, 13);
INSERT INTO public.user_answer (user_id, answer_id) VALUES (2, 14);


--
-- Data for Name: user_comment; Type: TABLE DATA; Schema: public; Owner: zsu
--

INSERT INTO public.user_comment (user_id, comment_id) VALUES (2, 15);
INSERT INTO public.user_comment (user_id, comment_id) VALUES (2, 16);


--
-- Data for Name: user_question; Type: TABLE DATA; Schema: public; Owner: zsu
--

INSERT INTO public.user_question (user_id, question_id) VALUES (2, 9);
INSERT INTO public.user_question (user_id, question_id) VALUES (2, 10);
INSERT INTO public.user_question (user_id, question_id) VALUES (2, 11);


--
-- Name: answer_id_seq; Type: SEQUENCE SET; Schema: public; Owner: zsu
--

SELECT pg_catalog.setval('public.answer_id_seq', 14, true);


--
-- Name: comment_id_seq; Type: SEQUENCE SET; Schema: public; Owner: zsu
--

SELECT pg_catalog.setval('public.comment_id_seq', 16, true);


--
-- Name: question_id_seq; Type: SEQUENCE SET; Schema: public; Owner: zsu
--

SELECT pg_catalog.setval('public.question_id_seq', 11, true);


--
-- Name: tag_id_seq; Type: SEQUENCE SET; Schema: public; Owner: zsu
--

SELECT pg_catalog.setval('public.tag_id_seq', 5, true);


--
-- Name: user_account_id_seq; Type: SEQUENCE SET; Schema: public; Owner: zsu
--

SELECT pg_catalog.setval('public.user_account_id_seq', 2, true);


--
-- PostgreSQL database dump complete
--

