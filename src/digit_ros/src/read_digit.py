from digit_interface import Digit
import cv2
import numpy as np

while True:
    d = Digit("D20394") # Unique serial number
    d.connect()
    frame = d.get_frame()
    frame = np.array(frame).astype(np.uint8)
    print(frame, type(frame))
    cv2.imshow('Frame', frame)
    cv2.waitKey(1)