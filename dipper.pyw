# Import Modules
import vgamepad as vg
import hid
import customtkinter as ctk
from threading import Thread
import sys
import os

# Function to get path for the icon
def resource_path(relative_path):
    # get abs path to resource
    base_path = getattr(sys, '_MEIPASS', os.path.dirname(os.path.abspath(__file__)))
    return os.path.join(base_path, relative_path)

class Mask:
     
    # Frets | 46 / 47
    FRET_1 = 0b00000001  # Green
    FRET_2 = 0b00000010  # Red
    FRET_3 = 0b00000100  # Yellow
    FRET_4 = 0b00001000  # Blue
    FRET_5 = 0b00010000  # Orange

    # DPad | 5
    DPAD_U = 0b00000000  # Up    / North
    DPAD_D = 0b00000100  # Down  / South
    DPAD_L = 0b00000110  # Left  / West
    DPAD_R = 0b00000010  # Right / East

    # System | 6, to 7
    STICK  = 0b01000000  # Joystick Button
    START  = 0b00100000  # Start Button
    SELECT = 0b00010000  # Select Button
    HOME   = 0b00000001  # PS Button, on index 7

# Create a Riffmaster class
class Riffmaster:

    # Attributes
    connected        = False
    running          = False
    device           = hid.device()
    gamepad          = vg.VX360Gamepad()
    tilt_sensitivity = 0

    # Constants
    VENDOR_ID  = 0x0E6F
    PRODUCT_ID = 0x024A

    # Buttons / Axis
    button_mapping = {
        'fret 1'     : vg.XUSB_BUTTON.XUSB_GAMEPAD_LEFT_SHOULDER,
        'fret 2'     : vg.XUSB_BUTTON.XUSB_GAMEPAD_A,
        'fret 3'     : vg.XUSB_BUTTON.XUSB_GAMEPAD_B,
        'fret 4'     : vg.XUSB_BUTTON.XUSB_GAMEPAD_X,
        'fret 5'     : vg.XUSB_BUTTON.XUSB_GAMEPAD_RIGHT_SHOULDER,

        'dpad up'    : vg.XUSB_BUTTON.XUSB_GAMEPAD_DPAD_UP,
        'dpad down'  : vg.XUSB_BUTTON.XUSB_GAMEPAD_DPAD_DOWN,
        'dpad left'  : vg.XUSB_BUTTON.XUSB_GAMEPAD_DPAD_LEFT,
        'dpad right' : vg.XUSB_BUTTON.XUSB_GAMEPAD_DPAD_RIGHT,

        'stick'      : vg.XUSB_BUTTON.XUSB_GAMEPAD_LEFT_THUMB,
        'start'      : vg.XUSB_BUTTON.XUSB_GAMEPAD_START,
        'select'     : vg.XUSB_BUTTON.XUSB_GAMEPAD_BACK,
        'home'       : vg.XUSB_BUTTON.XUSB_GAMEPAD_GUIDE
    }
    
    # Initialize button states
    button_states = {button: False for button in button_mapping.keys()}

    # Create Functions
    def connect_device():
        
        # Connect the device
        try:
            Riffmaster.device.open(Riffmaster.VENDOR_ID, Riffmaster.PRODUCT_ID)
            
            #should ONLY run if it works yk
            Riffmaster.connected = True
            GUI.device_label.configure(text='Device: Connected')
            GUI.start_button.configure(state='enabled')
            GUI.connect_button.configure(state='disabled')
            GUI.start_button.update()
            GUI.connect_button.update()

        except:
            None
    
    def read_device(num):
        return Riffmaster.device.read(num)
    
    def is_button_pressed(value, mask):
        return value & mask != 0
    
    def is_hat_pressed(value, mask):
        return value & 0b00001111 == mask & 0b00001111
    
    def update_controller_features(whammy, tilt, stickX, stickY):

        # Update triggers to map tilt and whammy
        Riffmaster.gamepad.left_trigger(value=whammy)
        Riffmaster.gamepad.right_trigger(value=tilt)

        # Update the joystick
        Riffmaster.gamepad.left_joystick(x_value=stickX, y_value=stickY)

        Riffmaster.gamepad.update()

    def update_button_states(button_name, is_pressed):

        button_states = Riffmaster.button_states

        if is_pressed and not button_states[button_name]:

            Riffmaster.gamepad.press_button(Riffmaster.button_mapping[button_name])
            Riffmaster.gamepad.update()
            Riffmaster.button_states[button_name] = True

        elif not is_pressed and button_states[button_name]:

            Riffmaster.gamepad.release_button(Riffmaster.button_mapping[button_name])
            Riffmaster.gamepad.update()
            Riffmaster.button_states[button_name] = False

    def main_loop():

        Riffmaster.connect_device()

        while Riffmaster.running:

            #  Get new controller data
            inputs = Riffmaster.read_device(64)
            Riffmaster.tilt_sensitivity = GUI.slider_bar.get()

            current_states = {
            'fret 1'     : Riffmaster.is_button_pressed(inputs[46], Mask.FRET_1) or Riffmaster.is_button_pressed(inputs[47], Mask.FRET_1),
            'fret 2'     : Riffmaster.is_button_pressed(inputs[46], Mask.FRET_2) or Riffmaster.is_button_pressed(inputs[47], Mask.FRET_2),
            'fret 3'     : Riffmaster.is_button_pressed(inputs[46], Mask.FRET_3) or Riffmaster.is_button_pressed(inputs[47], Mask.FRET_3),
            'fret 4'     : Riffmaster.is_button_pressed(inputs[46], Mask.FRET_4) or Riffmaster.is_button_pressed(inputs[47], Mask.FRET_4),
            'fret 5'     : Riffmaster.is_button_pressed(inputs[46], Mask.FRET_5) or Riffmaster.is_button_pressed(inputs[47], Mask.FRET_5),

            'dpad up'    : Riffmaster.is_hat_pressed(inputs[5], Mask.DPAD_U),
            'dpad down'  : Riffmaster.is_hat_pressed(inputs[5], Mask.DPAD_D),
            'dpad left'  : Riffmaster.is_hat_pressed(inputs[5], Mask.DPAD_L),
            'dpad right' : Riffmaster.is_hat_pressed(inputs[5], Mask.DPAD_R),

            'stick'      : Riffmaster.is_button_pressed(inputs[6], Mask.STICK),
            'start'      : Riffmaster.is_button_pressed(inputs[6], Mask.START),
            'select'     : Riffmaster.is_button_pressed(inputs[6], Mask.SELECT),
            'home'       : Riffmaster.is_button_pressed(inputs[7], Mask.HOME)
            }

            # Update the buttons states
            for button in Riffmaster.button_mapping.keys():
                Riffmaster.update_button_states(button, current_states[button])

            Riffmaster.update_controller_features(inputs[44], (min(int(inputs[45]*Riffmaster.tilt_sensitivity),255)), inputs[1], inputs[2])

class GUI:

    def start_program():
        Riffmaster.running = True
        GUI.state_label.configure(text='Service: Running')
        GUI.start_button.configure(state='disabled')
        GUI.stop_button.configure(state='enabled')
        GUI.start_button.update()
        GUI.stop_button.update()

        thread = Thread(target=Riffmaster.main_loop)
        thread.start()

    def stop_program():
        Riffmaster.running = False
        GUI.start_button.configure(state='enabled')
        GUI.stop_button.configure(state='disabled')
        GUI.state_label.configure(text='Service: Not Running')
        GUI.start_button.update()
        GUI.stop_button.update()


    def start_gui():

        # Try to auto connect
        Riffmaster.connect_device()
        GUI.root.mainloop()

    ctk.set_appearance_mode("System")
    ctk.set_default_color_theme("blue")

    radius           = 15
    controller_state = 'Disconnected'
    service_state    = 'Not Running'
    release          = '1.1.1'

    root = ctk.CTk()
    root.title(f'Dipper v{release}')
    root.geometry('750x410')
    root.resizable(width=False, height=False)
    root.iconbitmap(resource_path('AppIcon.ico'))

    # Create 3 main frames
    right_frame = ctk.CTkFrame(root,width=240,corner_radius=radius)
    right_frame.pack_propagate(False)
    right_frame.pack(side=ctk.RIGHT,fill='y',padx=7,pady=7)

    middle_frame = ctk.CTkFrame(root,width=260,fg_color='transparent')
    middle_frame.pack(side=ctk.RIGHT,fill='y',padx=7)

    left_frame = ctk.CTkFrame(root,width=225,fg_color='transparent')
    left_frame.pack(side=ctk.RIGHT,fill='both',padx=7)

    # Create middle frame content
    options_frame = ctk.CTkFrame(middle_frame,width=260,height=230,corner_radius=radius)
    options_frame.pack_propagate(False)
    options_frame.pack(side=ctk.TOP,pady=7)
    status_frame = ctk.CTkFrame(middle_frame,width=260,corner_radius=20)
    status_frame.pack_propagate(False)
    status_frame.pack(side=ctk.TOP,pady=7)

    # Create left frame content
    caption_frame = ctk.CTkFrame(left_frame,width=225,height=130,corner_radius=radius)
    caption_frame.pack_propagate(False)
    caption_frame.pack(side=ctk.TOP,pady=7)
    button_frame = ctk.CTkFrame(left_frame,width=225,height=300,corner_radius=radius)
    button_frame.pack_propagate(False)
    button_frame.pack(side=ctk.TOP,pady=7,fill='y')

    # Create the title section
    program_name_label = ctk.CTkLabel(caption_frame,text='Dipper',font=('Consolas',35,'bold'))
    program_name_label.pack(side=ctk.TOP,pady=(22,1))
    release_label = ctk.CTkLabel(caption_frame,text=f'v{release}',font=('Consolas',30))
    release_label.pack(side=ctk.TOP,pady=(2,1))

    # Create the buttons
    buttons_label = ctk.CTkLabel(button_frame,text="Actions",font=('Consolas',24,'bold'))
    buttons_label.pack(pady=(20,20))

    start_button = ctk.CTkButton(button_frame,text="Start Service",font=('Consolas',20),width=160,height=35,state='disabled',command=start_program)
    start_button.pack(pady=(4,10))
    stop_button = ctk.CTkButton(button_frame,text="Stop Service",font=('Consolas',20),width=160,height=35,state='disabled',command=stop_program)
    stop_button.pack(pady=10)
    connect_button = ctk.CTkButton(button_frame,text="Connect",font=('Consolas',20),width=160,height=35,command=Riffmaster.connect_device)
    connect_button.pack(pady=10)

    # Status
    status_label = ctk.CTkLabel(status_frame,text="Status",font=('Consolas',24,'bold'))
    status_label.pack(pady=(20,10))

    device_label = ctk.CTkLabel(status_frame,text='Device: Disconnected',font=('Consolas',20))
    device_label.pack(pady=5,padx=10,side=ctk.TOP)
    state_label = ctk.CTkLabel(status_frame,text='Service: Not Running',font=('Consolas',20))
    state_label.pack(pady=5,padx=10,side=ctk.TOP)

    # Options
    options_label = ctk.CTkLabel(options_frame,text='Options',font=('Consolas',35,'bold'))
    options_label.pack(side=ctk.TOP,pady=(22,15))

    # To be implemented another day, my friend.
    #checkbox_1 = ctk.CTkCheckBox(options_frame,text='Unique Solo Frets',font=('Consolas',18),state='disabled')
    #checkbox_1.pack(pady=7,padx=25,anchor=ctk.W)
    #checkbox_2 = ctk.CTkCheckBox(options_frame,text='—————— TBD ——————',font=('Consolas',18),state='disabled')
    #checkbox_2.pack(pady=7,padx=25,anchor=ctk.W)

    slider_label = ctk.CTkLabel(options_frame,text='Tilt Sensitivity',font=('Consolas',20))
    slider_label.pack()
    slider_bar = ctk.CTkSlider(options_frame,from_=1,to=3)
    slider_bar.set(1.5)
    slider_bar.pack(pady=(1, 7), padx=25)

    # Updates
    news_label = ctk.CTkLabel(right_frame,text="What's New?",font=('Consolas',35,'bold'))
    news_label.pack(side=ctk.TOP,pady=(22,10))

    news_box = ctk.CTkScrollableFrame(right_frame,height=300,label_anchor=ctk.W)
    news_box.pack_propagate()
    news_box.pack(pady=10)
    
    news_info = ctk.CTkLabel(news_box, font=('Consolas',20), text=f'————— v{release} —————\nAdded a tilt sensitivity slider!\n\n————— v1.0.1 —————\nAdded an app icon!\n\nFixed the controller tilt functionality so it works out of the box.\n(You will need to recalibrate, I apologize.)\n\nThe app will no longer continue to run if you close the GUI before ending the process.\n\n———— Contact —————\nAs always, feel free to message me on Discord (@Najatski) if you need any help, need to report a bug, or have feature suggestions. Thank you!',justify=ctk.LEFT,wraplength=205)
    news_info.pack(side=ctk.LEFT,anchor=ctk.NW, pady=2)

GUI.start_gui()
Riffmaster.running = False
sys.exit()