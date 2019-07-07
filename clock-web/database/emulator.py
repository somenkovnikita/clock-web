# -*- coding: utf-8 -*-

import time
import threading

from . import timedb


class TimeDBActivityEmulator:
    def __init__(self, timedb: timedb.TimeDB):
        self.timedb = timedb
        self.thread = threading.Thread(target=self._activity_emulate)
        self.stop_need = False

    def start(self):
        self.thread.start()

    def stop(self):
        self.stop_need = True

    def _activity_emulate(self):
        while not self.stop_need:
            self.timedb.push_time(time.strftime('%X %x %Z'))
            if not self.stop_need:
                time.sleep(1)
