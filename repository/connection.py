import os
import psycopg2
import urllib

url = os.environ.get("DATABASE_URL")
result = urllib.parse.urlparse(url)

username = result.username
password = result.password
database = result.path[1:]
hostname = result.hostname


def query(sql, is_query=True):
    con = None
    try:
        con = psycopg2.connect(database=database, user=username, host=hostname, password=password)
        cursor = con.cursor()
        cursor.execute(sql)

        if is_query:
            return cursor.fetchall()
        else:
            rowcount = cursor.rowcount
            con.commit()
            return rowcount
    except psycopg2.DatabaseError as e:
        print(f'Error {e}')
    finally:
        if con:
            con.close()


def insert(sql):
    return query(sql, False)


def update(sql):
    return query(sql, False)


def delete(sql):
    return query(sql, False)


def get_db():
    return None