import sqlite3

conn = sqlite3.connect('emotion_data.db')
cursor = conn.cursor()

# tôi viết cái này cho mỗi lần tôi xóa cài lại mà nếu chưa có database thì nó tự tạo, đỡ bị lỗi
cursor.execute('''
CREATE TABLE IF NOT EXISTS emotions (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    emotion TEXT NOT NULL,
    confidence REAL NOT NULL,
    timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
)
''')

def insert_emotion(emotion, confidence):
    cursor.execute('''
    INSERT INTO emotions (emotion, confidence)
    VALUES (?, ?)
    ''', (emotion, confidence))
    conn.commit()

def fetch_all_emotions():
    cursor.execute('SELECT * FROM emotions')
    return cursor.fetchall()

# ko dùng thì thôi, cho nó ngắt
def close_connection():
    conn.close()
