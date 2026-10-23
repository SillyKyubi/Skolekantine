from flask import Flask, render_template
from data import VARER
from data import MENY
#Denne funksjonen tar et malenavn som argument og returnerer
#innholdet (html) som skal sendes til klienten
app = Flask(__name__)


# routes??? idk..
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/meny')
def hovedmeny():
    return render_template('meny.html', meny=MENY)

@app.route('/varer')
def varer():
    return render_template('varer.html', varer=VARER)

@app.route('/kontakt')
def kontakter():
    return render_template('kontakt.html')


if __name__ == "__main__":
    app.run(debug=True, port=5005)
