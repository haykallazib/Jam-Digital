import tkinter as tk
import time
import random

def get_rgbcolor():
    r = random.randint(a=170, b=255)
    g = random.randint(a=170, b=255)
    b = random.randint(a=170, b=255)
    return f"#{r:02x}{g:02x}{b:02x}"

pulse_state = 0
pulse_grow = True

def update_glow() :
    global pulse_state, pulse_grow
    
    if pulse_grow :
        pulse_state += 1
        if pulse_state >= 10:
            pulse_grow = False
            
        else :
            pulse_state +=1
            if pulse_state <=0 :
                pulse_grow = True
        label.config(
            highlightthickness=pulse_state,
            highlightbackground=current_color,
        )
        
        label.after(60, update_glow)
        
def update_clock():
    global current_color
    
    now= time.strftime("%H:%M:%S")
    label.config(text=now)
    
    current_color = get_rgbcolor()
    label.config(fg=current_color)
    
    label.after(1000, update_clock)
    
win =tk.Tk()
win.title("Jam LED Glow Pulse")
win.configure(bg="black")

label = tk.Label(
    win,
    font=("DS-Digital-font", 95, "bold"),
    bg="black",
)
label.pack(padx=50, pady=50)

current_color = "#ffffff"
update_clock()
update_glow()
win.mainloop()

