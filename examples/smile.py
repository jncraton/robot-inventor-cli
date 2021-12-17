"""
Displays an alternative happy and sad face on the hub
"""

import hub
import time

while True:
    hub.display.show(hub.Image("09090:" "00000:" "00000:" "90009:" "09990:"))
    time.sleep(1)
    hub.display.show(hub.Image("09090:" "00000:" "00000:" "09990:" "90009:"))
    time.sleep(1)
