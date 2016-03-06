

import Tkinter as tk

## Modify this function to call itself recursively to draw smaller
## plus signs at the four end points of the current plus sign.
def draw_plus(chart_1, rootx, rooty, length, level, maxlevel):
    if level == maxlevel:
        return ##insert random comment here
    else:
        chart_1.create_line(rootx, rooty+length, rootx, rooty-length, fill="black") 
        chart_1.create_line(rootx+length, rooty, rootx-length, rooty, fill="black")
        right_rootx = rootx + length
        left_rootx = rootx - length
        top_rooty = rooty - length
        bottom_rooty = rooty + length
        length /= 2
        
        
        
        chart_1.update()
        
        level += 1
        draw_plus(chart_1, right_rootx, rooty, length, level, maxlevel)
        draw_plus(chart_1, rootx, bottom_rooty, length, level, maxlevel)
        draw_plus(chart_1, left_rootx, rooty, length, level, maxlevel)
        draw_plus(chart_1, rootx, top_rooty, length, level, maxlevel)
         

        
## Increases max level and calls the draw_plus function with the 
## given level. Note: maxlevel_info must be a list due to a 
## non-standard use of tkinter.
def restart(chart):
    chart_1.delete(tk.ALL) 
    draw_plus(chart, 400,300, 150, 0, maxlevel_info[0])
    maxlevel_info[0] += 1


### The main code simply creates a canvas and two buttons. 
##  We use a global list called maxlevel to keep track of 
##  how many iterations we would like to use for the recursion.
##  Whenever button2 is clicked, the maxlevel increases by one.
if __name__ == "__main__":
    root = tk.Tk()
    root.title("Recursion Example")
    chart_1 = tk.Canvas(root, width=800, height=600, background="white")
    chart_1.grid(row=0, column=0)
    maxlevel_info = [1]
    restart(chart_1)
    root.frame = tk.Frame(root)
    root.frame.button = tk.Button(root.frame, text="quit", \
                                  command=lambda:root.destroy())
    root.frame.button2 = tk.Button(root.frame, text="draw again!", \
                                   command=lambda:restart(chart_1))
    root.frame.button.grid()
    root.frame.button2.grid()
    root.frame.grid()
    root.mainloop()
