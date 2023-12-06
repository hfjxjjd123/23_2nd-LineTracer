import cv2
import numpy as np

def main():
    # 카메라를 비디오 입력으로 사용
    camera = cv2.VideoCapture(-1)
    camera.set(3,160) #동영상 가로사이즈 160px
    camera.set(4,120) #동영상 가로사이즈 120px
    
    while( camera.isOpened() ):
        ret, frame = camera.read()
        #? Why flip?
        frame = cv2.flip(frame,-1)
        cv2.imshow( 'before' , frame)
        
        #세로: 60~120px, 가로: 0~160px
        crop_img =frame[60:120, 0:160] 
        
        cv2.imshow('cropped' ,crop_img)
        
        #? 종결조건: 현재는 키보드 q입력
        if cv2.waitKey(1) == ord('q'):
            break
        
    cv2.destroyAllWindows()
     
if __name__ == '__main__':
    main()