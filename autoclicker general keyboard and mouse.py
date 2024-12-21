## AUTO-CLICKER

# importing time and threading
import time
import threading
import pyautogui
# pynput.keyboard is used to watch events of keyboard for start and stop of auto-clicker
from pynput.mouse import Button, Controller
from pynput.keyboard import Listener, KeyCode

# four variables are created to control the auto-clicker
delay = 1
button = Button.left
start_stop_key = KeyCode(char='a')
stop_key = KeyCode(char='b')
 
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
                # New Game button + sufficient search time
                pyautogui.moveTo(1168, 715)
                mouse.click(self.button)
                time.sleep(8)
                if not self.running:  # Check for stop signal after each action
                    break
                    
                # (pre-)move the rook pawn + wait for opponent to make his move
                pyautogui.moveTo(948, 828)
                mouse.click(self.button)
                time.sleep(0.5)
                if not self.running:  # Check for stop signal after each action
                    break
                
                pyautogui.moveTo(948, 625)
                mouse.click(self.button)
                time.sleep(2)
                if not self.running:  # Check for stop signal after each action
                    break
                
                # resign button + confirm
                pyautogui.moveTo(1167, 780)
                mouse.click(self.button)
                time.sleep(1)
                if not self.running:  # Check for stop signal after each action
                    break
                
                pyautogui.moveTo(1166, 727)
                mouse.click(self.button)
                time.sleep(2)
                if not self.running:  # Check for stop signal after each action
                    break

                # Close "Game Resigned" Prompt
                pyautogui.moveTo(745, 466)
                mouse.click(self.button)
                time.sleep(2)
                if not self.running:  # Check for stop signal after each action
                    break    

                #---------------------------------
                
                # New Game button + sufficient search time
                pyautogui.moveTo(1168, 715)
                mouse.click(self.button)
                time.sleep(8)
                if not self.running:  # Check for stop signal after each action
                    break
                    
                # (pre-)move the rook pawn + wait for opponent to make his move
                pyautogui.moveTo(271, 828)
                mouse.click(self.button)
                time.sleep(0.5)
                if not self.running:  # Check for stop signal after each action
                    break
                
                pyautogui.moveTo(271, 625)
                mouse.click(self.button)
                time.sleep(2)
                if not self.running:  # Check for stop signal after each action
                    break
                
                # resign button + confirm
                pyautogui.moveTo(1167, 780)
                mouse.click(self.button)
                time.sleep(1)
                if not self.running:  # Check for stop signal after each action
                    break
                
                pyautogui.moveTo(1166, 727)
                mouse.click(self.button)
                time.sleep(2)
                if not self.running:  # Check for stop signal after each action
                    break

                # Close "Game Resigned" Prompt
                pyautogui.moveTo(745, 466)
                mouse.click(self.button)
                time.sleep(2)
                if not self.running:  # Check for stop signal after each action
                    break          

            
            time.sleep(0.1)

# ChatGPT condensed code
# def run(self):
#     actions = [
#         ((1336, 727), 7),  # New Game button + sufficient search time
#         ((1108, 834), 0.5),  # (pre-)move the rook pawn + wait for opponent to make his move
#         ((1108, 621), 2),  # (pre-)move the rook pawn + wait for opponent to make his move
#         ((1340, 784), 0.5),  # resign button + confirm
#         ((1340, 727), 1)  # resign button + confirm
#     ]
    
#     while self.program_running:
#         while self.running:
#             for action in actions:
#                 pyautogui.moveTo(action[0])
#                 mouse.click(self.button)
#                 time.sleep(action[1])
#                 if not self.running:  # Check for stop signal after each action
#                     break                
#         time.sleep(0.1)

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