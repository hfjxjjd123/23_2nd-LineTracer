import cv2

def main():
    # cv2에 카메라를 기본 입력으로 처리
    camera = cv2.VideoCapture(-1)
    # 동영상의 가로사이즈 처리
    camera.set(3,640)
    # 동영상의 세로사이즈 처리
    camera.set(4,480)
    
    while( camera.isOpened() ):  #카메라가 Open되어 있다면,
        _, image = camera.read()

        # 카메라 이미지 가공 & 시각화
        image = cv2.flip(image,-1)
        cv2.imshow( 'camera test' , image)
        if cv2.waitKey(1) == ord('q'):  #만약 q라는 키보드값을 읽으면 종료합니다.
            break
        
    cv2.destroyAllWindows() #이후 openCV창을 종료합니다.
    
if __name__ == '__main__':
    main()