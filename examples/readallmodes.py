"""
Reads sensor data iterating over every mode.

Uses port F by default
"""

import hub
import time

port = hub.port.F

while True:
    try:
        for i, mode in enumerate(port.info()["modes"]):
            hub.port.F.device.mode(i)
            time.sleep(0.2)
            print(i, mode["name"], hub.port.F.device.get())
        time.sleep(1)
    except:
        pass
