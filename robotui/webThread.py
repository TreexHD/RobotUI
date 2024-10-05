from collections.abc import Callable
from robotui.sthread import SThread
from flask import Flask, render_template, request, jsonify

app = Flask(__name__, template_folder='templates')

def disable_log():
    import logging
    log = logging.getLogger('werkzeug')
    log.setLevel(logging.ERROR)

btn_callback: Callable
dict_callback: Callable

def set_dct_callback(callback):
    global dict_callback
    dict_callback = callback


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

@app.route('/status')
def status():
    dct = dict_callback()
    console = str(dct['console'])
    stat = dct['is_sys_thread_running']
    cpu_load = 50
    ram_load = 40
    var = {
        "cpu_load": cpu_load,
        "ram_load": ram_load,
        "message": int(not stat) + 1,
        "console": console
    }
    dct['console'] = ""
    return jsonify(status=var)

@app.route('/pgm')
def program_select():
    dct = dict_callback()

    var = {
        "first": str(dct['program_names'])
    }
    return jsonify(status=var)

def run(port):
    app.run(debug=False, port=port, )

class WebThread(SThread):
    def __init__(self, name, dct):
        super().__init__(name, dct)

    def init(self):
        if self.dct['disable_log']:
            disable_log()
        set_btn_callback(self.btn_func)
        set_dct_callback(self.get_dct)

    def loop(self):
        run( 80)

    def btn_func(self, value):
        if value['value'] == 2:
            self.dct['stop_sys_thread'] = True
        if value['value'] == 1:
            self.dct['start_sys_thread'] = True

    def get_dct(self):
        return self.dct




