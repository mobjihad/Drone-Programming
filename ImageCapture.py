from djitellopy import Tello
import cv2 as cv


drone = Tello()
drone.connect()

print(drone.get_battery())

drone.streamon()

while True:

    img = drone.get_frame_read().frame
    img = cv.resize(img, (350 , 250))
    cv.imshow("Video",img)
    cv.waitKey(1)