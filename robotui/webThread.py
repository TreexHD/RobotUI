from robotui.sThread import SThread
from flask import Flask, render_template

app = Flask(__name__, template_folder='templates')


@app.route('/')
def startseite():
    return render_template('index.html')


def run(port):
    app.run(debug=True, port=port)


class webThread(SThread):
    def __init__(self, name, dct):
        super().__init__(name, dct)

    def loop(self):
        run(50)
