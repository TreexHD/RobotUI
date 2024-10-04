import time

from robotui.webThread import WebThread
from robotui.sysThread import SysThread
import multiprocessing

"""
this is the main file
"""





class TaskHandler:
    """
    this is the task handler
    """

    def __init__(self):
            manager = multiprocessing.Manager()
            self.websiteTask = None
            self.sysTask = None
            self.program_func = None
            dct = manager.dict()
            dct['stop_sys_thread'] = False
            dct['start_sys_thread'] = False

            self.dct = dct

    def update(self):
        time.sleep(.1)
        if self.dct['stop_sys_thread']:
            self.dct['stop_sys_thread'] = False
            self.stop_sys()
        if self.dct['start_sys_thread']:
            self.dct['start_sys_thread'] = False
            self.create_sys()
            self.start_sys()

    def set_start_program_func(self, func):
        self.program_func = func

    def create_web_site(self):
        self.websiteTask = WebThread("Web",self.dct)

    def start_web_site(self):
        self.websiteTask.start()

    def stop_web_site(self):
        self.websiteTask.killing()

    def create_sys(self):
        self.sysTask = SysThread("Sys",self.dct, self.program_func)

    def start_sys(self):
        self.sysTask.start()

    def stop_sys(self):
        self.sysTask.killing()

