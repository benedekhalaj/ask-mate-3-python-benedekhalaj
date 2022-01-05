from psycopg2.sql import SQL, Literal, Identifier
from database_common import connection_handler as connection
import data_manager


@connection
def get_users(cursor):
    query = """
    SELECT  username, id FROM user_account
    """
    cursor.execute(SQL(query))

    return cursor.fetchall()


@connection
def count_question_votes(cursor, user):
    query = """
    SELECT user_question.user_id, SUM(vote_number) AS vote_number FROM question
    INNER JOIN(
    SELECT question_id, user_id  FROM user_question
    WHERE user_id = {user_id}
    ) user_question ON user_question.question_id = question.id
    GROUP BY user_question.user_id
    """
    cursor.execute(SQL(query).format(
        user_id=Literal(user['id'])
    ))
    return cursor.fetchone()


@connection
def count_answer_votes(cursor, user):
    query = """
    SELECT user_question.user_id, SUM(vote_number) AS vote_number FROM answer
    INNER JOIN(
    SELECT answer_id, user_id  FROM user_answer
    WHERE user_id = {user_id}
    ) user_question ON user_question.answer_id = answer.id
    GROUP BY user_question.user_id
    """
    cursor.execute(SQL(query).format(
        user_id=Literal(user['id'])
    ))
    return cursor.fetchone()


@connection
def fix_reputation(cursor, user, reputation):
    query = """
    INSERT INTO user_reputation(user_id, reputation)
    VALUES (
     {user_id},
     {reputation}
    )
    """
    cursor.execute(SQL(query).format(
        user_id=Literal(user['id']),
        reputation=Literal(reputation)
    ))


def create_reputation():
    for user in get_users():
        total_question_votes = dict(count_question_votes(user))
        total_answer_votes = dict(count_answer_votes(user))
        total_votes = total_question_votes['vote_number'] + total_answer_votes['vote_number']
        reputation_from_votes = (5 * total_question_votes['vote_number']) + (10 * total_answer_votes['vote_number'])

        print(f"""
        User: {user['username']}:
        Votes on questions: {total_question_votes['vote_number']}
        Votes on answers: {total_answer_votes['vote_number']}
        Total votes: {total_votes}
        reputation = {reputation_from_votes}
        """)
        # THIS fix_reputation CAN REWRITE THE WHOLE REPUTATION DATABASE!!! #
        # data_manager.fix_reputation(user, reputation_from_votes)


def main():
    create_reputation()


if __name__ == "__main__":
    main()
