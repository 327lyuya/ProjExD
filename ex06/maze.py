import tkinter as tk
import maze_maker as mm
import random

def key_down(event):
    global key
    key = event.keysym

def key_up(event):
    global key
    key = ""

def main_proc():
    global mx, my
    if key == "Down" and maze_bg[my+1][mx] == 0: my += 1
    if key == "Left" and maze_bg[my][mx-1] == 0: mx -= 1
    if key == "Right" and maze_bg[my][mx+1] == 0: mx += 1
    if key == "Up" and maze_bg[my-1][mx] == 0: my -= 1
    cx, cy = mx*100+50, my*100+50
    canvas.coords("tori", cx, cy)
    canvas.coords("enemy",300,300)
    root.after(100, main_proc)

def goal():
    global map, canvas
    height = len(map)
    end_p=[]
    for i in range(0, height):
        if not map[i][-2]:
            if map[i][-3] + map[i-1][-2] + map[i+1][-2] == 2:
                end_p.append(i)
    if len(end_p):
        i = random.randint(0,len(end_p)-1)
        y = end_p[i]
    else:
        for i in range(height):
            if not map[i][-2]:
                y = i
    x = len(map[-2])-2
    canvas.create_rectangle(x*100, y*100, x*100+100, y*100+100, fill="red")
    return(x, y)



if __name__ == "__main__":
    root = tk.Tk()
    root.title("迷えるこうかとん")
    canvas = tk.Canvas(root,width=1500,height=900,bg="black")
    canvas.pack()
    maze_bg = mm.make_maze(30, 20) #1:壁/0:床を表す
    mm.show_maze(canvas, maze_bg)

    maze_mk=mm.make_maze(15,9)
    mm.show_maze(canvas,maze_mk)
    canvas.create_rectangle(100,100,200,200,fill="red")

    tori = tk.PhotoImage(file="fig/8.png")
    mx, my = 1, 1
    cx, cy = mx*30+30, my*30+30
    canvas.create_image(cx, cy, image=tori, tag="tori")
    
    key = ""
    root.bind("<KeyPress>",key_down)
    root.bind("<KeyRelease>",key_up)

    main_proc()
    root.mainloop()