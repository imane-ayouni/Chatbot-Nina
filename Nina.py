#import chatterbot_voice as voice
import chatterbot_weather as weather
from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
from chatterbot.comparisons import LevenshteinDistance
from chatterbot.response_selection import get_most_frequent_response
from chatterbot.trainers import ChatterBotCorpusTrainer
import twitter
import logging
from convokit import Corpus, download
import os
import logging
import re


rep_1 = open("Replika.txt","r")
rep_2 = open("Replika02.txt","r")
rep_3 = open("Replika03.txt","r")
wiki_1 = open("wiki_1.txt","r",encoding='utf-8')
wiki_2 = open("WikiQA-1.txt","r",encoding='utf-8')
wiki_3 = open("WikiQA-2.txt","r",encoding='utf-8')
train_data = []


for line in (rep_1):
    m = re.search('(Q:|A:)?(.+)', line)
    if m:
        train_data.append(m.groups()[1])

for line in (rep_2):
    m = re.search('(Q:|A:)?(.+)', line)
    if m:
        train_data.append(m.groups()[1])

for line in (rep_3):
    m = re.search('(Q:|A:)?(.+)', line)
    if m:
        train_data.append(m.groups()[1])

for line in (wiki_1):
    m = re.search('(Q:|A:)?(.+)', line)
    if m:
        train_data.append(m.groups()[1])

for line in (wiki_2):
    m = re.search('(Q:|A:)?(.+)', line)
    if m:
        train_data.append(m.groups()[1])
for line in (wiki_3):
    m = re.search('(Q:|A:)?(.+)', line)
    if m:
        train_data.append(m.groups()[1])


# Create a chatterbot instance
# Set the storage adapter (SQL Adapter)
# Set the path to the database
# Specify input and output adapters (to read the user's input and print the bot's answer on the terminal)
# Specify logic adapters: mathmatical for math questions, Time for time related questions
# and best match to compare the input statement to the known statements to get the closest matching one
# Set the input comparison function to Levenshtein distance ( distance between two words is the minimum number of single-character edits)
# Set the answer selection method to most frequent
bot = ChatBot("Nina",
               preprocessors=['chatterbot.preprocessors.clean_whitespace'],
               storage_adapter="chatterbot.storage.SQLStorageAdapter",
               logic_adapters=[
               'chatterbot.logic.BestMatch',
               'chatterbot.logic.MathematicalEvaluation',
               'chatterbot.logic.TimeLogicAdapter',
               {"import_path" : "chatterbot.logic.BestMatch",
               "statement_comparison_function" : "chatterbot.comparisons.levenshtein_distance",
               "response_selection_method": get_most_frequent_response}


],

               input_adapter='chatterbot.input.TerminalAdapter',
               output_adapter='chatterbot.output.TerminalAdapter',
               database='./database.sqlite3')

c_trainer =  ChatterBotCorpusTrainer(bot)
c_trainer.train(
    "chatterbot.corpus.english")


logger = logging.getLogger()
logger.setLevel(logging.CRITICAL)


#filepath = r"C:\Users\imane\OneDrive\Desktop\train"
#l_trainer = ListTrainer(bot.storage)
#for file in os.listdir(filepath):
#    data = open(filepath +"\\" + file, encoding="utf-8").readlines()
#    l_trainer.train(data)
l_trainer = ListTrainer(bot)

l_trainer.train(train_data)


print("Type something to begin...")

# Create a while loop for the bot to run in
while True:
    print(bot.get_response(input(">>>")))
