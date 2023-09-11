import cv2 as cv
import KeyInput as kp
from djitellopy import tello
import time

kp.start()
global img
drone = tello.Tello()
drone.connect()
print(drone.get_battery())

drone.streamon()


def getKeyboardInput():

    lr,fb, ud,yv = 0,0,0,0
    speed = 50
    if kp.getKey("LEFT"): lr = -speed
    elif kp.getKey("RIGHT"): lr = speed

    if kp.getKey("UP"): fb = speed
    elif kp.getKey("DOWN"): fb = -speed

    if kp.getKey("w"): ud = -speed
    elif kp.getKey("d"): ud = speed

    if kp.getKey("a"): yv = -speed
    elif kp.getKey("d"): yv = speed

    if kp.getKey("t"): drone.takeoff(); time.sleep(3)
    elif kp.getKey("l"): drone.land()

    if kp.getKey("z"):
        cv.imwrite(f'Images/{time.time()}.jpg',img)

    return  [lr,fb, ud,yv]


while True:

    values = getKeyboardInput()
    drone.send_rc_control(values[0],values[1],values[2],values[3])

    img = drone.get_frame_read().frame()
    img = cv.resize(img, (350, 250))
    cv.imshow("Video", img)
    cv.waitKey(1)

