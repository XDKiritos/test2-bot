import random
import time
from telethon import TelegramClient, events, sync

api_id = '24639866'
api_hash = 'd04ab3fca3e8b8bd2477d8dd1b3e2c97'
session_name = '1BVtsOKIBu33NMAEByUeZKkTgwpQrr-yJLyW9NMfy_P_RLolsVRz--m1xAFVM1impc3goUOrcBchlhhwn2zn0cnw2KgGX5RzkCU0twZIXuy9u8vWSftcFoWBrhl8pBXDunK3KJqY0DNurMwkzdDnPss0_ghoNn2alagCPqtSbBW84eWxb-8fMndvJxMtS8hnWZCwW5jyoK6NTb_yMLOlVbCUWxYXsVnHbVdP9aze-auMJut89Lv6_f9S_1lLNt5Z4ivWZ2YrDgdtxXWtBO_isjyNocLjxoLBKZNh4FDsHBj6KaPGJ2H-ZiSwe7ix14--kpw_ySczpkYNM2xBCg9YExIuX84Yrk5c='

client = TelegramClient(session_name, api_id, api_hash)

# define the message list and the period of time for sending messages
message_list = ['Vc available now', 'Hello boys msg me', 'Hlo \n\n\n\nService \n\n\n\nAvailable \n\n\n\nMsg']
time_interval = 20  # in seconds

# define the personal chat reply message
personal_reply_message = 'Join Here For Free Show 💫 \nhttps://t.me/+_PRSijG6OYczNzBl \nhttps://t.me/+_PRSijG6OYczNzBl'

# define the profile picture list and the period of time for changing profile picture
picture_list = ['https://telegra.ph/file/69967a21c3ed64568d2ff.jpg', 'https://telegra.ph/file/5854d74e7e74213151140.jpg', 'https://telegra.ph/file/0c3c9cb1028a50724968a.jpg']
picture_interval = 20  # in seconds

# define the username list and the period of time for changing the username
username_list = ['PaidGirlpihu', 'PaidGirlpihu2', 'PaidGirlpihu3']
username_interval = 7200  # in seconds

# define the event handler for incoming personal chats
@client.on(events.NewMessage())
async def handle_new_message(event):
    if event.is_private:
        # send the personal chat reply message
        await event.respond(personal_reply_message)

# define the message sending function
async def send_messages():
    while True:
        # get a random message from the message list
        message = random.choice(message_list)
        # send the message to the group
        await client.send_message('@Girls_Chatting_Group_And_Boys', message)
        # wait for the specified time interval
        time.sleep(time_interval)

# define the profile picture changing function
async def change_picture():
    while True:
        # get a random picture from the picture list
        picture = random.choice(picture_list)
        # upload the picture and set it as the profile picture
        await client.set_profile_photo(picture)
        # wait for the specified time interval
        time.sleep(picture_interval)

# define the username changing function
async def change_username():
    while True:
        # get a random username from the username list
        username = random.choice(username_list)
        # change the username
        await client(UpdateUsernameRequest(username))
        # wait for the specified time interval
        time.sleep(username_interval)

import sqlite3

conn = sqlite3.connect('DATABASE_URL')

# example function to insert data into a table
def insert_data(table, data):
    cursor = conn.cursor()
    query = f"INSERT INTO {table} VALUES (?, ?, ?)"
    cursor.execute(query, data)
    conn.commit()

# start the client and run the functions in separate threads
with client:
    client.loop.run_until_complete(asyncio.gather(
        send_messages(),
        change_picture(),
        change_username()
    ))
