import os

import psycopg2
from dotenv import load_dotenv

load_dotenv()

# SET UP DATABASE CONNECTION
conn = None
cur = None
try:
    conn = psycopg2.connect(
        database=os.getenv("POSTGRES_DB"),
        user=os.getenv("POSTGRES_USER"),
        password=os.getenv("POSTGRES_PASSWORD"),
        host=os.getenv("POSTGRES_HOST"),
    )
except psycopg2.OperationalError as error:
    print(error)

    # DEFINE A CURSOR
if conn is not None:
    cur = conn.cursor()


# SET UP TABLES
def create_tables():

    try:
        cur.execute(
            """
    CREATE TABLE IF NOT EXISTS notes(  
    id SERIAL PRIMARY KEY, 
    title VARCHAR(100),
    content VARCHAR(8000) 
    )
    """
        )
        cur.execute(
            "INSERT INTO notes (title,content) VALUES (%s, %s)",
            (
                (
                    "Welcome",
                    "This is a ELT/ETL prove of concept lab in flask using postgreSQL and doker",
                )
            ),
        )
        conn.commit()
    except AttributeError as error:
        print(f"{error} 🚧 this should be for bad connection or none DB host")

        return
