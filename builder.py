#Novastorm development all rights reserved!
import os
import time
import tkinter as tk
import subprocess

root = tk.Tk()
root.title("If0n's Nuker | v1.0")
root.geometry("500x350")
root.resizable(False, False)

window = tk.Canvas(root, height=350, width=751,bg="#000000", highlightthickness=0)
window.pack()

#Title
title = tk.Label(root, height=2, width=14, bg="#000000", fg="#FFFFFF", text="If0n's Nuke Maker", font=("Arial", 25),)
title.pack()
title.place(x=115, y=0)
#You are fully aloud to take code from this project but you must give credit.
tokenent = tk.Entry(root, width = 50, fg = "black")
tokenent.insert(0, 'Bot Token') 
tokenent.pack()
tokenent.place(x=100, y=133)

webhookent = tk.Entry(root, width = 50, fg = "black")
webhookent.insert(0, 'Webhook')
webhookent.pack()
webhookent.place(x=100, y=185)

def build():
    token = tokenent.get()
    webhook = webhookent.get()
#You are fully aloud to take code from this project but you must give credit.
    filename = "thenuke.py"
    filepath = os.path.join(os.getcwd(), filename)
    with open(filepath, "r", encoding="utf-8") as f:
        content = f.read()
    new_content = content.replace('"TOKEN-HERE"', f'"{token}"')
    new_content = new_content.replace('"WEBHOOK-HERE"', f'"{webhook}"')
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(new_content)
    
    cmd = f"pyinstaller --onefile {filename}"
    subprocess.call(cmd, shell=True)

    # Change content back to normal
    new_content = new_content.replace(f'"{token}"', '"TOKEN-HERE"')
    new_content = new_content.replace(f'"{webhook}"', '"WEBHOOK-HERE"')
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(new_content)


buildbtn = tk.Button(root, width = 15, height = 2, bg = "white", fg = "black", text = "Build", command = build, font=("Arial", 10))
buildbtn.pack()
buildbtn.place(x=190, y=280)
#You are fully aloud to take code from this project but you must give credit.

root.mainloop()