import cv2
import cv2 as cv


def nothing():
    pass

def create_trackbars():
    cv.namedWindow('result')
    cv.createTrackBar('min 1', 'result', 0, 255, nothing)
    cv.createTrackBar('min 2', 'result', 0, 255, nothing)
    cv.createTrackBar('min 3', 'result', 0, 255, nothing)
    cv.createTrackBar('max 1', 'result', 0, 255, nothing)
    cv.createTrackBar('max 2', 'result', 0, 255, nothing)
    cv.createTrackBar('max 3', 'result', 0, 255, nothing)

def main(type='video', src=0, format='bgr'):
    if type == 'video':
        cap = cv2.VideoCapture(src)
        while True:
            ret, frame = cap.read()
            if ret:
                if format == 'hsv':
                    frame = cv.cvtColor(frame, cv.COLOR_BGR2HSV)
                elif format == 'lab':
                    frame = cv.cvtColor(frame, cv.COLOR_BGR2LAB)
                elif format == 'rgb':
                    frame = cv.cvtColor(frame, cv.COLOR_BGR2RGB)

                min1 = cv.getTrackbarPos('min 1', 'result')
                min2 = cv.getTrackbarPos('min 2', 'result')
                min3 = cv.getTrackbarPos('min 3', 'result')
                max1 = cv.getTrackbarPos('max 1', 'result')
                max2 = cv.getTrackbarPos('max 2', 'result')
                max3 = cv.getTrackbarPos('max 3', 'result')
                mask = cv.inRange(frame, (min1, min2, min3), (max1, max2, max3))
                corrected_frame = cv.bitwise_and(frame, frame, mask=mask)
                cv.imshow('result', corrected_frame)

                if cv.waitKey(1) == 0xFF:
                    break
                    cap.release()
                    cv.destroyAllWindows()

    elif type == 'image':
        frame = cv.imread(src)
        if format == 'hsv':
            frame = cv.cvtColor(frame, cv.COLOR_BGR2HSV)
        elif format == 'lab':
            frame = cv.cvtColor(frame, cv.COLOR_BGR2LAB)
        elif format == 'rgb':
            frame = cv.cvtColor(frame, cv.COLOR_BGR2RGB)
        while True:
            min1 = cv.getTrackbarPos('min 1', 'result')
            min2 = cv.getTrackbarPos('min 2', 'result')
            min3 = cv.getTrackbarPos('min 3', 'result')
            max1 = cv.getTrackbarPos('max 1', 'result')
            max2 = cv.getTrackbarPos('max 2', 'result')
            max3 = cv.getTrackbarPos('max 3', 'result')
            mask = cv.inRange(frame, (min1, min2, min3), (max1, max2, max3))
            corrected_frame = cv.bitwise_and(frame, frame, mask=mask)
            cv.imshow('result', corrected_frame)

            if cv.waitKey(1) == 0xFF:
                break



if __name__ == "__main__":
    # type - input type (by default - video, you can choose 'image')
    # src - video file path (by default 0 - webcam),
    # format - video format (by default 'bgr', you can choose 'rgb', 'hsv', 'lab')
    main()