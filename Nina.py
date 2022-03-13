import chatterbot_voice as voice
import chatterbot_weather as weather
from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
from chatterbot.comparisons import LevenshteinDistance
from chatterbot.response_selection import get_most_frequent_response


# Create a chatterbot instance
# Set the storage adapter (SQL Adapter)
# Set the path to the database
# Specify input and output adapters (to read the user's input and print the bot's answer on the terminal)
# Specify logic adapters: mathmatical for math questions, Time for time related questions
# and best match to compare the input statement to the known statements to get the closest matching one
# Set the input comparison function to Levenshtein distance ( distance between two words is the minimum number of single-character edits)
# Set the answer selection method to most frequent
bot = ChatBot("Nina",
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


print("Type something to begin...")

# Create a while loop for the bot to run in
while True:
    try:
        bot_input = bot.get_response(None)
        print(bot_input)
    except(KeyboardInterrupt, EOFError, SystemExit):
        break
