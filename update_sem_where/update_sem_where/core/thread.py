import threading


class Local(threading.local):
    def __init__(self, *args, **kwargs):
        self.tenant = None


local = Local()
