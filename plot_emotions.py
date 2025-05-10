import sqlite3
import matplotlib.pyplot as plt
from collections import Counter

# tạo sẵn cái tên emotion_data.db vậy thôi
conn = sqlite3.connect('emotion_data.db')
cursor = conn.cursor()

cursor.execute('SELECT emotion FROM emotions')
data = cursor.fetchall()

emotions = [row[0] for row in data]
emotion_counts = Counter(emotions)

# Biểu đồ
plt.figure(figsize=(8,5))
plt.bar(emotion_counts.keys(), emotion_counts.values(), color=['red', 'green', 'blue', 'yellow', 'purple', 'orange', 'gray'])
plt.xlabel('Emotion')
plt.ylabel('Frequency')
plt.title('Classfier emotions from cellected data')
plt.xticks(rotation=45)
plt.show()


conn.close()
