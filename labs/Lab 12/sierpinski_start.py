"""This modules draws the Sierpinks triangles up to a given depth
using the Tkinter module. It illustrates the use of recursion in
drawing self-similar patterns in smaller and smaller regions of the
larger triangle.

See:

   http://en.wikipedia.org/wiki/Sierpinski_triangle

"""

import Tkinter as tk
import math

def sierpinski(chart_1, lowleft, top, lowright, level, maxlevel):
    """Recursive function to draw Sierpinski triangles in chart_1
    within coordinates: lowleft, top, lowright. 

    At each call, the call level is increased. The function ends
    when maxlevel is reached.

    """

    chart_1.create_polygon([lowleft, top, lowright], fill="red") 
    leftmid = (lowleft[0]+top[0])/2,(lowleft[1]+top[1])/2
    rightmid = (lowright[0]+top[0])/2,(lowright[1]+top[1])/2
    bottommid = (lowright[0]+lowleft[0])/2,(lowright[1]+lowleft[1])/2
    chart_1.create_polygon([leftmid, rightmid, bottommid], fill="white") 
    chart_1.update() 

def restart(chart):
    """Redraws the Sierpinski triangle, but increasing the depth 
    at each time.

    """

    chart_1.delete(tk.ALL) 
    sierpinski(chart, \
               (0,600), (300,600-300*math.sqrt(3)), \
               (600,600), 0, maxlevel_var[0])
    maxlevel_var[0] += 1

if __name__ == "__main__":
    root = tk.Tk()
    root.title("Sierpinski Recursion Example")
    chart_1 = tk.Canvas(root, width=600, height=600, background="white")
    chart_1.grid(row=0, column=0)
    ## Initially max level is 1, which will draw 
    ##a simple triangle with an inverted triangle inside.
    maxlevel_var = [1]

    restart(chart_1)  ## Draw the Sierpinski triangles once
    root.frame = tk.Frame(root)
    root.frame.button = tk.Button(root.frame,\
                                  text="quit", \
                                  command=lambda:root.destroy())
    root.frame.button2 = tk.Button(root.frame, \
                                   text="draw again!", \
                                   command=lambda:restart(chart_1))
    root.frame.button.grid()
    root.frame.button2.grid()
    root.frame.grid()
    root.mainloop()
