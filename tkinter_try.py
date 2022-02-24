import tkinter as tk
root = tk.Tk()

# tk.Label(root, text = "嗨你好").pack()
# tk.Label(root,text = "嗨你好", fg = "brown", bg = "lightyellow").pack()
# tk.Button(root,text="按我吧").pack()
n = 0
def on_click():
    global n
    n += 1
    label.config(bg = "lightgreen" if n % 2 == 0 else "lightblue")
    label.config(text = "按了{}".format(n))

tk.Button(root, text = "按我吧", command = on_click).pack()
label = tk.Label(root)
label.pack()
# text = tk.StringVar()
# tk.Label(root, textvariable = text).pack()
root.mainloop()