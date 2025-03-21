import sqlite3

def connect():
    conn=sqlite3.connect("users.db")
    return conn

def create_user_entries():
    conn=connect()
    cur= conn.cursor()
    create_sql = """create table if not exists users(id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT, email TEXT)"""
    cur.execute(create_sql)
    cur.execute("delete from users where id in (1,2)")
    cur.execute("INSERT INTO users (name, email) VALUES ('Alice', 'alice@example.com')")
    cur.execute("INSERT INTO users (name, email) VALUES ('Bob', 'bob@example.com')")
    conn.commit()
    cur.close()
    conn.close()

def insert_user_entries(name, email):
    conn=connect()
    cur= conn.cursor()
    cur.execute(f"INSERT INTO users ( name, email) VALUES ('{name}', '{email}')")
    conn.commit()
    cur.close()
    conn.close()

def get_users():
    conn=connect()
    cur= conn.cursor()
    users_fetch_sql = """select * from users"""
    cur.execute(users_fetch_sql)
    users=cur.fetchall()
    cur.close()
    conn.close()
    return users

