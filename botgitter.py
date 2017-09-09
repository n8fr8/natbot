# -*- coding: utf-8 -*-
from chatterbot import ChatBot
from settings import GITTER

import logging
logging.basicConfig(level=logging.INFO)

chatbot = ChatBot("Natbot",
    storage_adapter='chatterbot.storage.SQLStorageAdapter',
    gitter_room=GITTER['ROOM'],
    gitter_api_token=GITTER['API-TOKEN'],
    gitter_only_respond_to_mentions=False,
    input_adapter='chatterbot.input.Gitter',
    output_adapter='chatterbot.output.Gitter',
    database='./database.sqlite3'
)

# The following loop will execute each time the user enters input
while True:
    try:
        response = chatbot.get_response(None)

    # Press ctrl-c or ctrl-d on the keyboard to exit
    except (KeyboardInterrupt, EOFError, SystemExit):
        break

