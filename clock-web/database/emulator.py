# -*- coding: utf-8 -*-

import time
import threading

from . import timedb


class TimeDBActivityEmulator:
    def __init__(self, timedb: timedb.TimeDB):
        self.timedb = timedb
        self.thread = threading.Thread(target=self._activity_emulate)

    def start(self):
        self.thread.start()

    def _activity_emulate(self):
        while True:
            self.timedb.push_time(time.strftime('%X %x %Z'))
            time.sleep(1)

