import sqlite3


con = sqlite3.connect("User.db")
cur = con.cursor()

async def create_table():
    cur.execute("CREATE TABLE IF NOT EXISTS user_info_table ("
                "id INTEGER PRIMARY KEY AUTOINCREMENT, "
                "user_id INTEGER, "
                "user_name TEXT, "
                "user_real_name TEXT, "
                "user_contact_information TEXT, "
                "user_location TEXT)")
    con.commit()
    cur.execute("CREATE TABLE IF NOT EXISTS user_language_info ("
                "id INTEGER PRIMARY KEY AUTOINCREMENT, "
                "user_id INTEGER, "
                "user_language TEXT)")
    con.commit()

async def insert_user_language(language, user_id):
    cur.execute("SELECT user_id FROM user_language_info WHERE user_id = ?", (user_id,))
    result = cur.fetchall()

    if not result:
        cur.execute('INSERT INTO user_language_info('
                    'user_id, '
                    'user_language) '
                    'VALUES (?, ?)', (user_id, language))
        con.commit()

async def insert_user_info(user_id, user_name, user_real_name, user_contact_information, user_location):
    cur.execute("INSERT INTO user_info_table("
                "user_id, "
                "user_name, "
                "user_real_name, "
                "user_contact_information, "
                "user_location) "
                "VALUES (?, ?, ?, ?, ?)", (user_id, user_name, user_real_name, user_contact_information, user_location))
    con.commit()

async def is_language(user_id):
    cur.execute("SELECT user_language FROM user_language_info WHERE user_id = ?", (user_id,))
    result = cur.fetchall()
    return result[0][0]
