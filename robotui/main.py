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
        with multiprocessing.Manager() as manager:
            self.websiteTask = None
            self.sysTask = None
            self.dct = manager.dict()

    def create_web_site(self):
        self.websiteTask = WebThread("Web",self.dct)

    def start_web_site(self):
        self.websiteTask.start()

    def stop_web_site(self):
        self.websiteTask.killing()

    def create_sys(self, func):
        self.sysTask = SysThread("Sys",self.dct, func)

    def start_sys(self):
        self.sysTask.start()

    def stop_sys(self):
        self.sysTask.killing()

