from tkinter import *

'''
master = Tk()

master.geometry("600x350")
master.resizable(False, False)

background_color_main = '#1b2631'

master.iconbitmap("./images/rosetta_pierre_logo_v_1.0.ico")
master.config(bg=background_color_main)

master.overrideredirect(True)

title_bar = Frame(master,bg=background_color_main)
title_bar.pack( fill=X)

def move_app(e):
    master.geometry(f'+{e.x_root}+{e.y_root}')

title_bar.bind("<B1-Motion>", move_app)

label_title = Label(title_bar, text="RosettaPierre", bg=background_color_main, fg='white')
label_title.pack(side=LEFT, pady=2)

def keep_flat(e):
    if e.widget is button_close:
        e.widget.config(relief=FLAT)
        master.destroy()

def callback():
    print('button clicked')

def on_enter(e):
   button_close.config(bg='red')

def on_leave(e):
   button_close.config(bg= background_color_main)

button_close = Button(title_bar, text=" X ", bg=background_color_main, fg='white', relief=FLAT, command=callback)
button_close.pack(side=RIGHT)

button_close.bind('<Enter>', on_enter)
button_close.bind('<Leave>', on_leave)

master.bind('<Button-1>', keep_flat)

master.mainloop()
'''

class Interface():
    def __init__(self):
        self.root = Tk()

        self.root.geometry("600x350")
        self.root.resizable(False, False)

        #colors
        self.color_main_bg = '#1b2631'
        self.color_close_button = '#e74c3c'

        #useful images
        self.path_image_logo = "./images/rosetta_pierre_logo_v_1.0.ico"
        self.path_image_title = "./images/rosetta_pierre_title.png"

        self.root.config(bg=self.color_main_bg)
        self.root.overrideredirect(True)

    def start(self):
        self.create_fake_taskbar()
        self.print_header()
        self.login_page()
        self.root.mainloop()

    def print_header(self):
        # Image part
        canvas_image_title = Canvas(self.root, width=600, height=100, bg=self.color_main_bg, bd=0,
                                    highlightthickness=0)

        image_tile = PhotoImage(file=self.path_image_title).zoom(6).subsample(32)
        canvas_image_title.create_image(80, 20, image=image_tile)
        canvas_image_title.image = image_tile

        canvas_image_title.pack()

    def hide_login(self):
        self.frame_login.pack_forget()

    def login_page(self):

        self.frame_login = Frame(self.root, bg=self.color_main_bg)

        #Entry part
        frame_entry = Frame(self.frame_login, bg=self.color_main_bg)

        label_username = Label(frame_entry,text='username', bg=self.color_main_bg, fg='white')
        label_username.pack()
        entry_username = Entry(frame_entry, bg=self.color_main_bg, fg='white')
        entry_username.pack()

        label_password = Label(frame_entry, text='password', bg=self.color_main_bg, fg='white')
        label_password.pack()
        entry_password = Entry(frame_entry, bg=self.color_main_bg, fg='white')
        entry_password.pack()

        button_login = Button(frame_entry, text='   Login   ', bg='#3498db', fg='white', bd=0, relief=FLAT, command=self.hide_login)
        button_login.pack()

        frame_entry.grid(row=1, column=0)

        self.frame_login.pack()

    def create_fake_taskbar(self):
        title_bar = Frame(self.root, bg=self.color_main_bg)
        title_bar.pack(fill=X)

        def move_app(e):
            self.root.geometry(f'+{e.x_root}+{e.y_root}')

        title_bar.bind("<B1-Motion>", move_app)

        def keep_flat(e):
            if e.widget is button_close:
                e.widget.config(relief=FLAT)
                self.root.destroy()

        def callback():
            print('button clicked')

        def on_enter(e):
            button_close.config(bg=self.color_close_button)

        def on_leave(e):
            button_close.config(bg=self.color_main_bg)

        button_close = Button(title_bar, text=" X ", bg=self.color_main_bg, fg='white', relief=FLAT,
                              command=callback)
        button_close.pack(side=RIGHT)

        button_close.bind('<Enter>', on_enter)
        button_close.bind('<Leave>', on_leave)

        self.root.bind('<Button-1>', keep_flat)


if __name__ == "__main__":
    myInterface = Interface()
    myInterface.start()