# -*- coding: utf-8 -*-

import time

class TimeDB:
    _format = "%X %x %Z"
    def __init__(self):
        self.curtime = None
        self.db = None

    def get_last_time(self):
        return self.curtime

    def push_time(self, time):
        self.curtime = time
        self.db.write(time + "\n")
        self.db.flush()

    @staticmethod
    def load(path):
        instance = TimeDB()
        instance.db = open(path, "a")
        return instance
