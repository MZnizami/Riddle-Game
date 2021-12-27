from tkinter import *
from PIL import ImageTk, Image
import sqlite3
import tkinter.messagebox


class Riddle_Game:

    #################################### The Register Window#####################################
    ##############################################################################################
    def __init__(self):

        root_main = Tk()
        root_main.geometry("500x600")
        root_main['bg'] = 'lemon chiffon'
        root_main.title("Review Page/ Riddle Game")

        self.label = Label(root_main, text="*Please Register\nBefore Playing the Game*",
                           font=("Times", 16, "bold"),
                           width=90,
                           bg="yellow")
        self.label.place(anchor="center", relx=.5, rely=.050)
        self.name = Label(root_main, text="Name: ", bg="yellow", font=("Times", 16, "bold"))
        self.name.place(anchor="center", relx=.2, rely=.15)
        self.last = Label(root_main, text="LastName: ", bg="yellow", font=("Times", 16, "bold"))
        self.last.place(anchor="center", relx=.2, rely=.23)
        self.coun = Label(root_main, text="Country : ", bg="yellow", font=("Times", 16, "bold"))
        self.coun.place(anchor="center", relx=.2, rely=.3)
        self.email = Label(root_main, text="Email : ", bg="yellow", font=("Times", 16, "bold"))
        self.email.place(anchor="center", relx=.2, rely=.4)
        self.var1 = StringVar()
        self.var2 = StringVar()
        self.var3 = StringVar()
        self.var4 = StringVar()
        self.var5 = StringVar()
        self.name_entry = Entry(root_main, textvariable=self.var1)
        self.name_entry.place(anchor="center", relx=.6, rely=.15, width=200, height=30)
        self.last_entry = Entry(root_main, textvariable=self.var2)
        self.last_entry.place(anchor="center", relx=.6, rely=.23, width=200, height=30)
        self.count_entry = Entry(root_main, textvariable=self.var3)
        self.count_entry.place(anchor="center", relx=.6, rely=.3, width=200, height=30)
        self.email_entry = Entry(root_main, textvariable=self.var4)
        self.email_entry.place(anchor="center", relx=.6, rely=.4, width=200, height=30)
        self.delete_entry = Entry(root_main, textvariable=self.var5)
        self.delete_entry.place(anchor="center", relx=.6, rely=.5, width=200, height=30)

        self.button = Button(root_main, text="delete", width=10, bg="yellow", command=self.delete
                             , font=("Times", 16, "bold")).place(anchor="center", relx=.2, rely=.5)
        self.button2 = Button(root_main, text="insert", width=10, bg="yellow", command=self.insert
                              , font=("Times", 16, "bold")).place(anchor="center", relx=.2, rely=.6)
        self.button3 = Button(root_main, text="show", width=10, bg="yellow", command=self.show
                              , font=("Times", 16, "bold")).place(anchor="center", relx=.5, rely=.6)
        self.button4 = Button(root_main, text="Game", width=10, bg="yellow", command=self.main
                              , font=("Times", 16, "bold")).place(anchor="center", relx=.8, rely=.6)
        self.show_label = Label(root_main, bg='lemon chiffon', font=("Times", 15, "bold"))

        root_main.mainloop()

    #################################### The insert function#####################################
    ##############################################################################################
    def insert(self):
        username = self.var1.get()
        lastname = self.var2.get()
        country = self.var3.get()
        email = self.var4.get()
        connection = sqlite3.connect("register.db")
        # connection.execute('''create table Person(name text, last text, country text, email text)''')
        connection.execute("insert into Person values (?,?,?,?)", (username, lastname, country, email))
        connection.commit()
        result = connection.execute("select * from Person")
        for i in result:
            print(i)
        connection.close()
        tkinter.messagebox.showinfo('Window Title', 'Thank You For the Registration')
        self.name_entry.delete(0, END)
        self.last_entry.delete(0, END)
        self.count_entry.delete(0, END)
        self.email_entry.delete(0, END)
    #################################### The delete#####################################
    ##############################################################################################
    def delete(self):
        connection = sqlite3.connect('register.db')
        # Delete a record

        c = connection.cursor()
        c.execute('''delete from Person  where name =? ''', (self.var5.get(),))

        connection.commit()
        connection.close()
        self.delete_entry.delete(0, END)
    #################################### The show#####################################
    ##############################################################################################
    def show(self):
        conn = sqlite3.connect('register.db')
        c = conn.cursor()
        c.execute("select * from Person")
        records = c.fetchall()
        print_record = ''
        for i in records:
            print_record += str(i[0]) + "\t" + str(i[1]) + "\t" + str(i[2]) + "\t" + str(i[3]) + "\n"
        self.show_label.configure(text=print_record)
        self.show_label.place(anchor="center", relx=.5, rely=.8)
        conn.commit()
        conn.close()

    #################################### The main Game#####################################
    ##############################################################################################

    def main(self):

        window1 = Toplevel()
        window1.geometry("2000x800")
        window1['bg'] = 'papaya whip'

        insta = Image.open(r"img\\imageedit_3_8414519649.png")
        resize_insta = insta.resize((60, 50), Image.ANTIALIAS)
        resized2_insta = ImageTk.PhotoImage(resize_insta)
        insta_label = Label(window1, image=resized2_insta, bg='papaya whip')
        insta_label.place(anchor='center', relx=.050, rely=.060)

        twi = Image.open(r"img\\Twitter.png")
        resize_twi = twi.resize((60, 50), Image.ANTIALIAS)
        resized2_twi = ImageTk.PhotoImage(resize_twi)
        twi_label = Label(window1, image=resized2_twi, bg='papaya whip')
        twi_label.place(anchor='center', relx=.12, rely=.060)

        face = Image.open(r"img\\imageedit_3_3069034082.png")
        resize_face = face.resize((60, 50), Image.ANTIALIAS)
        resized2_face = ImageTk.PhotoImage(resize_face)
        face_label = Label(window1, image=resized2_face, bg='papaya whip')
        face_label.place(anchor='center', relx=.2, rely=.060)
        text = Label(window1, text="Welcome to **Riddle Game**\n Please choose any level ", bg='lemon chiffon'
                     , font=("Times", 20, 'bold'))
        text.place(anchor='center', relx=.5, rely=.15)

        photo = Image.open(r"img\\easy.gif")
        resize_photo = photo.resize((200, 250), Image.ANTIALIAS)
        resized = ImageTk.PhotoImage(resize_photo)
        button1 = Button(window1, image=resized,
                         bg='yellow', command=self.easy)
        button1.place(anchor='center', relx=.2, rely=.5)
        label1 = Label(window1, text="Easy", font=("Times", 16), width=10, bg="yellow")
        label1.place(anchor='center', relx=.2, rely=.7)

        photo1 = Image.open(r"img\\medium.gif")
        resize_photo1 = photo1.resize((200, 250), Image.ANTIALIAS)
        resized1 = ImageTk.PhotoImage(resize_photo1)
        button2 = Button(window1, image=resized1,
                         bg='yellow', command= self.medium)
        button2.place(anchor='center', relx=.5, rely=.5)
        label2 = Label(window1, text="Medium", font=("Times", 16), width=10, bg="yellow")
        label2.place(anchor='center', relx=.5, rely=.7)

        photo2 = Image.open(r"img\\hard.gif")
        resize_photo2 = photo2.resize((200, 250), Image.ANTIALIAS)
        resized2 = ImageTk.PhotoImage(resize_photo2)
        button3 = Button(window1, image=resized2,
                         bg='yellow')
        button3.place(anchor='center', relx=.8, rely=.5)
        label3 = Label(window1, text="Hard", font=("Times", 16), width=10, bg="yellow")
        label3.place(anchor='center', relx=.8, rely=.7)
        ############Three level buttons finishes###############################
        ############This is for the icons and buttons ###############################

        icon1 = PhotoImage(file=r"img\\review.gif")
        b1 = Button(window1, image=icon1, bd=0, command=self.signup)
        b1.place(anchor='center', relx=.3, rely=.9)
        icon2 = PhotoImage(file=r"img\\exit.gif")
        b2 = Button(window1, image=icon2, bd=0, command= window1.destroy)
        b2.place(anchor='center', relx=.6, rely=.9)
        ############icons and buttons are finished ###############################
        mainloop()

    #################################### The Easy level #####################################
    ##############################################################################################

    def easy(self):
        root = Toplevel()
        root.title("Easy Level Of Riddle Game")
        root.geometry("2000x800")
        root['bg'] = 'lemon chiffon'

        self.review = PhotoImage(file=r"img\\review.gif")

        self.b1 = Button(root, image=self.review, bg='lemon chiffon', bd=0, command=self.signup)
        self.b1.place(anchor='center', relx=.1, rely=.1)
        self.exit = PhotoImage(file=r"img\\exit.gif")
        self.b2 = Button(root, image=self.exit, bg='lemon chiffon', bd=0, command=root.destroy)
        self.b2.place(anchor='center', relx=.9, rely=.1)
        self.text = Label(root, text="**Easy Level**\nAnswer the Riddle and win The Treasure Box", bg='lemon chiffon'
                          , font=("Times", 20, 'bold'))
        self.text.place(anchor='center', relx=.4, rely=.1)

        self.load = Image.open(r"img\\point.png")
        self.resize_photo = self.load.resize((300, 300), Image.ANTIALIAS)
        self.render = ImageTk.PhotoImage(self.resize_photo)
        self.labelImg = Label(root, image=self.render, bg='lemon chiffon')
        self.labelImg.place(anchor='center', relx=.8, rely=.4)
        ############# the questions1 box##################
        self.label = Label(root,
                           bg='white', width='90', height='20')
        self.label.place(anchor='center', relx=.3, rely=.4)
        self.question = Label(root, text="Question: What has to be broken before you can use it?", font="Times",
                              bg='lemon chiffon')
        self.question.place(anchor='e', relx=.4, rely=.4)

        ###############the answer entry box#####################
        self.answer = Label(root, text="Write Your Answer", font="Times", bg='lemon chiffon')
        self.answer.place(anchor='e', relx=.2, rely=.7)
        self.var = StringVar()

        self.e1 = Entry(root, textvariable=self.var)
        self.e1.place(anchor='center', relx=.3, rely=.7, width=200, height=50)
        self.icon1 = PhotoImage(file=r"img\\check.gif")
        self.check = Button(root, text="check", command=self.question1, image=self.icon1, bd=0, bg= 'lemon chiffon')
        self.check.place(anchor='center', relx=.5, rely=.7)
        self.icon2 = PhotoImage(file=r"img\\next.gif")
        self.level = Button(root, text="level medium", command=self.medium, image=self.icon2, bd=0,bg= 'lemon chiffon')
        self.level.place(anchor='center', relx=.7, rely=.7)
    #################################### The Easy Question checker #####################################
    ##############################################################################################
    def question1(self):
        ans = self.var.get()

        y = "egg"


        if ans == y:

            prize = Toplevel()
            prize.geometry("500x400")


            image = PhotoImage(file=r"img\\treasure.png")
            label = Label(prize, image=image)
            label.place(x=0, y=0, relwidth=1, relheight=1)
            prize_text = Label(prize, text="You Won\n The treasure", font= ('Times', 16, 'bold'))
            prize_text.place(anchor='center', relx=.2, rely=.2)
            prize.mainloop()
        else:

            prize = Toplevel()
            prize.geometry("600x500")
            prize.title("Review Page/ Riddle Game")
            image = PhotoImage(file=r"img\\disapp.gif")
            label = Label(prize, image=image)
            label.place(x=0, y=0, relwidth=1, relheight=1)
            prize_text = Label(prize, text="Sorry You Lost", font=('Times', 16, 'bold'))
            prize_text.place(anchor='center', relx=.3, rely=.1)
            prize.mainloop()
        #################################### The Medium level #####################################
        ##############################################################################################

    def medium(self):
        root = Toplevel()
        root.title("Easy Level Of Riddle Game")
        root.geometry("2000x800")
        root['bg'] = 'lemon chiffon'

        self.review = PhotoImage(file=r"img\\review.gif")

        self.b1 = Button(root, image=self.review, bg='lemon chiffon', bd=0, command=self.signup)
        self.b1.place(anchor='center', relx=.1, rely=.1)
        self.exit = PhotoImage(file=r"img\\exit.gif")
        self.b2 = Button(root, image=self.exit, bg='lemon chiffon', bd=0,command=root.quit)
        self.b2.place(anchor='center', relx=.9, rely=.1)
        self.text = Label(root, text="**Medium Level**\nAnswer the Riddle and win The Treasure", bg='lemon chiffon'
                          , font=("Times", 18))
        self.text.place(anchor='center', relx=.4, rely=.1)

        self.load = Image.open(r"img\\point.png")
        self.resize_photo = self.load.resize((300, 300), Image.ANTIALIAS)
        self.render = ImageTk.PhotoImage(self.resize_photo)
        self.labelImg = Label(root, image=self.render, bg='lemon chiffon')
        self.labelImg.place(anchor='center', relx=.8, rely=.4)
        ############# the questions1 box##################
        self.label = Label(root,
                           bg='white', width='90', height='20')
        self.label.place(anchor='center', relx=.3, rely=.4)
        self.question = Label(root, text="Question: No matter how little or how much you use me,\nyou change me every month. What am I?", font="Times",
                              bg='lemon chiffon')
        self.question.place(anchor='e', relx=.4, rely=.4)

        ###############the answer entry box#####################
        self.answer = Label(root, text="Write Your Answer", font="Times", bg='lemon chiffon')
        self.answer.place(anchor='e', relx=.2, rely=.7)
        self.var = StringVar()

        self.e1 = Entry(root, textvariable=self.var)
        self.e1.place(anchor='center', relx=.3, rely=.7, width=200, height=50)
        self.icon1 = PhotoImage(file=r"img\\check.gif")
        self.check = Button(root, text="check",  command=self.question2, image=self.icon1, bd=0, bg='lemon chiffon')
        self.check.place(anchor='center', relx=.5, rely=.7)
        self.icon2 = PhotoImage(file=r"img\\next.gif")
        self.level = Button(root, text="level medium", image=self.icon2, bd=0,
                            bg='lemon chiffon')
        self.level.place(anchor='center', relx=.7, rely=.7)
        #################################### The Medium Question checker #####################################
        ##############################################################################################

    def question2(self):
        ans = self.var.get()
        x = "calender"


        if ans == x:

            prize = Toplevel()
            prize.geometry("500x400")

            image = PhotoImage(file=r"img\\treasure.png")
            label = Label(prize, image=image)
            label.place(x=0, y=0, relwidth=1, relheight=1)
            prize_text = Label(prize, text="You Won\n The treasure", font=('Times', 16, 'bold'))
            prize_text.place(anchor='center', relx=.2, rely=.2)
            prize.mainloop()
        else:

            prize = Toplevel()
            prize.geometry("600x500")

            image2 = PhotoImage(file=r"img\\disapp.gif")
            label2 = Label(prize, image=image2)
            label2.place(x=0, y=0, relwidth=1, relheight=1)
            prize_text = Label(prize, text="Sorry You Lost", font=('Times', 16, 'bold'))
            prize_text.place(anchor='center', relx=.3, rely=.1)
            prize.mainloop()

    #################################### Review page #####################################
    ##############################################################################################
    def signup(self):
        self.master = Toplevel()
        self.master.geometry("500x400")
        self.master.title("Review Page/ Riddle Game")
        self.background_image = PhotoImage(file=r"img\\signup.gif")
        self.background_label = Label(self.master, image=self.background_image)
        self.background_label.place(x=0, y=0, relwidth=1, relheight=1)
        self.label = Label(self.master, text="*Please Gives Us\n Your Review of The Game*", font=("Times", 20, "bold"),
                           width=90,
                           bg="yellow")
        self.label.place(anchor="center", relx=.5, rely=.080)
        self.name = Label(self.master, text="Name: ", bg="yellow", font=("Times", 16, "bold"))
        self.name.place(anchor="center", relx=.2, rely=.3)
        self.email = Label(self.master, text="Email: ", bg="yellow", font=("Times", 16, "bold"))
        self.email.place(anchor="center", relx=.2, rely=.4)
        self.password = Label(self.master, text="Review : ", bg="yellow", font=("Times", 16, "bold"))
        self.password.place(anchor="center", relx=.2, rely=.5)
        self.var1 = StringVar()
        self.var2 = StringVar()
        self.var3 = StringVar()
        self.name_entry = Entry(self.master, textvariable=self.var1)
        self.name_entry.place(anchor="center", relx=.6, rely=.3, width=200, height=30)
        self.email_entry = Entry(self.master, textvariable=self.var3)
        self.email_entry.place(anchor="center", relx=.6, rely=.4, width=200, height=30)
        self.pass_entry = Entry(self.master, textvariable=self.var2)
        self.pass_entry.place(anchor="center", relx=.6, rely=.6, width=250, height=100)
        self.button = Button(self.master, text="sign_up", width=20, command=self.database, bg="yellow",
                             font=("Times", 16, "bold")).place(anchor="center", relx=.5, rely=.8)
        self.master.mainloop()

    #################################### adding to the review database #####################################
    ##############################################################################################
    def database(self):
        username = self.var1.get()
        password = self.var2.get()
        email = self.var3.get()
        connection = sqlite3.connect("review.db")
        connection.execute("insert into user values (?,?,?)", (username, password, email))
        connection.commit()
        result = connection.execute("select * from user")
        for i in result:
            print(i)
        connection.close()
        tkinter.messagebox.showinfo('Window Title', 'Thank You For your review')
        self.master.quit()

Riddle_Game()
