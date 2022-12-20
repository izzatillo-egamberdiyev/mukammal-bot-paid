import aiomysql
from data.config import MY_BOT,ip

async def connection():
    conn = await aiomysql.connect(host=ip, port=3306,
                                  user='root', password='jshd6d', db=MY_BOT)
    conn.close()
   
async def user_info(chat_id):
    connect = await connection()
    async with connect.cursor() as cursor:
        await cursor.execute(f"SELECT FROM `user` WHERE `chat_id` = {chat_id}")
        print(cursor)
        r = await cursor.fetchall()
        print(r)
