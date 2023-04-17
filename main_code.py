import pyrogram

app = pyrogram.Client('my_resume_bot', api_id='your_api_id_here', api_hash='your_api_hash_here')

# Variables to track interaction count and user IDs
interactions_count = 0
user_ids = []

@app.on_message(pyrogram.Filters.command('start'))
def send_welcome(client, message):
    global interactions_count, user_ids

    # Increase interaction count on each interaction
    interactions_count += 1

    # Record user ID of the user interacting with the bot
    user_ids.append(message.chat.id)

    # Send a welcome message to the user
    client.send_message(message.chat.id, "Hello! I am your resume bot. How can I help you?")

@app.on_message(pyrogram.Filters.command('stats'))
def send_stats(client, message):
    global interactions_count, user_ids

    # Check if the stats request is coming from the bot owner (you can define your own user ID)
    if message.chat.id == your_user_id:
        # Send statistics to the bot owner
        stats = f"Interactions count: {interactions_count}\nUser IDs: {user_ids}"
        client.send_message(message.chat.id, stats)

app.run()
