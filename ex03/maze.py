import tkinter as tk
import maze_maker as mm

def key_down(event):
    global key
    key = event.keysym

def key_up(event):
    global key
    key = ""

def main_proc():
    global mx, my
    #delta = {#キー：押されているキーkey/値：移動幅リスト[x,y]
     #   "": [0, 0],
      #  "Up": [0, 20],
       # "Down": [0, -20],
       # "Left": [-20, 0],
        #"Right" :[+20, 0]
    #}
    #cx, cy = cx+delta[key][0], cy+delta[key][0]
    if key == "Up" and maze_bg[my-1][mx] == 0: my -= 1
    if key == "Down" and maze_bg[my+1][mx] == 0: my += 1
    if key == "Left" and maze_bg[my][mx-1] == 0: mx -= 1
    if key == "Right" and maze_bg[my][mx+1] == 0: mx += 1
    cx, cy = mx*50+30, my*50+30
    canvas.coords("tori", cx, cy)
    root.after(100, main_proc)

if __name__ == "__main__":
    root = tk.Tk()
    root.title("迷えるこうかとん")
    canvas = tk.Canvas(root,width=1500,height=900,bg="black")
    canvas.pack()
    maze_bg = mm.make_maze(30, 20) #1:壁/0:床を表す
    mm.show_maze(canvas, maze_bg)


    tori = tk.PhotoImage(file="fig/8.png")
    mx, my = 1, 1
    cx, cy = mx*30+30, my*30+30
    canvas.create_image(cx, cy, image=tori, tag="tori")

    key = ""
    root.bind("<KeyPress>",key_down)
    root.bind("<KeyRelease>",key_up)

    main_proc()
    root.mainloop()