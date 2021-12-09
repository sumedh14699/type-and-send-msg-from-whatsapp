#import emoji
import keyboard
from pykeyboard import PyKeyboard
#import cv2
k = PyKeyboard()
 
while True:
 if keyboard.is_pressed('e'):         
  while True:
        
        k.type_string('harmonium....')
        
        k.tap_key(k.enter_key)
        
        if keyboard.is_pressed('q'):
             break
 
 elif keyboard.is_pressed('t'):
             break
