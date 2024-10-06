from collections.abc import Callable
from robotui.sthread import SThread
from flask import Flask, render_template, request, jsonify
import psutil
import pkg_resources
package_folder = pkg_resources.resource_filename('your_package_name', '')

app = Flask(__name__, template_folder=package_folder + "/templates")

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


def get_system_usage():
    # Get RAM usage
    ram_usage = psutil.virtual_memory().percent

    # Get overall CPU usage
    cpu_usage = psutil.cpu_percent(interval=1)

    # Get individual CPU core usages
    cpu_core_usages = psutil.cpu_percent(interval=1, percpu=True)

    return {
        'ram_usage': ram_usage,
        'cpu_usage': cpu_usage,
        'cpu_core_usages': cpu_core_usages
    }


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
    usage = get_system_usage()
    console = str(dct['console'])
    stat = dct['is_sys_thread_running']
    prog = dct['program_active']
    cores = ""
    for i, core_usage in enumerate(usage['cpu_core_usages']):
        cores+= "!" + str(core_usage)
    cpu_load = 50
    ram_load = 40
    var = {
        "cpu_load": str(usage['cpu_usage']) + cores,
        "ram_load": usage['ram_usage'],
        "message": int(stat),
        "console": console,
        "program": str(prog)
    }
    dct['console'] = ""
    return jsonify(status=var)

@app.route('/pgm')
def program_select():
    dct = dict_callback()
    data = str(dct['program_names'])[:-1]

    var = {
        "prog": data
    }
    return jsonify(status=var)

def run(port):
    app.run(debug=False, port=port)

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
            self.dct['program_active'] = value['program']
            self.dct['start_sys_thread'] = True

    def get_dct(self):
        return self.dct




