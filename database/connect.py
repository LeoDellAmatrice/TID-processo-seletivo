from psycopg2 import pool
from dotenv import load_dotenv
import os

load_dotenv()

DB_USER = os.getenv("DB_USER")
PASSWORD = os.getenv("PASSWORD")
HOST = os.getenv("HOST", "127.0.0.1")
PORT = int(os.getenv("DB_PORT"))
DBNAME = os.getenv("DB_NAME")

db_pool = pool.SimpleConnectionPool(
    minconn=1,
    maxconn=2,
    user=DB_USER,
    password=PASSWORD,
    host=HOST,
    port=PORT,
    dbname=DBNAME
)

from psycopg2.extras import RealDictCursor


class Cursor:
    def __init__(self, commit=True, dict_cursor=False):
        self._do_commit = commit
        self._dict_cursor = dict_cursor

    def __enter__(self):
        self.conn = db_pool.getconn()

        if self._dict_cursor:
            self.cursor = self.conn.cursor(cursor_factory=RealDictCursor)
        else:
            self.cursor = self.conn.cursor()

        return self.cursor

    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_type:
            self.conn.rollback()
        elif self._do_commit:
            self.conn.commit()

        self.cursor.close()
        db_pool.putconn(self.conn)

