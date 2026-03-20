import sqlite3

class TaxiBotDB:
    def __init__(self, db_name='taxi_bot.db'):
        self.conn = sqlite3.connect(db_name)
        self.create_tables()

    def create_tables(self):
        with self.conn:
            self.conn.execute('''
                CREATE TABLE IF NOT EXISTS users (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    name TEXT NOT NULL,
                    email TEXT NOT NULL UNIQUE
                )
            ''')
            self.conn.execute('''
                CREATE TABLE IF NOT EXISTS orders (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    user_id INTEGER,
                    order_details TEXT,
                    FOREIGN KEY (user_id) REFERENCES users (id)
                )
            ''')
            self.conn.execute('''
                CREATE TABLE IF NOT EXISTS ratings (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    order_id INTEGER,
                    rating INTEGER CHECK(rating >= 1 AND rating <= 5),
                    FOREIGN KEY (order_id) REFERENCES orders (id)
                )
            ''')

    def add_user(self, name, email):
        with self.conn:
            self.conn.execute('INSERT INTO users (name, email) VALUES (?, ?)', (name, email))

    def update_user(self, user_id, name=None, email=None):
        with self.conn:
            if name:
                self.conn.execute('UPDATE users SET name = ? WHERE id = ?', (name, user_id))
            if email:
                self.conn.execute('UPDATE users SET email = ? WHERE id = ?', (email, user_id))

    def delete_user(self, user_id):
        with self.conn:
            self.conn.execute('DELETE FROM users WHERE id = ?', (user_id,))

    def get_user(self, user_id):
        cursor = self.conn.execute('SELECT * FROM users WHERE id = ?', (user_id,))
        return cursor.fetchone()

    # Similar methods for orders and ratings...

    def __del__(self):
        self.conn.close()