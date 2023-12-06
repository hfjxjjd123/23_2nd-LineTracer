import cv2
import numpy as np

# 왼쪽으로 가야할 때, 오른쪽으로 가야할 때 central point 기록할 것

def main():
    camera = cv2.VideoCapture(-1)
    camera.set(3,160)
    camera.set(4,120)
    
    while( camera.isOpened() ):
        ret, frame = camera.read() 
        frame = cv2.flip(frame,-1) 
        cv2.imshow( 'before' , frame)
        
        # crop 포함
        crop_img =frame[60:120, 0:160]
        
        gray = cv2.cvtColor(crop_img, cv2.COLOR_BGR2GRAY) 
        blur = cv2.GaussianBlur(gray, (5,5) , 0) 
        
        # 임계점 처리 포함
        ret,thresh1 = cv2.threshold(blur, 123, 255, cv2.THRESH_BINARY_INV)

        #이미지 압축 -> 노이즈 제거
        mask = cv2.erode(thresh1, None, iterations=2)  
        mask = cv2.dilate(mask, None, iterations=2)
        cv2.imshow('masked', mask)
    
        # line 윤곽선 따기
        contours,hierarchy = cv2.findContours(mask.copy(), 1, cv2.CHAIN_APPROX_NONE)
        
        # (윤곽선이 있다면)
        if len(contours) > 0:
            # max 반호나
            c = max(contours, key=cv2.contourArea)
            # moments 계산
            M = cv2.moments(c)
             
            # 무게중심
            cx = int(M['m10']/M['m00'])
            cy = int(M['m01']/M['m00'])
            
           # 무게중심 출력
            cv2.line(crop_img,(cx,0),(cx,720),(255,0,0),1)
            cv2.line(crop_img,(0,cy),(1280,cy),(255,0,0),1)
        
            cv2.drawContours(crop_img, contours, -1, (0,255,0), 1)
            
            # 무게중심(x) 출력
            print(cx)
        
        #? 키보드 종료조건
        if cv2.waitKey(1) == ord('q'):
            break
    
    cv2.destroyAllWindows()

if __name__ == '__main__':
    main()