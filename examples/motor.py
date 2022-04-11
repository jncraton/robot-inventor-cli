"""
Spin Motor A slowly
"""

import hub
import time

while True:
    if hub.port.A.motor:
        hub.port.A.motor.run_at_speed(25)
    time.sleep(1000)
