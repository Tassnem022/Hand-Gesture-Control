
# Hand Gesture Controlled System 🖐️💻

A real-time hand gesture control system using **MediaPipe**, **OpenCV**, and **PyAutoGUI** that lets you:
- Control mouse with your index finger
- Control volume by pinching (thumb + index)

## 🛠️ Requirements

Install dependencies:
```bash
pip install mediapipe opencv-python pyautogui numpy
```

## 🚀 How It Works

- MediaPipe detects 21 hand landmarks.
- Index finger controls cursor.
- Distance between thumb and index controls volume.

## 🎮 Gestures

| Gesture             | Action        |
|---------------------|---------------|
| Move Index Finger   | Move Cursor   |
| Thumb & Index Close | Volume Down   |
| Thumb & Index Wide  | Volume Up     |

## ▶️ Run It

```bash
python hand_gesture_control.py
```

Press `Q` to quit.

## 📁 Structure

```
HandGestureControl/
├── hand_gesture_control.py
├── README.md
├── utils/
└── images/
```
