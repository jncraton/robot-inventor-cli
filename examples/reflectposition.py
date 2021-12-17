"""
Rotates the motor in port A to a position relative to the amount of light
reflected by the light sensor attached to port F.
"""

import hub
import time

while True:
    if hub.port.A.motor and hub.port.F.device:
        hub.port.F.device.mode(1)  # Reflection
        ref = hub.port.F.device.get()[0]
        if ref:
            hub.port.A.motor.run_to_position(ref)
        time.sleep(0.016)
