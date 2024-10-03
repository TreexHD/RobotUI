from flask import Flask, render_template

"""
this is the main file
"""

app = Flask(__name__, template_folder='templates')


@app.route('/')
def startseite():
    return render_template('index.html')


def run():
    app.run(debug=True)
