# Import the Tello SDK library and sleep module
from djitellopy import tello
from time import sleep

# Initialize the drone and establish a connection
me = tello.Tello()
me.connect()

# Print the drone's current battery percentage
print("Battery:", me.get_battery(), "%")

# Command the drone to take off
me.takeoff()

# Move the drone forward
me.send_rc_control(0, 35, 0, 0)  # (left/right, forward/backward, up/down, yaw)
sleep(2)

# Move the drone to the right
me.send_rc_control(20, 0, 0, 0)
sleep(2)

# Rotate the drone clockwise
me.send_rc_control(0, 0, 0, 90)
sleep(2)

# Land the drone
me.land()
