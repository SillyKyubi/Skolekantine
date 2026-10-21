from flask import Flask, render_template
#Denne funksjonen tar et malenavn som argument og returnerer
#innholdet (html) som skal sendes til klienten
app = Flask(__name__)

if __name__ == "__main__":
    app.run()

# routes??? idk..
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/meny')
def hovedmeny():
    return render_template('meny.html')

@app.route('/varer')
def varer():
    return render_template('varer.html')

@app.route('/kontakt')
def kontakter():
    return render_template('kontakt.html')