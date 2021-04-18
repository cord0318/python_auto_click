import time
import threading
from pynput.mouse import Button, Controller
from pynput.keyboard import Listener, KeyCode


class AutoClick(threading.Thread):
    def __init__(self, delay, button):
        super(AutoClick, self).__init__()
        self.delay = delay
        self.button = button
        self.running = False
        self.progarm_running = True
        self.mouse = Controller()

    def developer():
        return {"error":False, "name":"Jung Ji-Hyo", "message":"Thanks for use this module!"}

    def start_clicker(self):
        self.running = True
        return {"error":False, "message":"start AutoClick ..."}

    def stop_clicker(self):
        self.running = False
        return {"error":False, "message":"stop AutoClick ..."}

    def exit(self):
        self.stop_clicker()
        self.progarm_running = False
        return {"error":False, "message":"exit AutoClick ..."}

    def run(self):
        try:
            while self.progarm_running:
                while self.running:
                    self.mouse.click(self.button)
                    time.sleep(self.delay)
                time.sleep(0.01)

            return {"error":False, "message":"run AutoClick ..."}

        except Exception as e:
            return {"error":True, "message":e}