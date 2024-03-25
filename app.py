from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return 'Hello, this is the first deployment from the best dev team of fluid intellect'

if __name__ == '__main__':
    app.run(port=5000, host='0.0.0.0')
