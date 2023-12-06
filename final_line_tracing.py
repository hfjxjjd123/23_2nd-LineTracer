import cv2
import numpy as np

from serial_command import cmd_arduino

def main():
    camera = cv2.VideoCapture(0)
    camera.set(3,160) 
    camera.set(4,120)

    while( camera.isOpened() ):
        ret, frame = camera.read()
        frame = cv2.flip(frame,-1)
        cv2.imshow('before',frame)
        
        crop_img =frame[60:120, 0:160]
        
        gray = cv2.cvtColor(crop_img, cv2.COLOR_BGR2GRAY)
        blur = cv2.GaussianBlur(gray,(5,5),0)
        
        ret,thresh1 = cv2.threshold(blur,130,255,cv2.THRESH_BINARY_INV)
        
        mask = cv2.erode(thresh1, None, iterations=2)
        mask = cv2.dilate(mask, None, iterations=2)
        cv2.imshow('masked',mask)
    
        contours,hierarchy = cv2.findContours(mask.copy(), 1, cv2.CHAIN_APPROX_NONE)
        
        #? cx 좌/우 이동 기준 설정
        # 95, 125, 39, 65 change
        if len(contours) > 0:
            c = max(contours, key=cv2.contourArea)
            M = cv2.moments(c)
            
            cx = int(M['m10']/M['m00'])
            cy = int(M['m01']/M['m00'])
            
            #? 좌우 이동 속도 설정
            if cx >= 95 and cx <= 125:              
                print("Turn Left!")
                cmd_arduino(40,0)
            elif cx >= 39 and cx <= 65:
                print("Turn Right")
                cmd_arduino(0,40)
            else:
                print("go")
                cmd_arduino(40,40)
        
        #? 종료조건 설정
        if cv2.waitKey(1) == ord('q'):
            break
    
    cv2.destroyAllWindows()