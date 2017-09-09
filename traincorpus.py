# -*- coding: utf-8 -*-

from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer
from chatterbot.storage import SQLStorageAdapter

import logging
logging.basicConfig(level=logging.INFO)

bot = ChatBot('Natbot',
    storage_adapter='chatterbot.storage.SQLStorageAdapter',
    trainer='chatterbot.trainers.ChatterBotCorpusTrainer',
    database='./database.sqlite3'
)

#bot.train('chatterbot.corpus.english')
bot.train('chatterbot.corpus.spanish')
##chatbot.train('natbot-corpus')

