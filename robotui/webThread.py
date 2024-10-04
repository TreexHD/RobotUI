from robotui.sthread import SThread
from flask import Flask, render_template

app = Flask(__name__, template_folder='templates')


@app.route('/')
def startseite():
    return render_template('index.html')


def run(port):
    app.run(debug=False, port=port)


class WebThread(SThread):
    def __init__(self, name, dct):
        super().__init__(name, dct)

    def init(self):
        pass

    def loop(self):
        run( 80)
