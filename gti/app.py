import os
from tkinter import *

def show_gti():
    # Create the window
    root = Tk()
    root.config(bg="#454545")
    root.overrideredirect(True)
    root.wm_attributes("-topmost", True)
    root.wm_attributes("-transparentcolor", "white")
    path = os.path.dirname(os.path.realpath(__file__))

    # Load the image
    photo = PhotoImage(file= path + "/gti.png")
    width, height = photo.width(), photo.height()

    # Place image on canvas for transparency
    canvas = Canvas(root, bg="white", width=width,
                    height=height, highlightthickness=0)
    canvas.pack()
    canvas.create_image(0, 0, image=photo, anchor=NW)

    screen_width = root.winfo_screenwidth() * 2
    screen_height = root.winfo_screenheight()
    x = 0 - width
    y = screen_height - height

    # Move window from left to right
    shouldRun = True
    try:
        while shouldRun:
            root.geometry(f"{width}x{height}+{x}+{y}")
            root.update()
            x += 1
            if x > screen_width:
                shouldRun = False
    except KeyboardInterrupt:
        pass
    root.destroy()

if __name__ == '__main__':
    show_gti()