from flask import Flask

app = Flask(__name__)

@app.route('/')
def neko():
    return "<h1>にゃーん</h1>"

if __name__ == "__main__":
    app.run()
