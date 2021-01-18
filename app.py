#import files
from flask import Flask, render_template, request
from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer


app = Flask(__name__)


bot = ChatBot("Candice")

trainer =  ChatterBotCorpusTrainer(bot)
# trainer.train({'What is your name?':'My name is Candice'})
#trainer.train("chatterbot.corpus.english")
trainer.train("data/greetings.yml")
trainer.train("data/data.yml")

@app.route("/chatbot")
def home():
    return render_template("home.html")
@app.route("/get")
def get_bot_response():
    userText = request.args.get('msg')
    return str(bot.get_response(userText))
if __name__ == "__main__":
    app.run()
