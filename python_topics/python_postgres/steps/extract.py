from database.db import cur

# FETH ALL FROM NOTES TABLE


def extract_all_notes() -> list:
    cur.execute("SELECT * FROM notes")
    data = list(cur.fetchall())

    return data
