from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "DPSA Project!"

if __name__ == '__main__':
    app.run(debug=True)
