import numpy as np
import pyautogui, cv2 

resolution = tuple(pyautogui.size())

codec = cv2.VideoWriter_fourcc(*"XVID")
filename = "rec.avi"
fps = 11

output = cv2.VideoWriter(filename, codec, fps, (resolution))

while True:
    img = pyautogui.screenshot()
    frame = np.array(img)
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    output.write(frame)

    if cv2.waitKey(1) == ord('q'):
        break

output.release()
cv2.destroyAllWindows()