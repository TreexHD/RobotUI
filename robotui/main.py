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
            self.programs = []
            self.program_func = None
            dct = manager.dict()
            dct['program_names'] = "" # separated by ! .First  one is the selected.
            dct['program_active'] = ""
            dct['console'] = ""
            dct['disable_log'] = False
            dct['stop_sys_thread'] = False
            dct['start_sys_thread'] = False
            dct['is_sys_thread_running'] = False
            dct['console'] += "[BLUE]Booted...[END] <br>"
            self.dct = dct


    def update(self):
        time.sleep(.5)
        if self.dct['start_sys_thread'] and self.dct['is_sys_thread_running']:
            self.dct['start_sys_thread'] = False
        if self.dct['start_sys_thread'] and self.dct['is_sys_thread_running'] == False:
            self.dct['start_sys_thread'] = False
            self.update_sys_thread_func()
            self.create_sys()
            self.start_sys()
        if self.dct['stop_sys_thread']:
            self.dct['stop_sys_thread'] = False
            self.dct['is_sys_thread_running'] = False
            self.stop_sys()

    def update_sys_thread_func(self):
        for i in self.programs:
            if i[0] == self.dct['program_active']:
                self.program_func = i[1]

    def disable_log(self):
        self.dct['disable_log'] = True

    def save_other_programs(self, selected):
        for i in self.programs:
            if i[0] != selected:
                self.dct['program_names'] += i[0] + "!"


    def append_program(self, name, func):
        self.programs.append((name, func))

    def set_start_program_func(self, name):
        for i in self.programs:
            if i[0] == name:
                self.program_func = i[1]
        self.dct['program_names'] += name + "!"
        self.save_other_programs(name)

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
        if self.sysTask is not None:
            self.sysTask.killing()

