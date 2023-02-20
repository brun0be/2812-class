from flask import Flask
import requests

# Question 9
app = Flask(__name__)


@app.route('/content')
def read():
    return open("words.txt").read(), 200


@app.route('/register')
def register():
    open("words.txt", 'w').write("hello")
    return "success", 201


if __name__ == '__main__':
    app.run('0.0.0.0', debug=True, port=30000)
    # output1 = requests.get("http://127.0.0.1:30000/content")
    # print(output1.content)
    # output2 = requests.get("http://127.0.0.1:30000/register")
    # print(output2.content)

