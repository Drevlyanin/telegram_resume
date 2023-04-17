import pyrogram

app = pyrogram.Client('my_resume_bot', api_id='your_api_id_here', api_hash='your_api_hash_here')

@app.on_message(pyrogram.Filters.command('start'))
def send_welcome(client, message):
    client.send_message(message.chat.id, "Hello! I am your resume bot. How can I help you?")

app.run()
