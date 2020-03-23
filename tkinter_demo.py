import tkinter as tk
from PIL import Image, ImageTk


class Window(tk.Frame):

    def __init__(self, master=None):
        tk.Frame.__init__(self, master)               
        self.master = master
        self.width = 520
        self.height = 400
        self.email = tk.StringVar()
        self.password = tk.StringVar()
        self.text = tk.StringVar()
        self.text.set('')
        self.label = None
        self.init_window()

    # Creation of init_window
    def init_window(self):
        # changing the title of our master widget
        self.master.title("GUI")
        # size of the window
        self.master.geometry(f"{self.width}x{self.height}")

        # allowing the widget to take the full space of the root window
        self.pack(fill=tk.BOTH, expand=1)

        # creating a menu instance
        menu = tk.Menu(self.master)
        self.master.config(menu=menu)

        # create the file object)
        file = tk.Menu(menu)
        file.add_command(label="Restart", command=self.client_restart)

        file.add_command(label="Exit", command=self.client_exit)

        # create the file object)
        # adds a command to the menu option, calling it exit, and the
        # command it runs on event is client_exit
        edit = tk.Menu(menu)
        edit.add_command(label="Undo")
        # adds a command to the menu option, calling it exit, and the
        # command it runs on event is client_exit
        edit.add_command(label="Show Img", command=self.show_img)
        edit.add_command(label="Show Text", command=self.show_text)

        # added "file" and "edit" to our menu
        menu.add_cascade(label="File", menu=file)
        menu.add_cascade(label="Edit", menu=edit)

        # creating a button instance
        submit_button = tk.Button(self, text="Submit", command=self.submit, bg='#9A9AAE', width=10, height=1)

        # placing the button on my window
        submit_button.place(x=self.width / 2 - 20, y=self.height / 2 - 10)

        email = tk.Entry(self, textvar=self.email, width=30)
        email.place(x=self.width / 2 - 50, y=self.height / 2 - 65)
        email_label = tk.Label(self, text='Email:')
        email_label.place(x=self.width / 2 - 100, y=self.height / 2 - 65)

        password = tk.Entry(self, textvar=self.password, show='*', width=30)
        password.place(x=self.width / 2 - 50, y=self.height / 2 - 40)
        password_label = tk.Label(self, text='Password:')
        password_label.place(x=self.width / 2 - 110, y=self.height / 2 - 40)

        self.label = tk.Label(self, textvariable=self.text)
        self.label.pack()

    @staticmethod
    def client_exit():
        print('Exiting application')
        exit()

    def client_restart(self):
        print('Restarting application')
        self.destroy()
        Window(self.master)

    def show_img(self):
        load = Image.open("img.jpg")
        render = ImageTk.PhotoImage(load, width=self.width, height=self.height)
        # labels can be text or images
        img = tk.Label(self, image=render)
        img.image = render
        img.place(x=0, y=0)

    def show_text(self, txt='Please enter your username and password'):
        self.text.set(txt)

    def submit(self):
        print(self.email.get())
        print(self.password.get())
        print('submitted')
        if len(self.email.get()) == 0 or len(self.password.get()) == 0:
            self.show_text()
        else:
            self.show_text('')


root = tk.Tk()
app = Window(root)
root.mainloop()
