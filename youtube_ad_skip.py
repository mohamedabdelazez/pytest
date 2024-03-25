import pyautogui
import time

def click_skip_button():
    while True:
        try:
        
            skip_button_location = pyautogui.locateCenterOnScreen('D:\\my st\\suezuni\\HVAC\\my-hvac-software\\web\\skip.png', confidence=0.7)
            
         
            if skip_button_location:
                pyautogui.click(skip_button_location)
                print("clicked")
          
                time.sleep(1)
            else:
                print("retrying")
        except pyautogui.ImageNotFoundException:
          
            print("searching for the ad..")
            time.sleep(2)


click_skip_button()
