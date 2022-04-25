from telnetlib import SE
import tkinter as tk
from tkinter import ANCHOR, CENTER, EW, NE, NS, NSEW, NW, SW, ttk
import os
from os import listdir
from PIL import Image, ImageTk, ImageOps


class Page(tk.Frame):
    def __init__(self, *args, **kwargs):
        tk.Frame.__init__(self, *args, **kwargs)
        self.canvas = tk.Canvas(self, borderwidth=0, width=1500,
                                height=900, yscrollincrement=10, background="#263D42")
        self.frame = tk.Frame(self.canvas, bg="#263D42")
        self.vsb = tk.Scrollbar(self, orient="vertical",
                                command=self.canvas.yview)
        self.canvas.configure(yscrollcommand=self.vsb.set)
        self.canvas.configure(scrollregion=(0, 0, 2999, 3699))

        self.canvas.grid(row=0, column=0, sticky="nsew")
        self.vsb.grid(row=0, column=1, sticky="ns")
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)
        self.canvas.create_window(
            (4, 4), anchor=NW, window=self.frame, tags="self.frame")

        self.frame.bind('<Enter>', self._bound_to_mousewheel)
        self.frame.bind('<Leave>', self._unbound_to_mousewheel)

    def _on_mousewheel(self, event):
        self.canvas.yview_scroll(int(-1*(event.delta/30)), "units")

    def _bound_to_mousewheel(self, event):
        self.canvas.bind_all("<MouseWheel>", self._on_mousewheel)

    def _unbound_to_mousewheel(self, event):
        self.canvas.unbind_all("<MouseWheel>")

    def show(self):
        self.lift()


class Page1(Page):
    def __init__(self, *args, **kwargs):
        Page.__init__(self, *args, **kwargs)
        label = tk.Label(self.frame, text="All Designs", font=(
            "Arial", 20), background="#263D42", fg="white")
        description = tk.Label(self.frame, text="A compilation of all custom Magic: The Gathering cards I have designed, listed in alphabetical order.",
                               font="Arial", background="#263D42", fg="white")
        label.grid(row=0, column=1, sticky=EW)
        description.grid(row=1, column=1)

        path = ".\All"
        row = 2
        column = 0
        for images in os.listdir(path):
            if(images.endswith(".png")):
                icon = Image.open(".\All\\" + images)
                if(icon.width <= 800):
                    resize = icon.resize((298, 408))
                    img = ImageTk.PhotoImage(resize)
                    button = tk.Button(self.frame, image=img,
                                       height=408, width=298)
                    button.image = img
                    button.grid(row=row, column=column)
                    title = tk.Label(self.frame, text=images.removesuffix(
                        ".png"), font=("Arial", 15), background="#263D42", fg="white")
                    title.grid(row=row + 1, column=column, pady=10)
                    vlist = ["1", "2", "3", "4", "5"]
                    Combo = ttk.Combobox(self.frame, values=vlist)
                    Combo.set("Rate this design")
                    Combo.grid(row=row + 2, column=column, pady=15)
                    column += 1
                    if column >= 3:
                        row += 3
                        column = 0
                else:
                    resize = icon.resize((int(icon.width / 3), int(icon.height / 3)))
                    img = ImageTk.PhotoImage(resize)
                    button = tk.Button(self.frame, image=img,
                                       height=int(icon.height / 3), width=int(icon.width / 3))
                    button.image = img
                    if(column >= 1):
                        row += 3
                    button.grid(row=row, column=1)
                    title = tk.Label(self.frame, text=images.removesuffix(
                        ".png"), font=("Arial", 15), background="#263D42", fg="white")
                    title.grid(row=row + 1, column=1, pady=10)
                    vlist = ["1", "2", "3", "4", "5"]
                    Combo = ttk.Combobox(self.frame, values=vlist)
                    Combo.set("Rate this design")
                    Combo.grid(row=row + 2, column=1, pady=15)
                    row += 3
                    column = 0                                      

class Page2(Page):
    def __init__(self, *args, **kwargs):
        Page.__init__(self, *args, **kwargs)
        label = tk.Label(self.frame, text="Darchaen Empire", font=(
            "Arial", 20), background="#263D42", fg="white")
        description = tk.Label(self.frame, text="This deck was built around the idea of dealing damage to your opponents for\n doing things in Magic: The Gathering, such as drawing cards or casting spells. This straegy is called group slug.",
                               font="Arial", background="#263D42", fg="white")
        label.grid(row=0, column=1)
        description.grid(row=1, column=1)

        path = ".\Darch"
        row = 2
        column = 0
        for images in os.listdir(path):
            if(images.endswith(".png")):
                icon = Image.open(".\Darch\\" + images)
                resize = icon.resize((298, 408))
                img = ImageTk.PhotoImage(resize)
                button = tk.Button(self.frame, image=img,
                                   height=408, width=298)
                button.image = img
                button.grid(row=row, column=column)
                title = tk.Label(self.frame, text=images.removesuffix(
                    ".png"), font=("Arial", 15), background="#263D42", fg="white")
                title.grid(row=row + 1, column=column, pady=10)
                vlist = ["1", "2", "3", "4", "5"]
                Combo = ttk.Combobox(self.frame, values=vlist)
                Combo.set("Rate this design")
                Combo.grid(row=row + 2, column=column, pady=15)
                column += 1
                if column >= 3:
                    row += 3
                    column = 0


class Page3(Page):
    def __init__(self, *args, **kwargs):
        Page.__init__(self, *args, **kwargs)
        label = tk.Label(self.frame, text="Profile", font=(
            "Arial", 20), background="#263D42", fg="white")
        label.grid(row=0, column=1, sticky=EW)
        name1 = tk.Label(self.frame, text="Name: ", font=(
            "Arial", 15), background="#263D42", fg="white")
        name1.grid(row=1, column=0)
        name2 = tk.Label(self.frame, text="Kevin Kolkman", font=(
            "Arial", 15), background="#263D42", fg="white")
        name2.grid(row=1, column=1)
        age1 = tk.Label(self.frame, text="Age: ", font=(
            "Arial", 15), background="#263D42", fg="white")
        age1.grid(row=2, column=0)
        age2 = tk.Label(self.frame, text="20", font=(
            "Arial", 15), background="#263D42", fg="white")
        age2.grid(row=2, column=1)
        major1 = tk.Label(self.frame, text="Major: ", font=(
            "Arial", 15), background="#263D42", fg="white")
        major1.grid(row=3, column=0)
        major2 = tk.Label(self.frame, text="Computer Science (Cybersecurity)", font=(
            "Arial", 15), background="#263D42", fg="white")
        major2.grid(row=3, column=1)
        contact1 = tk.Label(self.frame, text="Contact Info: ", font=(
            "Arial", 15), background="#263D42", fg="white")
        contact1.grid(row=4, column=0)
        contact2 = tk.Label(self.frame, text="Email: filler@notreal.what\nPhone Number: +1 XXX-XXX-FAKE",
                            font=("Arial", 15), background="#263D42", fg="white")
        contact2.grid(row=4, column=1)
        summary1 = tk.Label(self.frame, text="Description: ", font=(
            "Arial", 15), background="#263D42", fg="white")
        summary1.grid(row=5, column=0)
        summary2 = tk.Label(self.frame, text="I am an avid fan of card games, specifically Magic: The Gathering. I've been playing since my sophomore year of high school,\nwhen my friend introduced me to the game. Since then, I've built several decks geared towards\nthe Commander format, and have even designed custom Magic cards as a hobby. The designs on this site are a sample of\nwhat I've made.", font=("Arial", 15), background="#263D42", fg="white")
        summary2.grid(row=5, column=1)
        canvasPro = tk.Canvas(self.frame, width=298, height=408)
        canvasPro.grid(row=6, column=1, sticky=NS)
        holder = Image.open("Profile.jpg")
        holder = ImageOps.exif_transpose(holder)
        img = ImageTk.PhotoImage(holder)
        canvasPro.create_image(0, 0, image=img, anchor=NW)
        canvasPro.image = img


class MainView(tk.Frame):
    def __init__(self, *args, **kwargs):
        tk.Frame.__init__(self, *args, **kwargs)
        p1 = Page1(self)
        p2 = Page2(self)
        p3 = Page3(self)

        buttonframe = tk.Frame(self)
        container = tk.Frame(self)
        buttonframe.pack(side="top", fill="x", expand=False)
        container.pack(side="top", fill="both", expand=True)

        p1.place(in_=container, x=0, y=0, relwidth=1, relheight=1)
        p2.place(in_=container, x=0, y=0, relwidth=1, relheight=1)
        p3.place(in_=container, x=0, y=0, relwidth=1, relheight=1)

        b1 = tk.Button(buttonframe, text="All Designs", padx=10,
                       pady=5, fg="white", bg="#263D42", command=p1.show)
        b2 = tk.Button(buttonframe, text="Darchaen Empire", padx=10,
                       pady=5, fg="white", bg="#263D42", command=p2.show)
        b3 = tk.Button(buttonframe, text="Profile", padx=10,
                       pady=5, fg="white", bg="#263D42", command=p3.show)

        b1.pack(side="left")
        b2.pack(side="left")
        b3.pack(side="left")

        p1.show()


if __name__ == "__main__":
    root = tk.Tk()
    root.title('Custom Design Portfolio')
    main = MainView(root)
    main.pack(side="top", fill="both", expand=True)
    root.wm_geometry("1920x1080")
    root.mainloop()
