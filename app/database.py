import sqlite3

DB_FILE = "orders.db"

def get_connection():
    conn = sqlite3.connect(DB_FILE, check_same_thread=False)
    return conn
