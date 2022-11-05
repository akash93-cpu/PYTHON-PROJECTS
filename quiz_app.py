import tkinter as tk
from tkinter import tix
from tkinter import ttk
from datetime import datetime
import json
import tkinter.messagebox
import sqlite3


# # FUNCTION USED TO CREATE THE INITIAL DATABASE TABLE--------------------------------------------------------------------

def create_initial_database():

    with sqlite3.connect("userdata.db") as db:

        cursor = db.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS quizdata(username TEXT NOT NULL PRIMARY KEY,"
                   "password TEXT NOT NULL, score INT, score2 INT);")
    cursor.execute("SELECT * FROM quizdata")
    db.commit()
    db.close()


create_initial_database()

# MAIN GUI DESIGN: ------------------------------------------------------------------------------------------------------


class Main:

    def __init__(self):
        self.root = tix.Tk()
        self.root.style = ttk.Style()
        self.root.style.theme_use('clam')
        self.root.title("Quiz App")
        self.root.geometry("850x600+530+230")
        self.root.resizable(False, False)
        self.root.iconbitmap(r'logo.ico')

        self.create_user = tk.StringVar()
        self.login_user = tk.StringVar()
        self.user_admin = tk.StringVar()
        self.var = tk.StringVar()
        self.max_len = 5

        self.var2 = tk.StringVar()
        self.max_len2 = 5

        self.admin_password = tk.StringVar()
        self.max_len3 = 4

        # MAIN FRAME:

        self.mainFrame = tk.Frame(self.root)
        self.mainFrame.pack(fill="both", expand=True)

        self.some_label = tk.Label(self.mainFrame,text="Developed by: Akash S.", font=('Cambria', 9))
        self.some_label.place(relx=0.5, y=588, anchor='center')

        self.label1 = tk.Label(self.mainFrame, text=" WELCOME TO THE QUIZ APP ", font=('Cambria italic', 30),
                               relief="groove")
        self.label1.pack(pady=25)

        self.label2 = tk.Label(self.mainFrame, text="NEW USER", font=('Courier New italic', 16), relief="ridge")
        self.label2.place(x=180, y=150)

        self.labelname = tk.Label(self.mainFrame, text="USERNAME:", font=('Courier New', 12))
        self.labelname.place(x=50, y=216)

        self.labelpassword = tk.Label(self.mainFrame, text="PASSWORD:", font=('Courier New', 12))
        self.labelpassword.place(x=50, y=248)

        self.entry1 = tk.Entry(self.mainFrame, width=33, bg="light blue", justify=tk.CENTER,
                               textvariable=self.create_user, font=('Courier New', 9))
        self.entry1.place(x=150, y=220, height=20)

        self.entry2 = tk.Entry(self.mainFrame, width=33, bg="light blue", show='•', textvariable=self.var,
                               justify=tk.CENTER, font=('Courier New', 9))
        self.var.trace_variable("w", self.on_write)
        self.entry2.place(x=150, y=250, height=20)

        self.clear1 = tk.Button(self.mainFrame, text="CLEAR", font=("Courier New", 12), command=self.clearfunc1)
        self.clear1.place(x=50, y=350)

        self.create = tk.Button(self.mainFrame, text="CREATE", font=("Courier New", 12),
                                command = self.create_new_user_func)
        self.create.place(x=310, y=350)

        self.create.bind("<Enter>", self.hover)
        self.create.bind("<Leave>", self.hoverLeave)

        self.tooltipcreate = tix.Balloon(self.mainFrame)
        self.tooltipcreate.bind_widget(self.create, balloonmsg="Create a new user within the system")

        self.label3 = tk.Label(self.mainFrame, text="EXISTING USER", font=('Courier New italic', 16), relief="ridge")
        self.label3.place(x=550, y=150)

        self.label4 = tk.Label(self.mainFrame, text="USERNAME:", font=("Courier New", 12))
        self.label4.place(x=475, y=216)

        self.label5 = tk.Label(self.mainFrame, text="PASSWORD:", font=("Courier New", 12))
        self.label5.place(x=475, y=248)

        self.clear2 = tk.Button(self.mainFrame, text="CLEAR", font=("Courier New", 12), command=self.clearfunc2)
        self.clear2.place(x=475, y=350)

        self.login = tk.Button(self.mainFrame, text="LOGIN", font=("Courier New", 12), command=self.login_user_func)
        self.login.place(x=745, y=350)

        self.login.bind("<Enter>", self.hover2)
        self.login.bind("<Leave>", self.hoverLeave)

        self.tooltiplogin = tix.Balloon(self.mainFrame)
        self.tooltiplogin.bind_widget(self.login, balloonmsg="Login to the app with an existing user's credentials")

        self.entry3 = tk.Entry(self.mainFrame, width=33, bg="light blue", justify=tk.CENTER,
                               textvariable=self.login_user, font=('Courier New', 9))
        self.entry3.place(x=575, y=220, height=20)

        self.entry4 = tk.Entry(self.mainFrame, width=33, bg="light blue", show='•', justify=tk.CENTER,
                               textvariable=self.var2, font=('Courier New', 9))
        self.var2.trace_variable("w", self.on_write2)
        self.entry4.place(x=575, y=250, height=20)

        self.separator = ttk.Separator(self.mainFrame, orient="vertical").pack(ipady=220, padx=195)

        self.exitButton = tk.Button(self.mainFrame, text="EXIT", command=self.close, font=('Courier New italic', 12))
        self.exitButton.place(x=780, y=550)

        self.exitButton.bind("<Enter>", self.exitHover)
        self.exitButton.bind("<Leave>", self.hoverLeave)

        self.scoreboard = tk.Button(self.mainFrame, text="SCOREBOARD",
                                    font=('Courier New italic', 12), command=self.scoreboard_view)
        self.scoreboard.place(x=30, y=550)

        self.tooltipscoreboard = tix.Balloon(self.mainFrame)
        self.tooltipscoreboard.bind_widget(self.scoreboard, balloonmsg="View user score data")

        self.admin = tk.Button(self.mainFrame, text="ADMIN", font=('Courier New italic', 12),
                               command=self.admin_func)
        self.admin.place(x=30, y=510)

        self.tooltipadmin = tix.Balloon(self.mainFrame)
        self.tooltipadmin.bind_widget(self.admin, balloonmsg="Delete a user from the system")

        # FRAME 2:

        self.frame2 = tk.Frame(self.root, bg="Light Blue")

        self.label1frame2 = tk.Label(self.frame2, text="Select your choice:",
                                     font=('Cambria italic', 20), bg="Light Blue")
        self.label1frame2.place(x=30, y=20)

        self.buttonFrame2 = tk.Button(self.frame2, text="LOG OUT", command=self.frame2to1,
                                      font=('Courier New italic', 12))
        self.buttonFrame2.place(x=30, y=550)

        self.tooltip = tix.Balloon(self.frame2)
        self.tooltip.bind_widget(self.buttonFrame2, balloonmsg="Log off and return back to the main screen")

        # OPTION 1

        self.iframe = tk.LabelFrame(self.frame2, text="Quiz 1", padx=10, pady=120, bg="Light Blue",
                                    font=('Cambria', 18),
                                    labelanchor='n', bd=3)
        self.iframe.pack(fill="both", expand=True)
        self.iframe.place(x=40, y=70)

        self.ilabel = tk.Label(self.iframe, text='This quiz contains questions from', font=('Courier New italic', 10)
                               , bg="Light Blue")
        self.ilabel.pack(pady=20)

        self.ilabel2 = tk.Label(self.iframe, text='popular games such as',
                                font=('Courier New italic', 10), bg="Light Blue")
        self.ilabel2.pack(pady=20)

        self.ilabel3 = tk.Label(self.iframe, text='God Of War, The Last Of Us and Tomb Raider',
                                font=('Courier New italic', 10), bg="Light Blue")
        self.ilabel3.pack(pady=20)

        self.startButton = tk.Button(self.iframe, text="START",
                                     font=('Courier New', 10), command=self.frame2to3)
        self.startButton.pack(ipadx=200, pady=20)

        self.startButton.bind("<Enter>", self.hover)
        self.startButton.bind("<Leave>", self.hoverLeave)

        self.startButton.place(y=250, x=140)

        # OPTION 2

        self.iframe2 = tk.LabelFrame(self.frame2, text="Quiz 2", padx=10, pady=120, bg="Light Blue",
                                     font=('Cambria', 18), labelanchor='n', bd=3)
        self.iframe2.pack(fill="both", expand=True)
        self.iframe2.place(x=440, y=70)

        self.ilabel4 = tk.Label(self.iframe2, text='This quiz contains questions from', font=('Courier New italic', 10),
                                bg="Light Blue")
        self.ilabel4.pack(pady=20)

        self.ilabel5 = tk.Label(self.iframe2, text='popular games such as', font=('Courier New italic', 10),
                                bg="Light Blue")
        self.ilabel5.pack(pady=20)

        self.ilabel6 = tk.Label(self.iframe2, text="Assassin's Creed, Dead Space and The Witcher",
                                font=('Courier New italic', 10), bg="Light Blue")
        self.ilabel6.pack(pady=20)

        self.startButton2 = tk.Button(self.iframe2, text='START', font=('Courier New', 10), command=self.frame2to5)
        self.startButton2.pack(pady=10)

        self.startButton2.bind("<Enter>", self.hover2)
        self.startButton2.bind("<Leave>", self.hoverLeave)
        self.startButton2.place(y=250, x=140)

        self.exitButton2 = tk.Button(self.frame2, text="EXIT", command=self.close, font=('Courier New italic', 12))
        self.exitButton2.place(x=780, y=550)

        self.exitButton2.bind("<Enter>", self.exitHover2)
        self.exitButton2.bind("<Leave>", self.hoverLeave)

        # FRAME 3:

        self.frame3 = tk.Frame(self.root)

        # FRAME 4:

        self.frame4 = tk.Frame(self.root)

        # FRAME 5:

        self.frame5 = tk.Frame(self.root)

        # FRAME 6:

        self.frame6 = tk.Frame(self.root)

        # SCORE FRAME:

        self.scoreFrame = ttk.Treeview(self.root)
        self.style = ttk.Style()
        self.style.configure("Treeview.Heading", font=('Courier New', 10))
        self.style.configure("Treeview", font=('Courier New', 10))
        self.scoreFrame['show'] = 'headings'
        self.scoreFrame['columns'] = ("Username", "Score - Quiz 1", "Score - Quiz 2")
        self.scoreFrame.column("Username", anchor='center', minwidth=400)
        self.scoreFrame.column("Score - Quiz 1", anchor='center', minwidth=80)
        self.scoreFrame.column("Score - Quiz 2", anchor='center', minwidth=220)

        self.scoreFrame.heading("Username", text="USERNAME", anchor='center')
        self.scoreFrame.heading("Score - Quiz 1", text="SCORE - QUIZ 1", anchor='center')
        self.scoreFrame.heading("Score - Quiz 2", text="SCORE - QUIZ 2", anchor='center')

        self.backbutton = tk.Button(self.scoreFrame, text="RETURN", font=('Courier New italic', 12),
                                    command=self.scoreframetomainframe)
        self.backbutton.place(x=765, y=550)

        # ADMIN FRAME:

        self.admin_view_frame = tk.Frame(self.root, bg='lavender')
        self.admin_tree = ttk.Treeview(self.admin_view_frame, selectmode='browse')
        self.admin_tree.pack(fill='both')

        self.admin_label = tk.Label(self.admin_view_frame,
                                    text="Please enter the admin password together with the username to delete",
                                    font = ('Courier New italic', 12), bg='light goldenrod', relief=tk.GROOVE)
        self.admin_label.place(relx=0.5,rely=0.5, anchor='center')

        self.admin_password_label = tk.Label(self.admin_view_frame, text="ADMIN PASSWORD:",
                                             font=('Courier New italic', 10), bg='light goldenrod')
        self.admin_password_label.place(x=200,y=350)

        self.user_label = tk.Label(self.admin_view_frame, text="USER TO DELETE:", font=('Courier New italic', 10),
                                   bg='light goldenrod')
        self.user_label.place(x=200, y=382)

        self.admin_password_entry = tk.Entry(self.admin_view_frame, width=20, justify=tk.CENTER, show='$', bg='gold',
                                             textvariable=self.admin_password, font=('Courier New', 9))
        self.admin_password.trace_variable("w", self.on_write3)

        self.admin_password_entry.place(y=352, x=340, height=20)

        self.note_label = tk.Label(self.admin_view_frame, text="N.B. Please contact the developer for admin password",
                                   font=('Courier New', 8), bg='lavender', relief=tk.GROOVE)
        self.note_label.place(x=0,y=592, anchor='w')

        self.user_entry_field = tk.Entry(self.admin_view_frame, justify=tk.CENTER, bg='gold',
                                         textvariable=self.user_admin, font=('Courier New', 9))

        self.user_entry_field.place(x=340, y=385, height=20)

        self.delete_button = tk.Button(self.admin_view_frame, text="DELETE RECORD", font=('Courier New italic', 12)
                                       , command=self.delete_user_admin)
        self.delete_button.place(x=340, y=425)

        self.style2 = ttk.Style()
        self.style2.configure("Treeview.Heading", font=('Courier New', 10))
        self.style2.configure("Treeview", font=('Courier New', 10))
        self.admin_tree['show'] = 'headings'
        self.admin_tree['columns'] = "Username"
        self.admin_tree.column("Username", anchor='center')
        self.admin_tree.heading("Username", text="CURRENT USERS", anchor='center')

        self.admin_return_button = tk.Button(self.admin_view_frame, text="RETURN", command=self.admin_frame_to_main,
                                             font=('Courier New italic', 12))
        self.admin_return_button.place(x=765, y=550)

        self.entry1.bind('<space>', lambda e: "break")
        self.entry2.bind('<space>', lambda e: "break")
        self.entry3.bind('<space>', lambda e: "break")
        self.entry4.bind('<space>', lambda e: "break")
        self.admin_password_entry.bind('<space>', lambda e: "break")
        self.user_entry_field.bind('<space>', lambda e: "break")

        self.root.mainloop()

    # FUNCTIONS AND METHODS:--------------------------------------------------------------------------------------------
    # SQL FUNCTIONS:

    def delete_user_admin(self):

        if len(self.user_admin.get()) == 0 or self.admin_password.get() != '1111':
            tkinter.messagebox.showerror("Quiz App - Error", "Missing inputs or wrong password!")

        elif self.admin_password.get() == '1111':
            with sqlite3.connect("userdata.db") as db:
                cursur_delete = db.cursor()

            delete_user_statement = "DELETE FROM quizdata WHERE username = ?"
            cursur_delete.execute(delete_user_statement, [self.user_admin.get()])

            tkinter.messagebox.showinfo("Quiz App - Information", "User deleted!")

            self.admin_password_entry.delete(0, 'end')
            self.user_entry_field.delete(0, 'end')
            db.commit()
            db.close()

        else:

            with sqlite3.connect("userdata.db") as db:

                cursur_exists = db.cursor()
                cursur_exists_statement = \
                    "SELECT EXISTS(SELECT 1 FROM quizdata WHERE username = ? COLLATE NOCASE) LIMIT 1"
                cursur_exists.execute(cursur_exists_statement, [self.user_admin.get()])
                if cursur_exists.fetchall():
                    tkinter.messagebox.showerror("Quiz App - Error", "User not exists!")

            db.commit()
            db.close()

    def create_new_user_func(self):

        self.clearfunc2()

        if len(self.create_user.get()) == 0 or len(self.var.get()) == 0:

            tkinter.messagebox.showerror("Quiz App - Error", "Please enter a username and/or password!")

        else:

            with sqlite3.connect("userdata.db") as db:

                cursur = db.cursor()

            find_user = "SELECT * FROM quizdata WHERE username = ? COLLATE NOCASE"
            cursur.execute(find_user,[(self.create_user.get())])
            if cursur.fetchall():
                tkinter.messagebox.showerror("Quiz App - Error", "Username taken!")

            else:
                self.created_message()
                self.mainFrame.pack_forget()
                self.frame2.pack(fill="both", expand=True)
                insert = 'INSERT INTO quizdata(username,password,score,score2) VALUES(?,?,0,0)'
                cursur.execute(insert,[(self.create_user.get()),(self.var.get())])
                print("Now logged in as:")
                print(self.create_user.get())
                db.commit()
                db.close()

    def login_user_func(self):

        self.clearfunc1()

        with sqlite3.connect("userdata.db") as db:

            cursur = db.cursor()

        see_user = 'SELECT * FROM quizdata WHERE username = ? AND password = ?'
        cursur.execute(see_user, [(self.login_user.get()),(self.var2.get())])
        result = cursur.fetchall()
        if result:
            self.mainFrame.pack_forget()
            self.login_message()
            self.frame2.pack(fill="both",expand=True)
            print("Now logged in as:")
            print(self.login_user.get())
            # self.another_label = tk.Label(self.frame2,text="Now logged in as: ",bg='light blue',
            #                               font=('Courier New italic', 8))
            # self.another_label.place(x=700)
            #
            # self.current_user_label = tk.Label(self.frame2,textvariable=(
            # self.login_user or self.create_user),bg='light blue',
            #                              font=('Courier New italic', 8), relief="groove")
            # self.current_user_label.place(y=20, x=750)

        else:
            tkinter.messagebox.showerror("Quiz App - Error", "   Login Error:\n\nIncorrect details!")
            db.close()

    def user_score_func(self):

        with sqlite3.connect("userdata.db") as db:

            cursur = db.cursor()

        cursur.execute("UPDATE quizdata SET score = ? WHERE username = ?",
                       (self.score,self.login_user.get() or self.create_user.get()))
        db.commit()
        db.close()

    def user_score_func2(self):

        with sqlite3.connect("userdata.db") as db:

            cursur = db.cursor()

        cursur.execute("UPDATE quizdata SET score2 = ? WHERE username = ?",
                       (self.score1,self.login_user.get() or self.create_user.get()))
        db.commit()
        db.close()

    def scoreboard_view(self):

        self.mainFrame.pack_forget()
        self.scoreFrame.pack(fill="both", expand=True)

        conn = sqlite3.connect("userdata.db")
        cursor1 = conn.cursor()
        cursor1.execute("SELECT username, score, score2 FROM quizdata ORDER BY score DESC")
        rows = cursor1.fetchall()

        for row in rows:
            self.scoreFrame.insert('', 'end', values=row)
        conn.close()

    def admin_func(self):

        self.mainFrame.pack_forget()
        self.admin_view_frame.pack(fill='both',expand=True)

        connection = sqlite3.connect("userdata.db")
        cursor2 = connection.cursor()
        cursor2.execute("SELECT username FROM quizdata")
        rows2 = cursor2.fetchall()

        for row in rows2:
            self.admin_tree.insert('', 'end', values=row)
        connection.close()

    # GENERAL FUNCTIONS:

    def admin_frame_to_main(self):

        self.admin_view_frame.pack_forget()
        self.clearfunc2()
        self.clearfunc1()
        self.admin_password_entry.delete(0, 'end')
        self.user_entry_field.delete(0, 'end')
        for i in self.admin_tree.get_children():
            self.admin_tree.delete(i)
        self.mainFrame.pack(fill='both', expand=True)

    def login_message(self):

        DURATION = 700
        self.top = tk.Toplevel(bg='azure3')
        self.top.geometry("295x100+800+460")
        self.top.resizable(False, False)
        self.top.title("Quiz App - Information")
        self.top.iconbitmap("logo.ico")
        self.top_message = tk.Label(self.top, text="LOGIN SUCCESS!", font=('Courier New italic', 12),
                                    bg='azure3')
        self.top_message.pack(padx=20, pady=35)
        self.top.after(DURATION, self.top.destroy)

    def created_message(self):

        DURATION2 = 700
        self.top2 = tk.Toplevel(bg='azure3')
        self.top2.geometry("295x100+800+460")
        self.top2.resizable(False, False)
        self.top2.title("Quiz App - Information")
        self.top2.iconbitmap("logo.ico")
        self.top2_message = tk.Label(self.top2, text="ACCOUNT CREATED!", font=('Courier New italic', 12), bg='azure3')
        self.top2_message.pack(padx=20, pady=35)
        self.top2.after(DURATION2, self.top2.destroy)

    def on_write(self, *args):

        self.s = self.var.get()
        if len(self.s) > self.max_len:
            self.var.set(self.s[:self.max_len])

    def on_write2(self, *args):

        self.s2 = self.var2.get()
        if len(self.s2) > self.max_len2:
            self.var2.set(self.s2[:self.max_len2])

    def on_write3(self, *args):

        self.s3 = self.admin_password.get()
        if len(self.s3) > self.max_len3:
            self.admin_password.set(self.s3[:self.max_len3])

    def exitHover2(self, event):

        self.exitButton2['bg'] = 'IndianRed'

    def exitHover(self, event):

        self.exitButton['bg'] = 'IndianRed'

    def hover2(self, event):

        self.login['bg'] = 'LightSteelBlue'
        self.startButton2['bg'] = "goldenrod1"

    def hover(self, event):

        self.startButton['bg'] = "goldenrod1"
        self.create["bg"] = 'goldenrod1'

    def hoverLeave(self, enter):

        self.startButton['bg'] = "SystemButtonFace"
        self.startButton2['bg'] = "SystemButtonFace"
        self.exitButton2['bg'] = "SystemButtonFace"
        self.exitButton['bg'] = "SystemButtonFace"
        self.login['bg'] = "SystemButtonFace"
        self.create["bg"] = "SystemButtonFace"

    def frame1to2(self):
        self.mainFrame.pack_forget()
        self.frame2.pack(fill="both", expand=True)

    def frame2to1(self):

        self.frame2.pack_forget()
        print("Logged out:")
        print(self.login_user.get() or self.create_user.get())
        self.clearfunc1()
        self.clearfunc2()
        self.mainFrame.pack(fill="both", expand=True)

    def frame2to3(self):

        self.frame2.pack_forget()
        self.frame3.pack(fill="both", expand=True)

        now = datetime.now()
        self.dt_string = now.strftime("%d/%m/%Y %H:%M:%S")

        print("Started Quiz 1 at:", self.dt_string)

        self.q_no = 0
        self.display_question()
        self.opt_selected = tk.IntVar()
        self.opts = self.radio_buttons()
        self.display_options()
        self.buttons()
        self.data_size = len(question)
        self.correct = 0

    def frame2to5(self):

        self.frame2.pack_forget()
        self.frame5.pack(fill="both", expand=True)

        now2 = datetime.now()
        self.dt_string2 = now2.strftime("%d/%m/%Y %H:%M:%S")

        print("Started Quiz 2 at:", self.dt_string2)

        self.q_no1 = 0
        self.display_question1()
        self.opt_selected1 = tk.IntVar()
        self.opts1 = self.radio_buttons1()
        self.display_options1()
        self.buttons1()
        self.data_size1 = len(question1)
        self.correct1 = 0

    def scoreframetomainframe(self):

        self.scoreFrame.pack_forget()
        self.clearfunc1()
        self.clearfunc2()
        for i in self.scoreFrame.get_children():
            self.scoreFrame.delete(i)
        self.mainFrame.pack(fill="both", expand=True)

    def clearfunc1(self):

        self.entry1.delete(0, 'end')
        self.entry2.delete(0, 'end')

    def clearfunc2(self):

        self.entry3.delete(0, 'end')
        self.entry4.delete(0, 'end')

    def frame4tomain(self):

        self.frame4.pack_forget()
        # self.clearfunc1()
        # self.clearfunc2()
        self.frame2.pack(fill="both", expand=True)

    def frame6tomain(self):

        self.frame6.pack_forget()
        # self.clearfunc1()
        # self.clearfunc2()
        self.frame2.pack(fill="both", expand=True)

    # QUIZ 1 LOGIC:-----------------------------------------------------------------------------------------------------

    def display_result(self):

        self.frame3.pack_forget()
        self.frame4.pack(fill="both", expand=True)

        wrong_count = self.data_size - self.correct
        correct = f"Correct: {self.correct}"
        wrong = f"Wrong: {wrong_count}"

        self.score = int(self.correct / self.data_size * 100)
        self.result = f"Score: {self.score}%"

        print("------------------------------------------------------")
        print("Quiz 1")
        print("User:", self.login_user.get() or self.create_user.get())
        print("Result", f"{self.result}\n{correct}\n{wrong}")
        print("------------------------------------------------------")

        self.user_score_func()

        self.end_label = tk.Label(self.frame4, text="THANKS FOR PLAYING!", anchor='center',
                                  font=('Cambria bold italic', 20))
        self.end_label.place(x=285, y=50)

        self.score_numbers = tk.Label(self.frame4, text=f"{self.result}\n\n{correct} and {wrong}",
                                      font=('Courier New italic', 12), relief="ridge")
        self.score_numbers.place(x=300, y=120)

        self.finish = tk.Button(self.frame4, text="EXIT", font=('Courier New italic', 12), command=self.close)
        self.finish.place(x=780, y=550)

        self.go_back_to_main_menu = tk.Button(self.frame4, text="RETURN QUIZ SCREEN", command=self.frame4tomain,
                                              font=('Courier New italic', 12))
        self.go_back_to_main_menu.place(x=30, y=550)

        # if self.score == 100:
        #
        #     self.good_label = tk.Label(self.frame4,text="Well done, you got every question right!"
        #     ,font=('Courier New italic',12))
        #     self.good_label.place(x=220,y=200)
        #
        #     self.good_label2 = tk.Label(self.frame4,text="You really are a hardcore gamer! ;)"
        #     ,font=('Courier New italic',12))
        #     self.good_label2.place(x=250,y=240)


    def check_ans(self, q_no):

        if self.opt_selected.get() == answer[q_no]:
            return True

    def next_btn(self):

        if self.check_ans(self.q_no):
            self.correct += 1
        self.q_no += 1

        if self.q_no == self.data_size:

            self.display_result()

        else:
            self.display_question()
            self.display_options()

    def buttons(self):

        self.next_button = tk.Button(self.frame3, text="NEXT", command=self.next_btn, font=('Courier New italic', 12))
        self.next_button.place(x=780, y=550)

        self.quit_button = tk.Button(self.frame3, text="RETURN", command=self.quit_button_one,
                                     font=('Courier New italic', 12))
        self.quit_button.place(x=30, y=550)

    def display_options(self):
        val = 0

        self.opt_selected.set(0)

        for option in options[self.q_no]:
            self.opts[val]['text'] = option
            val += 1

    def display_question(self):

        q_no = tk.Label(self.frame3, text=question[self.q_no], width=82, anchor='nw', font=('Cambria bold', 13))
        q_no.place(x=50, y=100)

    def radio_buttons(self):

        q_list = []

        y_pos = 200

        while len(q_list) < 4:
            self.radio_btn = tk.Radiobutton(self.frame3, text=" ", variable=self.opt_selected, value=len(q_list) + 1,
                                            anchor='w', width=80, font=('Consolas italic', 12))
            q_list.append(self.radio_btn)

            self.radio_btn.place(x=100, y=y_pos)
            y_pos += 70
        return q_list

    # QUIZ 2 LOGIC:-----------------------------------------------------------------------------------------------------

    def display_result1(self):

        self.frame5.pack_forget()
        self.frame6.pack(fill="both", expand=True)

        wrong_count1 = self.data_size1 - self.correct1
        correct1 = f"Correct : {self.correct1}"
        wrong1 = f"Wrong : {wrong_count1}"

        self.score1 = int(self.correct1 / self.data_size1 * 100)
        result1 = f"Score: {self.score1}%"

        print("------------------------------------------------------")
        print("Quiz 2")
        print("User:", self.login_user.get() or self.create_user.get())
        print("Result", f"{result1}\n{correct1}\n{wrong1}")
        print("------------------------------------------------------")

        self.user_score_func2()

        self.end_label1 = tk.Label(self.frame6, text="THANKS FOR PLAYING!", anchor='center',
                                   font=('Cambria bold italic', 20))
        self.end_label1.place(x=285, y=50)

        self.score_numbers1 = tk.Label(self.frame6, text=f"{result1}\n\n{correct1} and {wrong1}",
                                       font=('Courier New italic', 12), relief="ridge")
        self.score_numbers1.place(x=300, y=120)

        self.finish1 = tk.Button(self.frame6, text="EXIT", font=('Courier New italic', 12), command=self.close)
        self.finish1.place(x=780, y=550)

        self.go_back_to_main_menu1 = tk.Button(self.frame6, text="RETURN QUIZ SCREEN", command=self.frame6tomain,
                                               font=('Courier New italic', 12))
        self.go_back_to_main_menu1.place(x=30, y=550)

    def check_ans1(self, q_no1):

        if self.opt_selected1.get() == answer1[q_no1]:
            return True

    def next_btn1(self):

        if self.check_ans1(self.q_no1):
            self.correct1 += 1
        self.q_no1 += 1

        if self.q_no1 == self.data_size1:

            self.display_result1()

        else:
            self.display_question1()
            self.display_options1()

    def buttons1(self):

        self.next_button2 = tk.Button(self.frame5, text="Next", command=self.next_btn1, font=('Courier New italic', 12))
        self.next_button2.place(x=780, y=550)

        self.quit_button2 = tk.Button(self.frame5, text="Return", command=self.quit_button_two,
                                      font=('Courier New italic', 12))
        self.quit_button2.place(x=30, y=550)

    def display_options1(self):

        val1 = 0
        self.opt_selected1.set(0)
        for option in options1[self.q_no1]:
            self.opts1[val1]['text'] = option
            val1 += 1

    def display_question1(self):

        q_no1 = tk.Label(self.frame5, text=question1[self.q_no1], width=82, anchor='nw', font=('Cambria bold', 13))
        q_no1.place(x=50, y=100)

    def radio_buttons1(self):
        q_list1 = []
        y_pos1 = 200

        while len(q_list1) < 4:
            self.radio_btn1 = tk.Radiobutton(self.frame5, text=" ", variable=self.opt_selected1, value=len(q_list1) + 1,
                                             anchor='w', width=80, font=('Consolas italic', 12))
            q_list1.append(self.radio_btn1)

            self.radio_btn1.place(x=100, y=y_pos1)
            y_pos1 += 70
        return q_list1

    def quit_button_one(self):

        if tkinter.messagebox.askyesno("Quiz App - Warning",
                                       "Are you sure you want to return? All points will be lost.") > 0:

            self.frame3.pack_forget()
            self.frame2.pack(fill="both", expand=True)

    def quit_button_two(self):

        if tkinter.messagebox.askyesno("Quiz App - Warning",
                                       "Are you sure you want to return? All points will be lost.") > 0:

            self.frame5.pack_forget()
            self.frame2.pack(fill="both", expand=True)

    def close(self):

        if tkinter.messagebox.askyesno("Quiz App", "Are you sure you want to exit?") > 0:
            self.root.destroy()
            return


with open('data1.json') as f:
    data = json.load(f)

question = (data['question'])
options = (data['options'])
answer = (data['answer'])

with open('data2.json') as f:
    data1 = json.load(f)

question1 = (data1['question'])
options1 = (data1['options'])
answer1 = (data1['answer'])


if __name__ == '__main__':

    main = Main()
