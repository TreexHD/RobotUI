import multiprocessing
import traceback
from robotui.debug import Debug
"""
this file contains the sThread
"""

class SThread(multiprocessing.Process):
    def __init__(self, name, dct):
        """
        :param name: name of the Process
        :param dct: parse the shared dictionary
        """
        super().__init__()
        self.dct = dct
        self.name = name
        self.running = True
        Debug.okblue(" (Threading) Created:  " + self.name)

    def run(self):
        Debug.okblue(" (Threading) Starting: " + self.name)
        try:
            self.running = True
            self.init()
            while self.running:
                self.loop()
            Debug.okblue("(Threading) Stopped:  " + self.name)
        except BaseException as e:
            self.dct['is_sys_thread_running'] = 2
            Debug.okblue("(Threading) Died:  " + self.name)
            traceback.print_exc()
            Debug.okblue("Because of: ")
            Debug.warning(str(e))


    def halt(self):
        """
        trying to normally end the task after one loop itteration
        """
        Debug.okblue("(Threading) Halt:" + self.name)
        self.running = False

    def killing(self):
        """
        killing this thread
        """
        Debug.okblue("(Threading) Killing:" + self.name)
        self.terminate()

    def loop(self):
        """
        override this and use as loop
        """
        pass

    def init(self):
        """
        override this and use as a setup
        """
        pass