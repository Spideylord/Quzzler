from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"

class QuizUi:
    def __init__(self , quiz_brain : QuizBrain ):
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(bg=THEME_COLOR , padx=20 , pady= 20)
        self.canvas = Canvas(height=250 , width= 300 , highlightthickness=0 , bg="white" )
        self.question_text = self.canvas.create_text(150 , 125,text= "question" , font=("Arial" , 20 , "italic") , fill=THEME_COLOR , width=280)
        self.canvas.grid(row = 1 , column = 0 , columnspan = 2 , pady = 50)
        #correct button
        correct_image = PhotoImage( file = "images/true.png")
        self.correct = Button(image=correct_image , highlightthickness=0 , command=self.tick)
        self.correct.grid(row = 2 , column = 0)
        #wrong button
        wrong_image =PhotoImage( file = "images/false.png")
        self.wrong = Button(image=wrong_image , highlightthickness=0 , command=self.cross)
        self.wrong.grid(row = 2 , column = 1)
        #score handling
        self.score = Label(text= f"score = {self.quiz.score}" , bg=THEME_COLOR , fg="white" )
        self.score.grid(row = 0 , column = 1 )

        self.next_q()

        self.window.mainloop()

    def next_q(self):
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():
            q = self.quiz.next_question()
            self.score.config(text = f"Score = {self.quiz.score}")
            self.canvas.itemconfig(self.question_text , text = q)
        else :
            self.canvas.itemconfig(self.question_text , text = "There are no more questions left !!")
            self.correct.config(state="disabled")
            self.wrong.config(state="disabled")




    def tick(self):
        self.give_feedback(self.quiz.check_answer("true"))
    def cross(self):
        self.give_feedback(self.quiz.check_answer("false"))

    def give_feedback(self , is_right):
        if is_right is True:
            self.canvas.config(bg="green")
            self.window.after(1000 , self.next_q)
        else :
            self.canvas.config(bg="red")
            self.window.after(1000, self.next_q)


