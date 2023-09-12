import KeyInput as kp
from djitellopy import Tello
from time import sleep

kp.start()

drone = Tello()
drone.connect()
print(drone.get_battery())


def getKeyboardInput():

    lr,fb, ud,yv = 0,0,0,0
    speed = 50
    if kp.getKey("LEFT"): lr = -speed
    elif kp.getKey("RIGHT"): lr = speed

    if kp.getKey("UP"): fb = speed
    elif kp.getKey("DOWN"): fb = -speed

    if kp.getKey("w"): ud = speed
    elif kp.getKey("d"): ud = -speed

    if kp.getKey("a"): yv = speed
    elif kp.getKey("f"): yv = -speed

    if kp.getKey("t"): drone.takeoff()
    elif kp.getKey("l"): drone.land()

    return  [lr,fb, ud,yv]


while True:

    values = getKeyboardInput()
    drone.send_rc_control(values[0],values[1],values[2],values[3])
    sleep(0.05)
