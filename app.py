from flask import Flask, render_template, request, redirect, url_for
from langchain_openai import ChatOpenAI
from langchain_core.messages import HumanMessage, SystemMessage
from langchain_openai import OpenAI
from decouple import config
app = Flask(__name__)
SECRET_KEY = config("OPENAI_API_KEY")

chat = ChatOpenAI(openai_api_key= SECRET_KEY)

todos = [{"task": " ", "ans" : " "}]


@app.route('/')
def index():
    return render_template('index.html', todos= todos)
   
@app.route('/add', methods=["POST"])
def add():
    todo = request.form['todo']
    todos.append({"task": todo})
    messages = [
    SystemMessage(content="you are a good assistan answer in 6 words"),
    HumanMessage(content= todo),
    ]
    chat.invoke(messages)
    a = ""
    for chunk in chat.stream(messages):
        a += chunk.content
    
    todos.append({"ans": a})
    return redirect(url_for("index"))

# if __name__ == '__main__':
#     app.run(debug=True)
