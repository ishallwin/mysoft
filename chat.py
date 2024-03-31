import sqlite3
import streamlit as st

# 连接到 SQLite 数据库
# 如果文件不存在，会自动在当前目录创建一个名为 chat.db 的数据库文件

conn = sqlite3.connect('msg.db')    
cursor = conn.cursor()

# 创建一个表来存储聊天消息
cursor.execute('''
CREATE TABLE IF NOT EXISTS messages (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    message TEXT NOT NULL
)
''')

# 提交更改并关闭连接
conn.commit()
#conn.close()

# 连接到 SQLite 数据库
#conn = sqlite3.connect('chat.db')
#cursor = conn.cursor()

# 插入新消息到数据库
def insert_message(message):
    cursor.execute('INSERT INTO messages (message) VALUES (?)', (message,))
    conn.commit()

# 查询最近的10条消息
def get_last_messages():
    cursor.execute('SELECT message FROM messages ORDER BY id DESC LIMIT 10')
    return cursor.fetchall()

# 从数据库中读取并展示最近的10条消息
def dsp_historyMessages():
    messages = get_last_messages()
    for message in reversed(messages):
        st.write(message[0])

# Streamlit 应用程序入口
def main():
    try:
        # 用户输入消息
        if user_message := st.chat_input():
            insert_message(user_message)
        
        # 从数据库中读取并展示最近的10条消息
        dsp_historyMessages()
    finally:
        # 关闭数据库连接
        conn.close()

# 运行 Streamlit 应用程序
if __name__ == "__main__":
    main()

