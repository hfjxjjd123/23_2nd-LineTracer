import cv2
import numpy as np

def main():
    camera = cv2.VideoCapture(-1)
    camera.set(3,160)
    camera.set(4,120)
    
    while( camera.isOpened() ):
        ret, frame = camera.read()
        frame = cv2.flip(frame,-1)
        cv2.imshow( 'before' , frame)
        
        # crop 적용
        crop_img =frame[60:120, 0:160]
        
        # image to Gray
        gray = cv2.cvtColor(crop_img, cv2.COLOR_BGR2GRAY)
        blur = cv2.GaussianBlur(gray, (5,5) , 0)
        
        # 123보다 작은 값 -> 0으로 변환
        # 검은 선 -> 0 다른 배경 -> 255
        #? 환경에 따른 조정 필요
        ret,thresh1 = cv2.threshold(blur, 123, 255, cv2.THRESH_BINARY_INV)
        cv2.imshow('thresholded' ,thresh1)
        
        #? 탈출조건: keyboard q
        if cv2.waitKey(1) == ord('q'):
            break
        
    cv2.destroyAllWindows()
     
if __name__ == '__main__':
    main()