import pyautogui
import time


class ScrollController:

    def __init__(self):
        self.scroll_amount = 10
        self.cooldown = 1.2
        self.last_action = 0
        self.gesture_locked = False


    def execute(self, gesture):

        now = time.time()

        if self.gesture_locked:
            return

        if now - self.last_action < self.cooldown:
            return


        if gesture == "SCROLL UP":
            pyautogui.scroll(self.scroll_amount)

        elif gesture == "SCROLL DOWN":
            pyautogui.scroll(-self.scroll_amount)


        self.last_action = now
        self.gesture_locked = True



    def reset(self):
        self.gesture_locked = False