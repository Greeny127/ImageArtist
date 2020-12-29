# ImageArtist
A short program that takes an image, maps it out using coordinates and then draws it in paint.net, a free alternate to photoshop.

# Requirements
- Paint.net
- OpenCV
- Pyautogui
- Time
- Colormap

# Setup
Once all requirements are met, you have to customise the program to suit your computers needs. Start by changing the `x` and `y` in `__init__`, this is the starting posistions for the program. Then change the coordinates in `setColor()`, it is used to set the `hex` color in the pallete. (clicking More>> before starting the program is necessary)

It is reccomended to resize the orignal image to a smaller size if it is too big, in case the coordintes go out of bounds.

**This is not complete.**
