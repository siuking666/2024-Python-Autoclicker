## AUTO-CLICKER for video clipping

# importing time and threading
import time
import threading
import pyautogui
import keyboard
# pynput.keyboard is used to watch events of keyboard for start and stop of auto-clicker
from pynput.mouse import Button, Controller
from pynput.keyboard import Listener, KeyCode

# four variables are created to control the auto-clicker
delay = 1
button = Button.left
start_stop_key = KeyCode(char='a')
stop_key = KeyCode(char='b')

episode = 1
end_episode = 1+7 # if the length is 10.5hrs, give 10

# threading.Thread is used to control clicks
class ClickMouse(threading.Thread):
   
  # delay and button is passed in class to check execution of auto-clicker
    def __init__(self, delay, button):
        super(ClickMouse, self).__init__()
        self.delay = delay
        self.button = button
        self.running = False
        self.program_running = True
 
    def start_clicking(self):
        self.running = True
 
    def stop_clicking(self):
        self.running = False
 
    def exit(self):
        self.stop_clicking()
        self.program_running = False
 
# method to check and run loop until it is true another loop will check if it is set to true or not, for mouse click it set to button and delay.

    def run(self):
        while self.program_running:
            while self.running:
                global episode
                global end_episode

                pyautogui.moveTo(181, 966) #set start marker A
                mouse.click(self.button)
                time.sleep(1)
                
                pyautogui.moveTo(45, 1003) #time
                mouse.click(self.button)
                time.sleep(1)
                keyboard.write(str(episode))
                time.sleep(1)
                pyautogui.moveTo(1029, 505) #add a few seconds
                mouse.click(self.button)
                time.sleep(1)
                pyautogui.moveTo(999, 551) #confirm timestamp
                mouse.click(self.button)
                time.sleep(1)
                
                pyautogui.moveTo(208, 964) #set end marker B
                mouse.click(self.button)
                time.sleep(1)
                
                pyautogui.moveTo(63, 59) #save video & give filename
                mouse.click(self.button)
                time.sleep(1)
                keyboard.write(str(episode))
                time.sleep(1)                
                pyautogui.moveTo(790, 531) #confirm save
                mouse.click(self.button)
                time.sleep(30)
                
                pyautogui.moveTo(1051, 567) #confirm encoding finished
                mouse.click(self.button)
                time.sleep(1)
             
                episode+=1
                if episode == end_episode:
                    pyautogui.moveTo(181, 966) #set start marker A
                    mouse.click(self.button)
                    time.sleep(1)
                
                    pyautogui.moveTo(333, 964) #go to end of video
                    mouse.click(self.button)
                    time.sleep(1)
                
                    pyautogui.moveTo(208, 964) #set end marker B
                    mouse.click(self.button)
                    time.sleep(1)
                
                    pyautogui.moveTo(63, 59) #save video & give filename
                    mouse.click(self.button)
                    time.sleep(1)
                    keyboard.write(str(episode))
                    time.sleep(1)                
                    pyautogui.moveTo(790, 531) #confirm save
                    mouse.click(self.button)
                    time.sleep(0.5)

                    time.sleep(30)
                    pyautogui.moveTo(1051, 567) #confirm encoding finished
                    mouse.click(self.button)
                    time.sleep(1)
                    
                    self.running = False
                    break
                    
                if not self.running:  # Check for stop signal after each action
                    break            
            time.sleep(0.1)

# instance of mouse controller is created
mouse = Controller()
click_thread = ClickMouse(delay, button)
click_thread.start()

# on_press method takes key as argument
def on_press(key):

  # start_stop_key will stop clicking if running flag is set to true
    if key == start_stop_key:
        if click_thread.running:
            click_thread.stop_clicking()
            print("paused")
        else:
            click_thread.start_clicking()
            print("started")
            
    # here exit method is called and when key is pressed it terminates auto clicker
    elif key == stop_key:
        click_thread.exit()
        listener.stop()
        print("stopped")
        
with Listener(on_press=on_press) as listener:
    listener.join()