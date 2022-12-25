from tkinter import *
from tkinter import ttk


class MyTodoLists:
    def __init__(self, master):
        master.title("Todo Lists")

        # create notebook
        self.my_notebook = ttk.Notebook(master)
        self.my_notebook.pack(padx=5, pady=5)
        # with style option, we can change the color, font, etc. tabs
        style = ttk.Style()
        style.configure("TNotebook.Tab", font=("Ariel", 10, "bold"))

        # create tabs/frames for notebook
        self.home_list_frame = Frame(self.my_notebook, width=400, height=300)
        self.home_list_frame.pack()
        self.work_list_frame = Frame(self.my_notebook, width=400, height=300, bg="white")
        self.work_list_frame.pack()
        self.groceries_list_frame = Frame(self.my_notebook, width=400, height=300, bg="white")
        self.groceries_list_frame.pack()

        # add tabs to notebook
        self.my_notebook.add(self.home_list_frame, text="HOME todo list ")
        self.my_notebook.add(self.work_list_frame, text="WORK todo list ")
        self.my_notebook.add(self.groceries_list_frame, text="GROCERIES todo list ")

        # add widgets to first tab/Home todo_list
        self.home_list_text = Text(self.home_list_frame, width=45, height=15, font=("Ariel", 13,"italic"))
        self.home_list_text.grid(row=0, column=0)

        # add scrollbar
        self.my_scroll = Scrollbar(self.home_list_frame)
        # scroll the text widget
        self.my_scroll.config(command=self.home_list_text.yview)
        # set the scrollbar to text widget
        self.home_list_text.config(yscrollcommand=self.my_scroll.set)
        self.my_scroll.grid(row=0, column=1, sticky="nsew")

        self.home_list_save_button = Button(self.home_list_frame, text="Save list",
                                            font=("Ariel", 11, "bold"), bg="green", fg="white",
                                            activebackground="green",
                                            command=self.home_list_save_items)
        self.home_list_save_button.grid(row=1, column=0, pady=5, padx=5, sticky="W")

        # add the items from home todo_list text file to text widget
        path = "C:\\Users\\urdan\\Desktop\\home todo list.txt"
        with open(path, "r") as file:
            home_todo_list = file.read()
            self.home_list_text.insert(END, home_todo_list)

        # add widgets to second tab/Work todo_list
        self.work_list_text = Text(self.work_list_frame, width=45, height=15, font=("Ariel", 13, "italic"))
        self.work_list_text.grid(row=0, column=0)

        # add scrollbar
        self.my_scroll = Scrollbar(self.work_list_frame)
        # scroll the text widget
        self.my_scroll.config(command=self.work_list_text.yview)
        # set the scrollbar to text widget
        self.work_list_text.config(yscrollcommand=self.my_scroll.set)
        self.my_scroll.grid(row=0, column=1, sticky="nsew")

        self.work_list_save_button = Button(self.work_list_frame, text="Save list",
                                            font=("Ariel", 11, "bold"), bg="#0c521e", activebackground="#0c521e",
                                            fg="white",
                                            command=self.work_list_save_items)
        self.work_list_save_button.grid(row=1, column=0, pady=5, padx=5, sticky="W")

        # add the items from work todo_list text file to text widget
        path = "C:\\Users\\urdan\\Desktop\\work todo list.txt"
        with open(path, "r") as file:
            work_todo_list = file.read()
            self.work_list_text.insert(END, work_todo_list)

        # add widgets to third tab/Groceries todo_list
        self.groceries_list_text = Text(self.groceries_list_frame, width=45, height=15, font=("Ariel", 13, "italic"))
        self.groceries_list_text.grid(row=0, column=0)

        # add scrollbar
        self.my_scroll = Scrollbar(self.groceries_list_frame)
        # scroll the text widget
        self.my_scroll.config(command=self.groceries_list_text.yview)
        # set the scrollbar to text widget
        self.groceries_list_text.config(yscrollcommand=self.my_scroll.set)
        self.my_scroll.grid(row=0, column=1, sticky="nsew")

        self.groceries_list_save_button = Button(self.groceries_list_frame, text="Save list",
                                                 font=("Ariel", 11, "bold"), bg="#23422b", activebackground="#23422b",
                                                 fg="white",
                                                 command=self.groceries_list_save_items)
        self.groceries_list_save_button.grid(row=1, column=0, pady=5, padx=5, sticky="W")

        # add the items from groceries todo_list text file to text widget
        path = "C:\\Users\\urdan\\Desktop\\groceries todo list.txt"
        with open(path, "r") as file:
            groceries_todo_list = file.read()
            self.groceries_list_text.insert(END, groceries_todo_list)

    def home_list_save_items(self):
        home_todo_list = self.home_list_text.get(1.0, END)
        path = "C:\\Users\\urdan\\Desktop\\home todo list.txt"
        with open(path, "w") as file:
            file.write(home_todo_list)

    def work_list_save_items(self):
        work_todo_list = self.work_list_text.get(1.0, END)
        path = "C:\\Users\\urdan\\Desktop\\work todo list.txt"
        with open(path, "w") as file:
            file.write(work_todo_list)

    def groceries_list_save_items(self):
        groceries_todo_list = self.groceries_list_text.get(1.0, END)
        path = "C:\\Users\\urdan\\Desktop\\groceries todo list.txt"
        with open(path, "w") as file:
            file.write(groceries_todo_list)


window = Tk()
todo_lists = MyTodoLists(window)
window.mainloop()
