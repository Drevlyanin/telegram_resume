import pyrogram
from pyrogram import InlineKeyboardMarkup, InlineKeyboardButton

app = pyrogram.Client('my_resume_bot', api_id='your_api_id_here', api_hash='your_api_hash_here')

interactions_count = 0
user_ids = []

@app.on_message(pyrogram.Filters.command('start'))
def send_welcome(client, message):
    global interactions_count, user_ids

    interactions_count += 1

    user_ids.append(message.chat.id)

    help_button = InlineKeyboardButton('Help', callback_data='help')
    reply_markup = InlineKeyboardMarkup([[help_button]])
    client.send_message(message.chat.id, "Hello! I am your resume bot. How can I help you?", reply_markup=reply_markup)

@app.on_message(pyrogram.Filters.command('stats'))
def send_stats(client, message):
    global interactions_count, user_ids

    if message.chat.id == your_user_id:
        # Send statistics to the bot owner
        stats = f"Interactions count: {interactions_count}\nUser IDs: {user_ids}"
        client.send_message(message.chat.id, stats)

@app.on_callback_query()
def handle_callback_query(client, callback_query):
    # Handle callback query from help button
    if callback_query.data == 'help':
        help_message = "This is a resume bot that helps you create your resume. Use /start to get started!"
        client.send_message(callback_query.message.chat.id, help_message)

app.run()
