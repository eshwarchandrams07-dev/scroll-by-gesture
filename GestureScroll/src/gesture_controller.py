import cv2
import mediapipe as mp


class GestureController:

    def __init__(self):
        self.hands = mp.solutions.hands.Hands(
            max_num_hands=1,
            min_detection_confidence=0.8,
            min_tracking_confidence=0.8
        )

        self.last_gesture = None
        self.counter = 0
        self.required_frames = 5


    def detect(self, frame):

        rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        result = self.hands.process(rgb)

        gesture = None


        if result.multi_hand_landmarks:

            hand = result.multi_hand_landmarks[0]


            # Thumb points
            thumb_tip = hand.landmark[4]
            thumb_ip = hand.landmark[3]

            # Other fingers
            index_tip = hand.landmark[8]
            middle_tip = hand.landmark[12]
            ring_tip = hand.landmark[16]
            pinky_tip = hand.landmark[20]

            index_pip = hand.landmark[6]
            middle_pip = hand.landmark[10]
            ring_pip = hand.landmark[14]
            pinky_pip = hand.landmark[18]


            index_open = index_tip.y < index_pip.y
            middle_open = middle_tip.y < middle_pip.y
            ring_open = ring_tip.y < ring_pip.y
            pinky_open = pinky_tip.y < pinky_pip.y



            # ✊ Fist
            if not index_open and not middle_open and not ring_open and not pinky_open:
                return None



            # 👍 Thumb up (improved)
            if (
                thumb_tip.y < thumb_ip.y
                and not middle_open
                and not ring_open
                and not pinky_open
            ):
                gesture = "SCROLL UP"



            # ✌️ Peace sign
            elif (
                index_open
                and middle_open
                and not ring_open
                and not pinky_open
            ):
                gesture = "SCROLL DOWN"



        # Stability
        if gesture == self.last_gesture:
            self.counter += 1
        else:
            self.counter = 0


        self.last_gesture = gesture


        if self.counter >= self.required_frames:
            self.counter = 0
            return gesture


        return None