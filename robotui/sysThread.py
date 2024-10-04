from robotui.sthread import SThread


class SysThread(SThread):
    def __init__(self, name, dct, func):
        super().__init__(name, dct)
        self.func = func

    def init(self):
        self.dct['is_sys_thread_running'] = True
        self.func()

    def loop(self):
        raise Exception("Sys Program Ended")
