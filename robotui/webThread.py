from collections.abc import Callable

from robotui.sthread import SThread
from flask import Flask, render_template, request, jsonify

app = Flask(__name__, template_folder='templates')

btn_callback: Callable
def set_btn_callback(callback):
    global btn_callback
    btn_callback = callback


@app.route('/')
def startseite():
    return render_template('index.html')


@app.route('/btn', methods=['POST'])
def button_stop():
    data = request.get_json()
    btn_callback(data)
    return render_template('index.html')


def run(port):
    app.run(debug=False, port=port)

class WebThread(SThread):
    def __init__(self, name, dct):
        super().__init__(name, dct)

    def init(self):
        set_btn_callback(self.btn_func)

    def loop(self):
        run( 80)

    def btn_func(self, value):
        if value['value'] == 2:
            self.dct['stop_sys_thread'] = True
        if value['value'] == 1:
            self.dct['start_sys_thread'] = True




