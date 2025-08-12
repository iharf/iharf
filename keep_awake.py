#!/usr/bin/env python3
import random
import sys
import time
from datetime import datetime

import pyautogui

CHECK_STATUS_ONCE_IN = 120
WAIT_FOR_POSITION_CHANGE = 10


def current_position():
    return list(pyautogui.position())


def mouse_is_moving():
    pos1 = current_position()
    time.sleep(WAIT_FOR_POSITION_CHANGE)
    pos2 = current_position()
    return not pos1 == pos2


def keep_awake():
    # Shake the mouse a lil bit
    initial_x, initial_y = current_position()
    try:
        for _ in range(random.randint(1, 10)):
            # Mouse
            pyautogui.moveTo(random.randint(1, 1000), random.randint(1, 1000))

            # Keys
            pyautogui.press("shift")

        # Restore controls
        pyautogui.moveTo(initial_x, initial_y)
    except pyautogui.FailSafeException as e:
        print(e)


def inspect_activity_until(time_to_stop: datetime):
    time_to_stop = datetime.now().replace(
        hour=time_to_stop.hour, minute=time_to_stop.minute
    )
    while datetime.now() < time_to_stop:
        if not mouse_is_moving():
            keep_awake()
        time.sleep(CHECK_STATUS_ONCE_IN)

    print(f"Stopping at {datetime.now()}")


if __name__ == "__main__":
    given_time = sys.argv[1]
    date_time_obj = datetime.strptime(given_time, "%H:%M")
    inspect_activity_until(date_time_obj)

