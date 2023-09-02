import os
import sys
import ctypes
import cv2
import json
import math
import mss
import numpy as np
import time
import torch
import uuid
import win32api
import os.path
import win32con
import winsound
import _thread
from pynput import keyboard
from termcolor import colored
import win32api, win32con, win32gui, win32ui
import tkinter
import customtkinter

class GUI(customtkinter.CTk):


    def __init__(self):
        super().__init__()

        self.geometry("700x500")
        self.title("Steam | Close with [delete]")
        customtkinter.set_appearance_mode("dark")
        self.resizable(False, False)



        ############### AIMBOT FRAME & GUI ELEMENTS ###########
        global enable_var
        enable_var = customtkinter.StringVar(value="off")
        global autoshoot_var
        autoshoot_var = customtkinter.StringVar(value="on")
        global togglebox_var
        togglebox_var = customtkinter.StringVar(value="SHIFT")

        aimbot_frame = customtkinter.CTkFrame(master=self,width=200,height=400)
        aimbot_frame.pack(pady=20, padx=40, fill="both", expand=True)
        aimbot_label = customtkinter.CTkLabel(master=aimbot_frame, justify=tkinter.LEFT, text="Aimbot")
        aimbot_label.pack(pady=12, padx=10)

        global aimbot_checkbox
        aimbot_checkbox = customtkinter.CTkCheckBox(master=aimbot_frame, text="Enable [F1]", command=Aimbot.update_status_aimbot,variable=enable_var, onvalue="on", offvalue="off")
        aimbot_checkbox.place(x=10, y=50)

        global ashoot_switch
        ashoot_switch = customtkinter.CTkSwitch(master=aimbot_frame, text="Autoshoot",variable=autoshoot_var, onvalue="on", offvalue="off")
        ashoot_switch.place(x=10, y=100)                          

        smooth_label = customtkinter.CTkLabel(master=aimbot_frame,text="Smooth")
        smooth_label.place(x=40, y=130)



        global smooth_slider
        smooth_slider = customtkinter.CTkSlider(master=aimbot_frame, from_=1, to=4,number_of_steps=4)
        smooth_slider.place(x=10, y=160)


        global togglebox
        togglebox = customtkinter.CTkOptionMenu(master=aimbot_frame,values=["SHIFT", "ALT","CTRL","MOUSE5","RIGHT MOUSE","LEFT MOUSE"],variable=togglebox_var)
        togglebox.place(x=450,y=50)

        

        ############### MISC FRAME & GUI ELEMENTS ###########
        global sound_feedback_var
        global debug_frame_var
        sound_feedback_var = customtkinter.StringVar(value="on")
        debug_frame_var = customtkinter.StringVar(value="on")

        misc_frame = customtkinter.CTkFrame(master=self,width=200,height=100)
        misc_frame.pack(pady=20, padx=40, fill="both", expand=True)

        misc_label = customtkinter.CTkLabel(master=misc_frame, justify=tkinter.LEFT, text="Misc")
        misc_label.pack(pady=12, padx=10)  

        global sound_feedback_switch
        sound_feedback_switch = customtkinter.CTkSwitch(master=misc_frame, text="Sound-Feedback",variable=sound_feedback_var, onvalue="on", offvalue="off")
        sound_feedback_switch.place(x=10,y=50)
        
        global debug_frame_switch
        debug_frame_switch = customtkinter.CTkSwitch(master=misc_frame, text="Debug-Frame",variable=debug_frame_var, onvalue="on", offvalue="off",command=GUI.debugframe_callback)
        debug_frame_switch.place(x=10,y=100)

        ############### OUTSIDE FRAME & CONFIG GUI ELEMENTS ###########
        save_conf_button = customtkinter.CTkButton(master=self, text="Save Config", command=GUI.save_config_callback)
        save_conf_button.place(x=195,y=430)
        load_conf_button = customtkinter.CTkButton(master=self, text="Load Config", command=GUI.load_config_callback)
        load_conf_button.place(x=365,y=430)

    def reconfigure_sens_button_callback():
        Setup.sens_configuration()
    def save_config_callback():
        Setup.safe_config()
    def load_config_callback():
        Setup.load_config("full")
    def debugframe_callback():
        hwndFrame = win32gui.FindWindow(None, "Debug Frame") # gets Debug Frame window title
        if win32gui.IsWindowVisible(hwndFrame):
            win32gui.ShowWindow(hwndFrame, win32con.SW_HIDE)
        else:
            win32gui.ShowWindow(hwndFrame, win32con.SW_RESTORE) #restoring the windows back to the top
            win32gui.SetWindowPos(hwndFrame,win32con.HWND_NOTOPMOST, 0, 0, 0, 0, win32con.SWP_NOMOVE + win32con.SWP_NOSIZE)  
            win32gui.SetWindowPos(hwndFrame,win32con.HWND_TOPMOST, 0, 0, 0, 0, win32con.SWP_NOMOVE + win32con.SWP_NOSIZE)  
            win32gui.SetWindowPos(hwndFrame,win32con.HWND_NOTOPMOST, 0, 0, 0, 0, win32con.SWP_SHOWWINDOW + win32con.SWP_NOMOVE + win32con.SWP_NOSIZE)


class Misc:
    def on_release(key):
        try:
            if key == keyboard.Key.f1:
                
                if Aimbot.is_aimbot_enabled():
                    aimbot_checkbox.deselect()
                else:
                    aimbot_checkbox.select()
            if key == keyboard.Key.delete:
                Aimbot.clean_up()
            if key == keyboard.Key.insert: #gui toggle with insert aka gui disapears and reaprears
                hwndGui = win32gui.FindWindow(None, "Steam | Close with [delete]") # gets gui window title
                if win32gui.IsWindowVisible(hwndGui): #checks if gui is visible
                    win32gui.ShowWindow(hwndGui, win32con.SW_HIDE)
                else:
                    win32gui.ShowWindow(hwndGui, win32con.SW_RESTORE) #restoring the windows back to the top
                    win32gui.SetWindowPos(hwndGui,win32con.HWND_NOTOPMOST, 0, 0, 0, 0, win32con.SWP_NOMOVE + win32con.SWP_NOSIZE)  
                    win32gui.SetWindowPos(hwndGui,win32con.HWND_TOPMOST, 0, 0, 0, 0, win32con.SWP_NOMOVE + win32con.SWP_NOSIZE)  
                    win32gui.SetWindowPos(hwndGui,win32con.HWND_NOTOPMOST, 0, 0, 0, 0, win32con.SWP_SHOWWINDOW + win32con.SWP_NOMOVE + win32con.SWP_NOSIZE)
                    print("try")
                print(hwndGui)
        except NameError:
            pass
    def inputToKeycode(toggle_choice): # gets the keycode to the wished key by the user
        if toggle_choice =="ALT":
            keycode = int(0x12)
        elif toggle_choice =="SHIFT":
            keycode = int(0x10)
        elif toggle_choice == "RIGHT MOUSE":            
            keycode = int(0x02)
        elif toggle_choice == "MOUSE5":
            keycode = int(0x06)
        elif toggle_choice == "LEFT MOUSE":
            keycode = int(0x01)
        elif toggle_choice == "CTRL":
            keycode = int(0x11)
        return keycode        
    def get_sound_feedback_status():
        try:
            sound_feedback = sound_feedback_var.get()
            if sound_feedback_var.get() == "on":
                return True
        except:
            return False

    def hide_console():
        kernel32 = ctypes.WinDLL('kernel32')
        user32 = ctypes.WinDLL('user32')
        SW_HIDE = 0
        hWnd = kernel32.GetConsoleWindow()
        user32.ShowWindow(hWnd, SW_HIDE)

class Setup:
    def prompt(str):
        valid_input = False
        while not valid_input:
            try:
                number = float(input(str))
                valid_input = True
            except ValueError:
                print("INVALID INPUT... only enter the number (for example: 6.9)")
        return number
    def sens_configuration():
        print("Plese enter your ingame-sensitivty settings...")
        print("If these prompts confuse you please check our #help channel :)")       
        xy_sens = Setup.prompt("Enter your X and Y sensitivty(X and Y have to be the same):")
        targeting_sens = Setup.prompt("Enter your ADS sensitivity:")
        global config
        config = {"xy_scale": 10/xy_sens, "targeting_scale": 1000/(targeting_sens * xy_sens)} #adding xy_scale and targeting_scale to a list but not to a json file yet
        with open('config.json', 'w') as outfile:
            json.dump(config, outfile)
    def safe_config():
        # first adding the configurations made in the UI
        config["autoshoot"] = autoshoot_var.get()
        config["toggle"] = togglebox_var.get()
        config["pixel_increment"] = smooth_slider.get()
        config["sound_feedback"] = sound_feedback_var.get()
        config["debug_frame"] = debug_frame_var.get()
        # then saving the whole whole dictonary including the targeting_scales to a file
        with open('config.json', 'w') as outfile:
            json.dump(config, outfile)
    def load_config(part):
        # loading the saved config and reading it as a dict but only the scales for the sens because gui hasnt loaded yet
        with open('config.json') as json_file:
            global config
            config = json.load(json_file)
        if part == "sens":
            pass
        # loading the rest of the config on button press of load config
        elif part == "full":
            if config["autoshoot"] == "on":
                ashoot_switch.select()
            else:
                ashoot_switch.deselect()
            if config["sound_feedback"] == "on":
                sound_feedback_switch.select()
            else:
                sound_feedback_switch.deselect()
            if config["debug_frame"] == "on":
                debug_frame_switch.select()
            else:
                debug_frame_switch.deselect()
            smooth_slider.set(config["pixel_increment"])
            togglebox.set(config["toggle"])



class Aimbot:
    rightShift = 90
    soundFeedback = True
    display_debug_window = True

    screen = mss.mss()
    aimbot_status = colored("ENABLED", 'green')
    def __init__(self, box_constant = 400, collect_data = False, mouse_delay = 0.00009, debug = False): # mouse_delay can be between 0.00008-0.0001 the lower it gets the snappier but also the less fps for the neural network
        #controls the initial centered box width and height of the "Vision" window
        self.box_constant = box_constant #controls the size of the detection box (equaling the width and height)

        print("[INFO] Loading the neural network model")
        self.model = torch.hub.load('ultralytics/yolov5', 'custom', path='best.pt', force_reload=True)
        if torch.cuda.is_available():
            print(colored("CUDA ACCELERATION [ENABLED]", "green"))
        else:
            print(colored("[!] CUDA ACCELERATION IS UNAVAILABLE", "red"))
            print(colored("[!] Check your PyTorch installation, else performance will be poor", "red"))




        self.model.conf = 0.7 # 0.6 base confidence threshold (or base detection (0-1) # changed this to 0.6 bcs it seems to reduce false detecionts a little
        self.model.iou = 0.45 # NMS IoU (0-1)
        self.collect_data = collect_data
        self.mouse_delay = mouse_delay
        self.debug = debug

        print("\n[INFO] PRESS 'F1' TO TOGGLE AIMBOT\n[INFO] PRESS 'F2' TO QUIT")
    def sleep(duration, get_now = time.perf_counter):
        if duration == 0: return
        now = get_now()
        end = now + duration
        while now < end:
            now = get_now()
    def is_targeted():
        return True if win32api.GetKeyState(Misc.inputToKeycode(togglebox_var.get())) in (-127, -128) else False

    def update_status_aimbot():
        if Aimbot.aimbot_status == colored("ENABLED", 'green'):
            Aimbot.aimbot_status = colored("DISABLED", 'red')
            if Misc.get_sound_feedback_status():
                duration = 100  # milliseconds
                freq = 150  # Hz
                winsound.Beep(freq, duration)
        else:
            if Misc.get_sound_feedback_status():
                duration = 100  # milliseconds
                freq = 540  # Hz
                winsound.Beep(freq, duration) 
            Aimbot.aimbot_status = colored("ENABLED", 'green')
        sys.stdout.write("\033[K")
        print(f"[!] AIMBOT IS [{Aimbot.aimbot_status}]", end = "\r")

    def right_click(): #checks if the right mousebuttoon is held
        return True if win32api.GetKeyState(0x02) in (-127, -128) else False 
    def autoshoot():
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)
        print("1")   

    def is_aimbot_enabled():
        return True if Aimbot.aimbot_status == colored("ENABLED", 'green') else False

    def is_target_locked(x, y):
        #plus/minus 5 pixel threshold
        threshold = 7
        return True if 960 - threshold <= x <= 960 + threshold and 540 - threshold <= y <= 540 + threshold else False

    def move_crosshair(self, x, y):
        if Aimbot.is_target_locked(x, y): # check if movement is really necessary because if it is allready locked then the crosshair allready is on top of a player
            print("allready locked")
        else:
            if Aimbot.is_targeted() and Aimbot.right_click():   # checks if right clicked and adjusts to targeting sens by loading the targeting scale from the config
                scale = config["targeting_scale"]
            elif Aimbot.is_targeted(): #if hipfiring a diffrent scale method is used to gurantee fastest movement
                scale = config["xy_scale"]
            else:
                return #TODO

            #now actually move the mouse there
            for rel_x, rel_y in Aimbot.interpolate_coordinates_from_center((x, y), scale):
                win32api.mouse_event(win32con.MOUSEEVENTF_MOVE, int(rel_x), int(rel_y), 0, 0) # second mouse movement method seems alot more stable and less flickery
                if not self.debug: Aimbot.sleep(self.mouse_delay) #time.sleep is not accurate enough
            

    def interpolate_coordinates_from_center(absolute_coordinates, scale):
        pixel_increment = smooth_slider.get()
        diff_x = (absolute_coordinates[0] - 960) * scale/pixel_increment
        diff_y = (absolute_coordinates[1] - 540) * scale/pixel_increment
        length = int(math.dist((0,0), (diff_x, diff_y)))
        if length == 0: return
        unit_x = (diff_x/length) * pixel_increment
        unit_y = (diff_y/length) * pixel_increment
        x = y = sum_x = sum_y = 0
        for k in range(0, length):
            sum_x += x
            sum_y += y
            x, y = round(unit_x * k - sum_x), round(unit_y * k - sum_y)
            yield x, y


    def start(self):
        print("[INFO] Beginning screen capture")
        Aimbot.update_status_aimbot()
        half_screen_width = ctypes.windll.user32.GetSystemMetrics(0)/2 #this should always be 960
        half_screen_height = ctypes.windll.user32.GetSystemMetrics(1)/2 #this should always be 540
        detection_box = {'left': int (Aimbot.rightShift + (half_screen_width - self.box_constant/2)), #x1 coord (for top-left corner of the box)
                          'top': int(half_screen_height - self.box_constant/2), #y1 coord (for top-left corner of the box)
                          'width': int(self.box_constant),  #width of the box
                          'height': int(self.box_constant)} #height of the box
        if self.collect_data:
            collect_pause = 0

        while True:
            start_time = time.perf_counter()
            frame = np.array(Aimbot.screen.grab(detection_box))
            if self.collect_data: orig_frame = np.copy((frame))
            results = self.model(frame)
            if len(results.xyxy[0]) != 0: #player detected
                least_crosshair_dist = closest_detection = player_in_frame = False
                for *box, conf, cls in results.xyxy[0]: #iterate over each player detected
                    x1y1 = [int(x.item()) for x in box[:2]]
                    x2y2 = [int(x.item()) for x in box[2:]]
                    x1, y1, x2, y2, conf = *x1y1, *x2y2, conf.item()
                    height = y2 - y1
                    relative_head_X, relative_head_Y = int((x1 + x2)/2), int((y1 + y2)/2 - height/2.7) #offset to roughly approximate the head using a ratio of the height
                    own_player = x1 < 5 #or (x1 < self.box_constant/5 and y2 > self.box_constant/1.2)
                    if Aimbot.right_click() == True:
                        own_player = x1 < 0  #if right click is held and the playermodel is adsing the own player is not in the frame so it dosent need to be filtered out 
                    else:
                        own_player = x1 < 5 # or (x1 < self.box_constant/5 and y2 > self.box_constant/1.2) #helps ensure that your own player is not regarded as a valid detection
                    #calculate the distance between each detection and the crosshair at (self.box_constant/2, self.box_constant/2)
                    crosshair_dist = math.dist((relative_head_X, relative_head_Y), (self.box_constant/2, self.box_constant/2))

                    if not least_crosshair_dist: least_crosshair_dist = crosshair_dist #initalize least crosshair distance variable first iteration

                    if crosshair_dist <= least_crosshair_dist and not own_player:
                        least_crosshair_dist = crosshair_dist
                        closest_detection = {"x1y1": x1y1, "x2y2": x2y2, "relative_head_X": relative_head_X, "relative_head_Y": relative_head_Y, "conf": conf}

                    if not own_player:
                        cv2.rectangle(frame, x1y1, x2y2, (207, 17, 17), 2) #draw the bounding boxes for all of the player detections (except own)
                        cv2.putText(frame, f"{int(conf * 100)}%", x1y1, cv2.FONT_HERSHEY_DUPLEX, 0.5, (244, 115, 115), 2) #draw the confidence labels on the bounding boxes
                    else:
                        own_player = False
                        if not player_in_frame:
                            player_in_frame = True

                if closest_detection: #if valid detection exists
                    cv2.circle(frame, (closest_detection["relative_head_X"], closest_detection["relative_head_Y"]), 2, (207, 17, 17), -1) #draw circle on the head

                    #draw line from the crosshair to the head
                    cv2.line(frame, (closest_detection["relative_head_X"], closest_detection["relative_head_Y"]), (self.box_constant//2, self.box_constant//2), (100, 100, 100), 2)

                    absolute_head_X, absolute_head_Y = closest_detection["relative_head_X"] + detection_box['left'], closest_detection["relative_head_Y"] + detection_box['top']

                    x1, y1 = closest_detection["x1y1"]
                    if Aimbot.is_target_locked(absolute_head_X, absolute_head_Y) and autoshoot_var.get() == "on":
                        _thread.start_new_thread( Aimbot.autoshoot, () ) # starting this in new thread for better performance 
                        cv2.putText(frame, "LOCKED", (x1 + 40, y1), cv2.FONT_HERSHEY_DUPLEX, 0.5, (149, 255, 0), 1) #draw the confidence labels on the bounding boxes
                    elif Aimbot.is_target_locked(absolute_head_X, absolute_head_Y):
                        cv2.putText(frame, "LOCKED", (x1 + 40, y1), cv2.FONT_HERSHEY_DUPLEX, 0.5, (149, 255, 0), 1) #draw the confidence labels on the bounding boxes
                    else:
                        cv2.putText(frame, "TARGETING", (x1 + 40, y1), cv2.FONT_HERSHEY_DUPLEX, 0.5, (45, 6, 128), 1) #draw the confidence labels on the bounding boxes

                    if Aimbot.is_aimbot_enabled():
                        Aimbot.move_crosshair(self, absolute_head_X, absolute_head_Y)

            if self.collect_data and time.perf_counter() - collect_pause > 1 and Aimbot.is_targeted() and Aimbot.is_aimbot_enabled() and not player_in_frame: #screenshots can only be taken every 1 second
                cv2.imwrite(f"lib/data/{str(uuid.uuid4())}.jpg", orig_frame)
                collect_pause = time.perf_counter()
            
            cv2.putText(frame, f"CPS: {int(1/(time.perf_counter() - start_time))}", (5, 390), cv2.FONT_ITALIC, 1, (255, 255, 255), 4)
            cv2.imshow("Debug Frame", frame)
            if cv2.waitKey(1) & 0xFF == ord('0'):
                break

    def clean_up():
        print("\n[INFO] F2 WAS PRESSED. QUITTING...")
        Aimbot.screen.close()
        os._exit(0)

if __name__ == "__main__":
   # if "0YpG3$A17lB#CgMy" in sys.argv: #checking for password this check just incase this program is going to be distributed in a closed source scenario
        # checking if config can be loaded or needs to be created
        if os.path.exists("config.json"):
            i = input("Reconfigure sens? (yes/no): ")
            if i == "yes":
                Setup.sens_configuration()
            else:
                pass
        else:
            Setup.sens_configuration()
            
            
        Setup.load_config("sens") #load the sens part of the config


        Misc.hide_console()
        ##### STARTING GUI, AIMBOT AND KEYBOARD LISTENER####
        listener = keyboard.Listener(on_release=Misc.on_release)
        listener.start()
        start = Aimbot()
        _thread.start_new_thread(start.start,())
        gui = GUI()
        gui.mainloop()
  #  else:  #wrong password or none
       # exit()
