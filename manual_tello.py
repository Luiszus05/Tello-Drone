from djitellopy import Tello
import cv2

tello = Tello()
tello.connect()

print("Temperature: "+str(tello.get_temperature())) 
print("Battery: "+ str(tello.get_battery()))

tello.streamon()
frame_read = tello.get_frame_read()
cv2.namedWindow("drone")

tello.takeoff()

while True:
    img = frame_read.frame
    img =  cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
    cv2.imshow("drone", img)

    key = cv2.waitKey(1) & 0xff
    if key == 27: # ESC
        print("landing")
        break
    elif key == ord('w'):
        tello.move_forward(30)
    elif key == ord('s'):
        tello.move_back(30)
    elif key == ord('a'):
        tello.move_left(30)
    elif key == ord('d'):
        tello.move_right(30)
    elif key == ord('e'):
        tello.rotate_clockwise(30)
    elif key == ord('q'):
        tello.rotate_counter_clockwise(30)
    elif key == ord('r'):
        tello.move_up(30)
    elif key == ord('f'):
        tello.move_down(30)
    elif key == ord(' '):
        print("emergency")
        tello.emergency()   
        break
tello.land()

# all commands: https://djitellopy.readthedocs.io/en/latest/tello/#djitellopy.tello.Tello.emergency