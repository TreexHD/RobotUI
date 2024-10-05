from robotui.sthread import SThread


class SysThread(SThread):
    def __init__(self, name, dct, func):
        super().__init__(name, dct)
        self.func = func

    def console_print(self, data):
        self.dct['console'] += (str(data) + "<br>")


    def init(self):
        self.dct['is_sys_thread_running'] = True
        self.func(self.console_print)

    def loop(self):
        raise Exception("Sys Program Ended")
