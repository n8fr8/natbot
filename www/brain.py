#!/usr/bin/python

import locale                                  # Ensures that subsequent open()s 
locale.getpreferredencoding = lambda: 'UTF-8'  # are UTF-8 encoded.

import sys                                     
sys.stdin = open('/dev/stdin', 'r')       # Re-open standard files in UTF-8 
sys.stdout = open('/dev/stdout', 'w')     # mode.
sys.stderr = open('/dev/stderr', 'w') 

import cgi
import cgitb
cgitb.enable()

# Print necessary headers.
print("Content-Type: text/html")
print()

from chatterbot import ChatBot

chatbot = ChatBot("Natbot",
    storage_adapter='chatterbot.storage.SQLStorageAdapter',
    database='./database.sqlite3',
    read_only=True
)


arguments = cgi.FieldStorage()
for i in arguments.keys():
 response = chatbot.get_response(arguments[i].value)
 print(response)
print()
