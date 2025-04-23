
import cv2
import mediapipe as mp
import numpy as np
import pyautogui
import math

mp_hands = mp.solutions.hands
hands = mp_hands.Hands(max_num_hands=1)
mp_draw = mp.solutions.drawing_utils

cap = cv2.VideoCapture(0)
screen_w, screen_h = pyautogui.size()

def calc_distance(p1, p2):
    return math.hypot(p2[0]-p1[0], p2[1]-p1[1])

while True:
    success, frame = cap.read()
    frame = cv2.flip(frame, 1)
    h, w, _ = frame.shape
    rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    results = hands.process(rgb)
    if results.multi_hand_landmarks:
        for hand_landmark in results.multi_hand_landmarks:
            lm_list = []
            for id, lm in enumerate(hand_landmark.landmark):
                cx, cy = int(lm.x * w), int(lm.y * h)
                lm_list.append((cx, cy))

            mp_draw.draw_landmarks(frame, hand_landmark, mp_hands.HAND_CONNECTIONS)

            index_finger = lm_list[8]
            #pyautogui.moveTo(index_finger[0] * screen_w // w, index_finger[1] * screen_h // h)

            thumb_tip = lm_list[4]
            dist = calc_distance(index_finger, thumb_tip)
            cv2.line(frame, index_finger, thumb_tip, (0, 255, 0), 2)
            cv2.circle(frame, thumb_tip, 10, (255, 0, 0), -1)
            cv2.circle(frame, index_finger, 10, (255, 0, 0), -1)

            if dist < 30:
                cv2.putText(frame, 'Volume Down', (10, 70), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)
                pyautogui.press("volumedown")
            elif dist > 100:
                cv2.putText(frame, 'Volume Up', (10, 70), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
                pyautogui.press("volumeup")

    cv2.imshow("Hand Control", frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
