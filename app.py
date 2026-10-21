from flask import Flask

app = Flask(__name__)

# routes??? idk..
@app.route('/')
@app.route('/home')
@app.route('/varer')
@app.route('/kontakt')

def index():
    return "Hello, world"

if __name__ == "__main__":
    app.run()