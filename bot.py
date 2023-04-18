import random
import time
from telethon import TelegramClient, events, sync

api_id = 'YOUR_API_ID'
api_hash = 'YOUR_API_HASH'
session_name = 'YOUR_SESSION_NAME'

client = TelegramClient(session_name, api_id, api_hash)

# define the message list and the period of time for sending messages
message_list = ['Hi there!', 'How are you?', 'Have a nice day!']
time_interval = 60  # in seconds

# define the personal chat reply message
personal_reply_message = 'Thank you for your message. I will get back to you soon!'

# define the profile picture list and the period of time for changing profile picture
picture_list = ['picture1.jpg', 'picture2.jpg', 'picture3.jpg']
picture_interval = 3600  # in seconds

# define the username list and the period of time for changing the username
username_list = ['new_username_1', 'new_username_2', 'new_username_3']
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
        await client.send_message('GROUP_USERNAME', message)
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

# start the client and run the functions in separate threads
with client:
    client.loop.run_until_complete(asyncio.gather(
        send_messages(),
        change_picture(),
        change_username()
    ))
