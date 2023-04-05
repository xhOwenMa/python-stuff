import numpy as np
import pyautogui, cv2, keyboard

resolution = tuple(pyautogui.size())

codec = cv2.VideoWriter_fourcc(*"XVID")
filename = "rec.avi"
fps = 11

output = cv2.VideoWriter(filename, codec, fps, (resolution))

# cv2.namedWindow('video', cv2.WINDOW_NORMAL)
# cv2.resizeWindow('video', 640, 480)

while True:
    img = pyautogui.screenshot()
    frame = np.array(img)
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    output.write(frame)

    # cv2.imshow('video', frame)
    if keyboard.is_pressed('q'):
        break

output.release()
cv2.destroyAllWindows()