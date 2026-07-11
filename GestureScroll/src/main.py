from camera import Camera
from gesture_controller import GestureController
from scroll_controller import ScrollController


def main():

    camera = Camera()
    gesture = GestureController()
    scroll = ScrollController()


    print("Gesture mode started...")
    print("👍 Thumb Up  = Scroll Up")
    print("✌️ Peace Sign = Scroll Down")
    print("✊ Closed Fist = Do Nothing")
    print("Press Q to quit")


    while True:

        frame = camera.get_frame()


        if frame is None:
            continue


        action = gesture.detect(frame)


        if action:
            print(action)
            scroll.execute(action)

        else:
            scroll.reset()



        if camera.quit_pressed():
            break



    camera.release()



if __name__ == "__main__":
    main()