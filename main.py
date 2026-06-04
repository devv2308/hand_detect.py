import cv2
import time 
import mediapipe as mp 
from mediapipe.tasks import python 
from mediapipe.tasks.python import vision
#─── Hand Detection Setup ───────────────────────────────────────
mp_hands = mp.tasks.vision.HandLandmarker 
mp_base = mp.tasks.BaseOptions 
mp_vision = mp.tasks.vision

HAND_CONNECTIONS = [ (0,1),(1,2),(2,3),(3,4), (0,5),(5,6),(6,7),(7,8), (0,9),(9,10),(10,11),(11,12), (0,13),(13,14),(14,15),(15,16), (0,17),(17,18),(18,19),(19,20), (5,9),(9,13),(13,17) ]

hand_options = mp_vision.HandLandmarkerOptions( base_options=mp_base(model_asset_path="hand_landmarker.task"), num_hands=2 )
hand_detector = mp_hands.create_from_options(hand_options)


#─── Camera & FPS ────────────────────────────────────────────────
cap = cv2.VideoCapture(0)
pTime = 0

while True:
    ret, frame = cap.read()
    if not ret:
        break

    frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    mp_image = mp.Image(image_format=mp.ImageFormat.SRGB, data=frame_rgb)

    # ─── Hand Detection ──────────────────────────────────────────
    hand_result = hand_detector.detect(mp_image)

    if hand_result.hand_landmarks:
        for hand_landmarks in hand_result.hand_landmarks:
            h, w, _ = frame.shape

            # Draw landmarks
            for point in hand_landmarks:
                cx, cy = int(point.x * w), int(point.y * h)
                cv2.circle(frame, (cx, cy), 4, (0, 255, 0), -1)

            # Draw connections
            for start_idx, end_idx in HAND_CONNECTIONS:
                start = hand_landmarks[start_idx]
                end = hand_landmarks[end_idx]
                cv2.line(frame,
                         (int(start.x * w), int(start.y * h)),
                         (int(end.x * w), int(end.y * h)),
                         (0, 0, 255), 2)



    # ─── FPS ─────────────────────────────────────────────────────
    cTime = time.time()
    fps = 1 / (cTime - pTime) if (cTime - pTime) != 0 else 0
    pTime = cTime
    cv2.putText(frame, f'FPS:{int(fps)}', (20, 70),
                cv2.FONT_HERSHEY_PLAIN, 3, (255, 0, 0), 2)

    cv2.imshow("Face + Hand Detection", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()