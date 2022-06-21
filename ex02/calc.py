import tkinter as tk
import tkinter.messagebox as tkm

def button_click(event):
    btn = event.widget
    num = btn["text"]
    if num =="=":
        eqn = entry.get()
        res = eval(eqn)
        entry.delete(0,tk.END)
        entry.insert(tk.END,res)
    
    elif num == "AC":#オールクリア
        entry.delete(0,tk.END)

    #if num == "C":
        #eqn = entry.get()
        #entry.delete(len(eqn)-1,tk.END)[クリア機能]


    elif num == "%":
        eqn = entry.get()
        res = eval(eqn + "/ 100")
        entry.delete(0,tk.END)
        entry.insert(tk.END,res)


    elif num == "+/-":
        eqn = entry.get()
        res = eval(eqn + "* -1")
        entry.delete(0,tk.END)
        entry.insert(tk.END,res)

    else:
        #tkm.showinfo("",f"{num}のボタンがクリックされました")
        entry.insert(tk.END,num)
        
        

if __name__=="__main__":
    root = tk.Tk()
    root.title("電卓")

    entry = tk.Entry(root,
                    justify="right",
                    width=10,
                    font=("Times New Roman",40))
    entry.grid(row=0, column=0, columnspan=4)

    r, c = 1, 0
    a = ["AC","C","%","/",7,8,9,"*",4,5,6,"-",1,2,3,"+",0,".","+/-","="]#四則演算、クリア機能の追加
    for i, num in enumerate(a):
        btn = tk.Button(root,
                        text=f"{num}",
                        width=4,
                        height=2,
                        font=("Times New Roman",30)
                        )
        btn.bind("<1>", button_click)
        btn.grid(row=r, column=c)
        c += 1
        if (i+1) % 4 == 0:
            r += 1
            c = 0
     
    root.mainloop()