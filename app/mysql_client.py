import mysql.connector

def get_connection():
    return mysql.connector.connect(
        host='mysql',
        port=3306,
        user='root',
        password='root',
        database='digital_hunter'
    )
    
def get_db():
    conn = get_connection()
    cursor = conn.cursor(dictionary=True)

    try:
        yield cursor
    finally:
        cursor.close()
        conn.close()