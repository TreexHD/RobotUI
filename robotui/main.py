import sThread
"""
this is the main file
"""





class TaskHandler:
    """
    this is the task handler
    """

    def __init__(self):
        self.websiteTask = None
        self.dct = {}

    def start_web_site(self):
        self.websiteTask = sThread.SThread("Web",self.dct)