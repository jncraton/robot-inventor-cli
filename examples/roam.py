"""
Simple reflexive agent that drives around a room.

The agent uses the onboard gyro to detect "bumps" from hitting walls or
obstacles and then backs up and picks a new direction.
"""

import hub
import time
import random

drive = None

speed = 50

while True:
    if hub.port.A.motor and hub.port.B.motor:
        drive = hub.port.A.motor.pair(hub.port.B.motor)
        break

while True:
    # Drive forward or sometimes turn
    r = random.randint(0, 1000)
    if r > 995:
        drive.run_at_speed(-speed, -speed)
        time.sleep(1.2 * 50 / speed)
    elif r > 985:
        drive.run_at_speed(speed, speed)
        time.sleep(1.5 * 50 / speed)
    drive.run_at_speed(-speed, speed)
    time.sleep(0.3 * 50 / speed)
    # Try to detect bumps using gyro
    if abs(sum(hub.motion.gyroscope())) > 35:
        drive.run_at_speed(speed, -speed)
        time.sleep(0.3 * 50 / speed)
        drive.run_at_speed(speed, speed)
        time.sleep(random.randint(10, 20) / 10)
