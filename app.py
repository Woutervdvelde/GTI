from tkinter import *

#Create the window
root = Tk()
root.config(bg="red")
root.overrideredirect(True)
root.wm_attributes("-topmost", True)
root.wm_attributes("-transparentcolor", "red")

#Load the image
photo = PhotoImage(file="gti.png")
width, height = photo.width(), photo.height()

#Place image on canvas for transparency
canvas = Canvas(root, bg="red", width=width, height=height)
canvas.pack()
canvas.create_image(0, 0, image=photo, anchor=NW)

screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
x = 0 - width
y = screen_height - height

#Move window from left to right
shouldRun = True
while shouldRun:
    root.geometry(f"{width}x{height}+{x}+{y}")
    root.update()
    x += 1
    if x > screen_width:
        shouldRun = False

root.destroy()