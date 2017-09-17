from flask import Flask,render_template,request
from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer

chatbot = ChatBot("myBot")
chatbot.set_trainer(ChatterBotCorpusTrainer)

chatbot.train("chatterbot.corpus.chinese")

app=Flask(__name__)
# anwser = chatbot.get_response("你好")
# print(anwser)

@app.route("/")
def index():
    content = request.args.get("content")
    if content == None:
        content="你好"
    anwser = chatbot.get_response(str(content))
    callback = request.args.get("callback")
    if callback == None:
        callback="callback"
    return callback+"({"+"'data':'"+str(anwser)+"'})"

if __name__ == '__main__':
    app.run()
