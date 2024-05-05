import cv2
import mediapipe as mp
import time
import modulegesture as  mgt
import numpy as np
import math
from ctypes import cast, POINTER
from comtypes import CLSCTX_ALL
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume
import pyautogui
import sys
###################################
wcam, hcam = 640, 480 

cap = cv2.VideoCapture(0)
cap.set(3, wcam)
cap.set(4, hcam)
ptime = 0
dectector = mgt.handdetecter(detectionCon=1)
devices = AudioUtilities.GetSpeakers()
interface = devices.Activate(
    IAudioEndpointVolume._iid_, CLSCTX_ALL, None)

volume = cast(interface, POINTER(IAudioEndpointVolume))



#volume.GetMute()
#volume.GetMasterVolumeLevel()
volrange = volume.GetVolumeRange()

minvol = volrange[0]
maxvol = volrange[1]


#(-63.5, 0.0, 0.5)
def wait():
    time.sleep(1)
    main()

def main():
  while True:
    success, img = cap.read()
    img  = dectector.FindHands(img)
    lmList = dectector.findPosition(img, draw=False)
    lmList2 = dectector.findPosition2(img,draw=False)
    if len(lmList) != 0:
     #print(lmList[4], lmList[8])
     x1, y1 =lmList[4][1], lmList[4][2]
     x2, y2 =lmList[8][1], lmList[8][2]
 

     length = math.hypot(x2 - x1, y2 - y1)
    
    # print(length)

     # hand range 200 -  20
     # vol range -63 - 0  
     #vol = np.interp(length,[50,100], [minvol,maxvol])
     #print(vol)
     #volume.SetMasterVolumeLevel(vol, None)
     
     if length < 20:
         print("ok")
         
         pyautogui.keyDown("win")
         pyautogui.press("d")
         time.sleep(1)
         
         pyautogui.keyUp("win")
         
     elif length < 150:
         print("okok")
         
         pyautogui.keyDown("alt")
         pyautogui.press("tab")
         time.sleep(1)
         pyautogui.keyUp("alt")
         


         
    if len(lmList2) != 0:
           x4, y4 =lmList2[4][1], lmList2[4][2]
           x3, y3 =lmList2[8][1], lmList2[8][2]
           length2 = math.hypot(x3 - x4, y3 - y4) 


           if length2 < 20:
            sys.exit()



     
          

  #  ctime = time.time()
  #  fps = 1/(ctime-ptime)
  #  ptime = ctime
  #  cv2.putText(img,f'fps:{int(fps)}',(570,470), cv2.FONT_HERSHEY_PLAIN,1, (0,0,0), 1)
    
   # cv2.imshow("img", img)
    #cv2.waitKey(1)
if __name__ == "__main__":
     main()
 
