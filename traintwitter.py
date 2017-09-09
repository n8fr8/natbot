# -*- coding: utf-8 -*-
from chatterbot import ChatBot
from settings import TWITTER
import logging 
import sys

# Comment out the following line to disable verbose logging
logging.basicConfig(level=logging.INFO)

chatbot = ChatBot(
    "Natbot",
    twitter_consumer_key=TWITTER["CONSUMER_KEY"],
    twitter_consumer_secret=TWITTER["CONSUMER_SECRET"],
    twitter_access_token_key=TWITTER["ACCESS_TOKEN"],
    twitter_access_token_secret=TWITTER["ACCESS_TOKEN_SECRET"],
    random_seed_word=sys.argv[1:],
    trainer="chatterbot.trainers.TwitterTrainer",
    database='./database.sqlite3'

)

chatbot.train()

chatbot.logger.info('Trained database generated successfully!')
