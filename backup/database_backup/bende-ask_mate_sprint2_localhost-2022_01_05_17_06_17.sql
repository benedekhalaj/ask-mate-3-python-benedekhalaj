--
-- PostgreSQL database dump
--

-- Dumped from database version 13.5 (Ubuntu 13.5-0ubuntu0.21.10.1)
-- Dumped by pg_dump version 14.1 (Ubuntu 14.1-1.pgdg21.04+1)

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
-- Data for Name: question; Type: TABLE DATA; Schema: public; Owner: bende
--

INSERT INTO public.question (id, submission_time, view_number, vote_number, title, message, image) VALUES (2, '2017-05-01 10:41:00', 1386, 72, 'Drawing canvas with an image picked with Cordova Camera Plugin', 'I''m getting an image from device and drawing a canvas with filters using Pixi JS. It works all well using computer to get an image. But when I''m on IOS, it throws errors such as cross origin issue, or that I''m trying to use an unknown format.
', NULL);
INSERT INTO public.question (id, submission_time, view_number, vote_number, title, message, image) VALUES (1, '2017-04-29 09:19:00', 24, 10, 'Wordpress loading multiple jQuery Versions', 'I developed a plugin that uses the jquery booklet plugin (http://builtbywill.com/booklet/#/) this plugin binds a function to $ so I cann call $(".myBook").booklet();

I could easy managing the loading order with wp_enqueue_script so first I load jquery then I load booklet so everything is fine.

BUT in my theme i also using jquery via webpack so the loading order is now following:

jquery
booklet
app.js (bundled file with webpack, including jquery)', 'images/questions/index_1.png');
INSERT INTO public.question (id, submission_time, view_number, vote_number, title, message, image) VALUES (8, '2021-12-10 08:35:13.184324', 210, 140, ' full crash while opening project 9', 'When I start IntelliJ it starts reading my project and when it comes to about 88% the IDEA vanishes. This happens consistently. I used the bat file to startup and get a stack trace. This is a blocking issue, I can not develop anymore. for further details see forum: http://intellij.net/forums/thread.jspa?threadID=278290&tstart=0

I tried some other EAP builds:
 - #9013 crash (is final 8.0 build)
 - #8995 crash
 - #8940 no problem
 - #8890 no problem
 - #8858 no problem

Full stack dump attached but here is an excerpt:
java.lang.Error: Cleaner terminated abnormally
Caused by: java.io.IOException: The process cannot access the file because another process has locked a portion of the file
', 'images/questions/index_8.jpeg');
INSERT INTO public.question (id, submission_time, view_number, vote_number, title, message, image) VALUES (0, '2017-04-28 08:29:00', 31, 7, 'How to make lists in Python?', 'I am totally new to this, any hints?', 'images/questions/tenor_0.png');
INSERT INTO public.question (id, submission_time, view_number, vote_number, title, message, image) VALUES (5, '2021-12-10 08:07:16.877175', 468, 68975, 'can you recommend a good IT school ?', 'Hello Guys!! I decided to i want to try myself as a programmer :). I would like to learn Python as my first programming language, becouse i heard this is a good programming language for those who''s never programmed before.  Can anyone suggest a good IT school for me? :)  ', NULL);
INSERT INTO public.question (id, submission_time, view_number, vote_number, title, message, image) VALUES (6, '2021-12-10 08:28:34.410508', 34, 16, 'IPVLAN CNI based pods across hosts using VLAN headers', 'I have 2 worker nodes in a Kubernetes cluster. The worker nodes are on the same L2 domain.

Pod00 on Worker-node0 is using IPVLAN. So, net1 gets 10.1.1.1

Pod01 on Worker-node1 is using IPVLAN. So, net1 gets 10.1.1.2

I want to able to ping 10.1.1.1 <---> 10.1.1.2 and it should carry the VLAN header. I don''t see any in the tcpdump. Questions:

    I assumed that the VLAN header is inserted by the Pod itself. However, in the IPVLAN CNI I don''t see any code where VLAN information is taken via config. Is my understanding correct?

    Should interfaces in pod be explicitly configured as vlan-subinterfaces (net1.10) or should I do it on the worker node (enp1s0.10)?

    What should I use as ''master'' interface? enp1s0 or enp1s0.10?

Thanks
', NULL);
INSERT INTO public.question (id, submission_time, view_number, vote_number, title, message, image) VALUES (4, '2021-12-10 07:50:39.102181', 19, 5, 'My SQL query won''t working!!!', 'I wrote this query, but it doesn''t want to work: SELECT * FROM my_table_name here WHERE id = FOUR ; What is the problem wit this?', NULL);
INSERT INTO public.question (id, submission_time, view_number, vote_number, title, message, image) VALUES (7, '2021-12-10 08:30:11.448276', 34, 69, 'Looping through nested array of objects', '

I have following array of objects with nested arrays in it. I wanted to traverse through those arrays and extract all those impact information to separate array:

this is how my input data looks like:

{
    "violations": [{
            "impact": "serious",
            "nodes": [{
                "any": [{
                        "impact": "critical"
                    },
                    {
                        "impact": "serious"
                    }
                ],
                "all": [{
                    "impact": "moderate"
                }],
                "none": [{
                    "impact": "minor"
                }]
            }]
        },
        {
            "impact": "serious",
            "nodes": [{
                "any": [{
                        "impact": "serious"
                    },
                    {
                        "impact": "minor"
                    }
                ],
                "all": [{
                    "impact": "moderate"
                }],
                "none": [{
                    "impact": "serious"
                }]
            }]
        },
        {
            "impact": "serious",
            "nodes": [{
                    "any": [{
                            "impact": "critical"
                        },
                        {
                            "impact": "critical"
                        }
                    ],
                    "all": [{
                        "impact": "moderate"
                    }],
                    "none": [{
                        "impact": "moderate"
                    }]
                },
                {
                    "any": [{
                            "impact": "critical"
                        },
                        {
                            "impact": "critical"
                        }
                    ],
                    "all": [{
                        "impact": "moderate"
                    }],
                    "none": [{
                        "impact": "moderate"
                    }]
                }
            ]
        }
    ]
}

expected output:

[
  {
    "impact": "serious"
  },
  {
    "impact": "critical"
  },
  {
    "impact": "serious"
  },
  {
    "impact": "moderate"
  },
  {
    "impact": "minor"
  },
  {
    "impact": "serious"
  },
  {
    "impact": "serious"
  },
  {
    "impact": "minor"
  },
  ......
]

I''m currently trying with forEach loop like below:

const results = [];
violations.forEach(({ nodes, impact }) => {
  results.push({ impact });
  // flattening nodes
  nodes.forEach(({ any, all, none }) => {
    any.forEach((v) => results.push(v));
    all.forEach((v) => results.push(v));
    none.forEach((v) => results.push(v));
  });
});

is there any better and shorter way to do the same?
', NULL);


--
-- Data for Name: answer; Type: TABLE DATA; Schema: public; Owner: bende
--

INSERT INTO public.answer (id, submission_time, vote_number, accepted, question_id, message, image) VALUES (12, '2021-12-10 08:31:44.921047', 0, NULL, 7, '

You can achieve your result like below snippet:

const items = {
  "violations": [
    {
      "impact": "serious",
      "nodes": [
        {
          "any": [
            {
              "impact": "critical"
            },
            {
              "impact": "serious"
            }
          ],
          "all": [
            {
              "impact": "moderate"
            }
          ],
          "none": [
            {
              "impact": "minor"
            }
          ]
        }
      ]
    },
    {
      "impact": "serious",
      "nodes": [
        {
          "any": [
            {
              "impact": "serious"
            },
            {
              "impact": "minor"
            }
          ],
          "all": [
            {
              "impact": "moderate"
            }
          ],
          "none": [
            {
              "impact": "serious"
            }
          ]
        }
      ]
    },
    {
      "impact": "serious",
      "nodes": [
        {
          "any": [
            {
              "impact": "critical"
            },
            {
              "impact": "critical"
            }
          ],
          "all": [
            {
              "impact": "moderate"
            }
          ],
          "none": [
            {
              "impact": "moderate"
            }
          ]
        },
        {
          "any": [
            {
              "impact": "critical"
            },
            {
              "impact": "critical"
            }
          ],
          "all": [
            {
              "impact": "moderate"
            }
          ],
          "none": [
            {
              "impact": "moderate"
            }
          ]
        }
      ]
    }
  ]
}

const newItems = items.violations.reduce((acc, {impact, nodes})=> {
  acc.push({impact});
  nodes.forEach(item => {
    Object.keys(item).forEach(key => {
      acc.push(...item[key]);
    })
  })
  return acc
}, []);

console.log(newItems);', NULL);
INSERT INTO public.answer (id, submission_time, vote_number, accepted, question_id, message, image) VALUES (6, '2021-12-10 07:45:20.922606', 3, NULL, 0, 'First of try to use this forum if you have any programming question :)
   Welcome here.', NULL);
INSERT INTO public.answer (id, submission_time, vote_number, accepted, question_id, message, image) VALUES (7, '2021-12-10 07:47:10.661185', 1, NULL, 0, '    
name = ''Newcomer''        
print(f''Helo {name})', NULL);
INSERT INTO public.answer (id, submission_time, vote_number, accepted, question_id, message, image) VALUES (13, '2021-12-10 08:36:37.285243', 8, NULL, 8, 'I found the following related JIRAs:
 - http://www.jetbrains.net/jira/browse/IDEADEV-32032 - same stack trace but with an additional JVM crash - unfortunately no build version is mentioned
 - http://www.jetbrains.net/jira/browse/IDEA-18953 - same stack trace but not at startup - ref to JDK bug: http://bugs.sun.com/bugdatabase/view_bug.do?bug_id=4938372

That JDK bug was reported on 1.4.2 and fixed on 7b10 if I read well. I hope you (JetBrains) will not invalidate this bug for that reason. It makes 8.0 completely unusable for me (for my main project at least), Furthermore, the fact that earlier versions (upto #8940) do not have this problem makes me believe that it is preventable.', NULL);
INSERT INTO public.answer (id, submission_time, vote_number, accepted, question_id, message, image) VALUES (14, '2021-12-10 08:36:55.930278', 13, NULL, 8, 'Please, check your antivirus software does not scan IDEA system directory', NULL);
INSERT INTO public.answer (id, submission_time, vote_number, accepted, question_id, message, image) VALUES (15, '2021-12-10 08:37:38.166824', 1, NULL, 8, 'I am getting this stage as well.  Any updates?  I have noticed that it is not deterministic', NULL);
INSERT INTO public.answer (id, submission_time, vote_number, accepted, question_id, message, image) VALUES (4, '2021-12-10 07:18:47.454089', -3, NULL, 2, '

on the option section, set as DATA_URL :

destinationType: Camera.DestinationType.DATA_URL

this will get image as base64 format, to display the image, add

<img src="data:image/jpeg;base64,''+ imageData +''">

then the canvas draw from this img tag
', NULL);
INSERT INTO public.answer (id, submission_time, vote_number, accepted, question_id, message, image) VALUES (1, '2017-04-28 16:49:00', 5, NULL, 1, 'You need to use brackets: my_list = []', NULL);
INSERT INTO public.answer (id, submission_time, vote_number, accepted, question_id, message, image) VALUES (8, '2021-12-10 07:52:50.107457', 14, NULL, 4, 'Is your id INTEGER? becouse you have to specify the integer by number, not like string. Try this : SELECT * FROM my_table_name_here WHERE id = 4; It should have work', NULL);
INSERT INTO public.answer (id, submission_time, vote_number, accepted, question_id, message, image) VALUES (2, '2021-12-10 07:39:11.125062', 35, NULL, 1, 'Look it up in the Python docs', 'images/questions/docs_screen_Su96LAK_2.png');
INSERT INTO public.answer (id, submission_time, vote_number, accepted, question_id, message, image) VALUES (9, '2021-12-10 08:12:57.721925', 39, NULL, 5, 'I This your best choice would be CodeCool :)', 'images/answers/codecool_9.png');
INSERT INTO public.answer (id, submission_time, vote_number, accepted, question_id, message, image) VALUES (10, '2021-12-10 08:16:31.177571', 135, NULL, 5, 'Try Codecool!! You wont be dissapointed for sure!!! They have the best mentors and their teaching technics.... well just have to experience it :)', 'images/answers/a8f2f47c57b1ff6e2c5c26229d7083ff_10.jpeg');
INSERT INTO public.answer (id, submission_time, vote_number, accepted, question_id, message, image) VALUES (11, '2021-12-10 08:26:01.203977', 16548, NULL, 5, 'CODECOOL !!!!! Forget University or some other bootcamps like Greenfox :'')... I recommend Codecool , you wont dissapointed. i learned there and that year was the greatest year in my life . I finished the school in 2019 and now i have a huge IT company: Jinja3 Foum :). they have everything what you need :)', 'images/answers/balna_eye_11.png');


--
-- Data for Name: comment; Type: TABLE DATA; Schema: public; Owner: bende
--

INSERT INTO public.comment (id, question_id, answer_id, message, submission_time, edited_count) VALUES (7, 1, NULL, 'Do you really need to use multiple versions of jQuery? Doing that normally creates more problems than it solves.', '2021-12-10 07:26:10.661588', 1);
INSERT INTO public.comment (id, question_id, answer_id, message, submission_time, edited_count) VALUES (14, 1, NULL, 'no, no, no exactly BECAUSE i have multiple versions (wordpress loads jquery and my theme loads jquery) it causes problems.', '2021-12-10 07:26:38.717418', NULL);
INSERT INTO public.comment (id, question_id, answer_id, message, submission_time, edited_count) VALUES (15, NULL, 2, 'https://docs.python.org/3/', '2021-12-10 07:28:37.769986', NULL);
INSERT INTO public.comment (id, question_id, answer_id, message, submission_time, edited_count) VALUES (17, NULL, 7, 'Ohhh i understand this codeee :'')', '2021-12-10 07:47:52.280575', NULL);
INSERT INTO public.comment (id, question_id, answer_id, message, submission_time, edited_count) VALUES (18, 0, NULL, 'heey :) Welcome Here!!!', '2021-12-10 07:48:13.476414', NULL);
INSERT INTO public.comment (id, question_id, answer_id, message, submission_time, edited_count) VALUES (20, 5, NULL, 'Maybe you should look for ion internet first :)', '2021-12-10 08:10:24.158453', NULL);
INSERT INTO public.comment (id, question_id, answer_id, message, submission_time, edited_count) VALUES (21, NULL, 9, '100% Right!! They are the best of all time :)', '2021-12-10 08:13:26.877028', NULL);
INSERT INTO public.comment (id, question_id, answer_id, message, submission_time, edited_count) VALUES (22, NULL, 10, 'And those parties....', '2021-12-10 08:17:08.463571', NULL);
INSERT INTO public.comment (id, question_id, answer_id, message, submission_time, edited_count) VALUES (23, NULL, 10, 'do you remember 2021 halloween? that was awesome dudeee. the mentors had awesome costume :'') i will never forget that day :)', '2021-12-10 08:18:27.877263', NULL);
INSERT INTO public.comment (id, question_id, answer_id, message, submission_time, edited_count) VALUES (24, NULL, 10, 'And those attendances and workshops.... good memories. i want to feel that feeling again...', '2021-12-10 08:19:35.186725', NULL);
INSERT INTO public.comment (id, question_id, answer_id, message, submission_time, edited_count) VALUES (25, NULL, 11, 'Woow The owner of the forum is a Codecooler? Niceee', '2021-12-10 08:26:46.158707', NULL);
INSERT INTO public.comment (id, question_id, answer_id, message, submission_time, edited_count) VALUES (26, 7, NULL, 'There are shorter ways to do the same, but at the expense of readability. I think your code is better than any of the answers below, because it is easy to see what happens and therefore easier to maintain with low risk of introducing bugs. That is much more important than saving a few lines of code.', '2021-12-10 08:31:04.753878', NULL);
INSERT INTO public.comment (id, question_id, answer_id, message, submission_time, edited_count) VALUES (27, NULL, 14, 'Tried it, but unfortunately that does not make any difference.', '2021-12-10 08:37:17.463034', NULL);
INSERT INTO public.comment (id, question_id, answer_id, message, submission_time, edited_count) VALUES (28, NULL, 15, '
I tried to start m-a-n-y times and occasionally I am getting through reading all the project files. From then on everything is fine as long as I properly close IntelliJ. When my machine crashes or if the IDE is irregularly closed I am in for many hours of trying to get the caches to fill correctly again. 

I also tried feeding in parts of the class path one-by-one, adding more and more, restarting in between. That also seems to work but is tedious as well.

Still not happy :-( but I paid for the 8-license anyway ;-) that should be worth some attention, right?
Shane commented 11 Dec 2008 00:37', '2021-12-10 08:38:09.21105', NULL);
INSERT INTO public.comment (id, question_id, answer_id, message, submission_time, edited_count) VALUES (29, NULL, 15, 'I just got it working with the EAP build, maybe you can try the same: 

     IDEA build: 9540
     JDK: 1.6.0_10
     Launch: Update the idea.bat and inserting this at the top: SET IDEA_JDK=C:\Java\jdk1.6.0_10 (change to your JDK path), then run idea.bat
     Delete the .iws file and all caches in the IDEA system directory


Not ideal but at least I am not stuck.  Hope this works for you.

Yes, I agree this deserves some attention.  But I am the only person with this problem of my development department (over 100 people) so there you have it.', '2021-12-10 08:38:30.132074', NULL);
INSERT INTO public.comment (id, question_id, answer_id, message, submission_time, edited_count) VALUES (19, NULL, 8, 'yes this was the problem :'') thank you so much!!!!!', '2021-12-10 09:55:10.647641', 1);


--
-- Data for Name: tag; Type: TABLE DATA; Schema: public; Owner: bende
--

INSERT INTO public.tag (id, name) VALUES (5, 'cordova');
INSERT INTO public.tag (id, name) VALUES (6, 'canvas');
INSERT INTO public.tag (id, name) VALUES (7, 'pixi.js');
INSERT INTO public.tag (id, name) VALUES (8, 'jquery');
INSERT INTO public.tag (id, name) VALUES (9, 'wordpress');


--
-- Data for Name: question_tag; Type: TABLE DATA; Schema: public; Owner: bende
--

INSERT INTO public.question_tag (question_id, tag_id) VALUES (1, 8);
INSERT INTO public.question_tag (question_id, tag_id) VALUES (1, 9);
INSERT INTO public.question_tag (question_id, tag_id) VALUES (2, 5);
INSERT INTO public.question_tag (question_id, tag_id) VALUES (2, 6);
INSERT INTO public.question_tag (question_id, tag_id) VALUES (2, 7);


--
-- Data for Name: user_account; Type: TABLE DATA; Schema: public; Owner: bende
--

INSERT INTO public.user_account (id, username, email, password, registration_date, admin) VALUES (1, 'bende', 'dudaskobende@gmail.com', '$2b$12$6bQAyohbTKxYN7Jn3EdH3uuAB.EzvYL4CrbtYlAXyw5rBbdHKw3U6', '2022-01-04 19:32:57.80833', true);
INSERT INTO public.user_account (id, username, email, password, registration_date, admin) VALUES (2, 'zsu', 'zsezsu6@gmail.com', '$2b$12$5F5X7x6zmhWxGY8cqh0jl.ANYWMP/yzBEDVeQ9faz5.0go1M2Td6W', '2022-01-05 11:52:42.870274', false);
INSERT INTO public.user_account (id, username, email, password, registration_date, admin) VALUES (3, 'Beni', 'beni@benimail.hu', '$2b$12$NfwKgv45MXmLFfFhfUAJM.mVD0u4sVewrLBQBT3bIxoyeeO05LZm.', '2022-01-05 12:18:52.885141', false);
INSERT INTO public.user_account (id, username, email, password, registration_date, admin) VALUES (4, 'Eddie Murphy', 'eddie@murphy.com', '$2b$12$fQbcNM5hWqaWpbfzbGiKEuNB0Wr74BMdVbBCCC8ahVrLqDILd6L1q', '2022-01-05 12:22:15.676845', false);
INSERT INTO public.user_account (id, username, email, password, registration_date, admin) VALUES (5, 'Johnny Deep', 'dzsonni@depp.hu', '$2b$12$1xMc3aY6evgXGzq3Wm6LA.2OHwYAgHwHX04X36Z.aesrfIRRO22C6', '2022-01-05 12:26:19.241824', false);
INSERT INTO public.user_account (id, username, email, password, registration_date, admin) VALUES (6, 'Scarlet', 'scarlet@johansson.com', '$2b$12$zz7ngbedWx3Fsb6QJqD.vOAeK0cLvK4h.6evYnpZ7aTF7rQjGmSPW', '2022-01-05 12:27:27.846725', false);


--
-- Data for Name: user_answer; Type: TABLE DATA; Schema: public; Owner: bende
--

INSERT INTO public.user_answer (user_id, answer_id) VALUES (1, 1);
INSERT INTO public.user_answer (user_id, answer_id) VALUES (1, 2);
INSERT INTO public.user_answer (user_id, answer_id) VALUES (1, 4);
INSERT INTO public.user_answer (user_id, answer_id) VALUES (2, 6);
INSERT INTO public.user_answer (user_id, answer_id) VALUES (2, 7);
INSERT INTO public.user_answer (user_id, answer_id) VALUES (2, 8);
INSERT INTO public.user_answer (user_id, answer_id) VALUES (3, 9);
INSERT INTO public.user_answer (user_id, answer_id) VALUES (3, 10);
INSERT INTO public.user_answer (user_id, answer_id) VALUES (4, 11);
INSERT INTO public.user_answer (user_id, answer_id) VALUES (4, 12);
INSERT INTO public.user_answer (user_id, answer_id) VALUES (5, 13);
INSERT INTO public.user_answer (user_id, answer_id) VALUES (6, 14);
INSERT INTO public.user_answer (user_id, answer_id) VALUES (6, 15);


--
-- Data for Name: user_comment; Type: TABLE DATA; Schema: public; Owner: bende
--

INSERT INTO public.user_comment (user_id, comment_id) VALUES (1, 7);
INSERT INTO public.user_comment (user_id, comment_id) VALUES (1, 14);
INSERT INTO public.user_comment (user_id, comment_id) VALUES (6, 15);
INSERT INTO public.user_comment (user_id, comment_id) VALUES (1, 17);
INSERT INTO public.user_comment (user_id, comment_id) VALUES (5, 18);
INSERT INTO public.user_comment (user_id, comment_id) VALUES (5, 19);
INSERT INTO public.user_comment (user_id, comment_id) VALUES (6, 21);
INSERT INTO public.user_comment (user_id, comment_id) VALUES (4, 21);
INSERT INTO public.user_comment (user_id, comment_id) VALUES (3, 22);
INSERT INTO public.user_comment (user_id, comment_id) VALUES (1, 23);
INSERT INTO public.user_comment (user_id, comment_id) VALUES (3, 24);
INSERT INTO public.user_comment (user_id, comment_id) VALUES (2, 25);
INSERT INTO public.user_comment (user_id, comment_id) VALUES (3, 26);
INSERT INTO public.user_comment (user_id, comment_id) VALUES (2, 27);
INSERT INTO public.user_comment (user_id, comment_id) VALUES (2, 28);
INSERT INTO public.user_comment (user_id, comment_id) VALUES (2, 29);


--
-- Data for Name: user_question; Type: TABLE DATA; Schema: public; Owner: bende
--

INSERT INTO public.user_question (user_id, question_id) VALUES (1, 6);
INSERT INTO public.user_question (user_id, question_id) VALUES (1, 7);
INSERT INTO public.user_question (user_id, question_id) VALUES (2, 0);
INSERT INTO public.user_question (user_id, question_id) VALUES (2, 8);
INSERT INTO public.user_question (user_id, question_id) VALUES (3, 2);
INSERT INTO public.user_question (user_id, question_id) VALUES (4, 4);
INSERT INTO public.user_question (user_id, question_id) VALUES (5, 5);
INSERT INTO public.user_question (user_id, question_id) VALUES (6, 1);


--
-- Data for Name: user_reputation; Type: TABLE DATA; Schema: public; Owner: bende
--

INSERT INTO public.user_reputation (user_id, reputation) VALUES (1, 795);
INSERT INTO public.user_reputation (user_id, reputation) VALUES (2, 915);
INSERT INTO public.user_reputation (user_id, reputation) VALUES (3, 2100);
INSERT INTO public.user_reputation (user_id, reputation) VALUES (4, 165505);
INSERT INTO public.user_reputation (user_id, reputation) VALUES (5, 344955);
INSERT INTO public.user_reputation (user_id, reputation) VALUES (6, 190);


--
-- Name: answer_id_seq; Type: SEQUENCE SET; Schema: public; Owner: bende
--

SELECT pg_catalog.setval('public.answer_id_seq', 15, true);


--
-- Name: comment_id_seq; Type: SEQUENCE SET; Schema: public; Owner: bende
--

SELECT pg_catalog.setval('public.comment_id_seq', 29, true);


--
-- Name: question_id_seq; Type: SEQUENCE SET; Schema: public; Owner: bende
--

SELECT pg_catalog.setval('public.question_id_seq', 8, true);


--
-- Name: tag_id_seq; Type: SEQUENCE SET; Schema: public; Owner: bende
--

SELECT pg_catalog.setval('public.tag_id_seq', 22, true);


--
-- Name: user_account_id_seq; Type: SEQUENCE SET; Schema: public; Owner: bende
--

SELECT pg_catalog.setval('public.user_account_id_seq', 6, true);


--
-- PostgreSQL database dump complete
--

