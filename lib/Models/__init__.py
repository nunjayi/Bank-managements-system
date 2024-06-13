import sqlite3

CONN = sqlite3.connect('Bank.db')
CURSOR = CONN.cursor()

create_accounts_table_sql = """
CREATE TABLE IF NOT EXISTS accounts (
    account_id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id INTEGER,
    branch_id INTEGER,
    account_type TEXT,
    account_balance FLOAT,
    FOREIGN KEY (user_id) REFERENCES users(user_id),
    FOREIGN KEY (branch_id) REFERENCES branches(branch_id)
)
"""

create_users_table_sql = """
CREATE TABLE IF NOT EXISTS users (
    user_id INTEGER PRIMARY KEY,
    name TEXT,
    password TEXT
)
"""

CURSOR.execute(create_accounts_table_sql)
CURSOR.execute(create_users_table_sql)
CONN.commit()