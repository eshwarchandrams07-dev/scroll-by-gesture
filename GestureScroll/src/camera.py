import cv2


class Camera:

    def __init__(self):
        self.cap = cv2.VideoCapture(0)


    def get_frame(self):
        ret, frame = self.cap.read()

        if ret:
            return frame

        return None


    def quit_pressed(self):
        return cv2.waitKey(1) & 0xFF == ord('q')


    def release(self):
        self.cap.release()
        cv2.destroyAllWindows()