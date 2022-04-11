"""
Blink LED
"""

import hub
import time

while True:
    hub.led(1)
    time.sleep(.3)
    hub.led(0)
    time.sleep(.3)
