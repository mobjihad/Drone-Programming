from djitellopy import tello
from time import sleep

drone = tello.Tello()
drone.connect()
print(drone.get_battery())

drone.takeoff()

#Move Forward 50 CM
drone.send_rc_control(0,50,0,0)
sleep(2)

#Move Right 50 cm
drone.send_rc_control(50,0,0,0)
sleep(2)

#Moving 90 Degree Right
drone.send_rc_control(0,0,0,90)
sleep(2)

drone.send_rc_control(0,0,0,0,)
drone.land() # For Landing

