#import emoji
import keyboard
from pykeyboard import PyKeyboard
#import cv2
k = PyKeyboard()
 
while True:
 if keyboard.is_pressed('e'):         
  while True:
    
 #if keyboard.is_pressed('l'):
        #k.tap_key('d')
        k.type_string('abba.... harmonium....')
      
        #k.tap_key(emoji.emojize(":grinning_face_with_big_eyes:"))
        #k.type_string(emoji.emojize(":grinning_face_with_big_eyes:"))
        k.tap_key(k.enter_key)
        
        if keyboard.is_pressed('q'):
             break
 
 elif keyboard.is_pressed('t'):
             break
