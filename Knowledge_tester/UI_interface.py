from tkinter import Frame, BOTH, Button, messagebox, Listbox, SINGLE, END, Text, Entry

from Knowledge_tester.Core import Test


class Example(Frame):
    def __init__(self, parent):
        Frame.__init__(self, parent, background='white')
        self.parent = parent
        self.test = Test()
        self.create_menu()

    def close(self):
        if messagebox.askyesno('Выход', 'Вы уверены?'):
            self.parent.destroy()

    def find_tests(self):
        self.list_of_topics = Listbox(selectmode=SINGLE)
        for i in self.test.find_test(self.topic.get()):
            self.list_of_topics.insert(END, i)
        self.topic.destroy()
        self.list_of_topics.place(x=144, y=0, height=475, width=706)
        # self.text = Label(text=self.test.find_test('1'), font=10, justify=LEFT)
        # self.text.place(x=144, y=0, height=475, width=706)


    def give_question(self):
        self.number += 1
        self.number_of_question.delete('1.0', END)
        self.number_of_question.insert('1.0', f'Номер вопроса: {self.number} из {self.count}')
        print(self.list_of_answers.curselection())

        self.question_text.delete('1.0', END)
        self.list_of_answers.delete('0', END)

        try:
            self.question_text.insert('1.0', self.questions[self.number-1])
        except IndexError:
            self.number_of_question.delete('1.0', END)
            self.number_of_question.insert('1.0', 'Вы успешно прошли тест!\nДля получения результата оплатите подписку')
            self.btn_accept.destroy()
        for answer in self.answers[self.number-1]:
            self.list_of_answers.insert(END, answer)
        print(self.number, self.count)

    def give_questions(self):
        try:
            self.questions, self.answers = self.test.give_test(int(self.list_of_topics.curselection()[0]) + 1)
        except TypeError:
            self.list_of_topics.delete(self.list_of_topics.curselection())
        self.number = 1
        self.count = len(self.questions)
        self.list_of_topics.destroy()

        self.number_of_question = Text()
        self.number_of_question.insert('1.0', f'Номер вопроса: {self.number} из {self.count}')
        self.number_of_question.place(x=145, y=0, width=706, height=65)

        self.question_text = Text(font=14)
        self.question_text.place(x=145, y=65, width=706, height=65)

        self.list_of_answers = Listbox(selectmode=SINGLE)
        self.list_of_answers.place(x=145, y=130, width=706, height=330)

        self.btn_accept = Button(text='accept', command=self.give_question)
        self.btn_accept.place(x=145, y=461,  width=706, height=90)

        self.question_text.insert('1.0', self.questions[0])
        for answer in self.answers[0]:
            self.list_of_answers.insert(END, answer)


    def create_menu(self):
        self.pack(fill=BOTH, expand=1)
        self.btn_exit = Button(text='Выход', command=self.close)
        self.btn_exit.place(x=0, y=65, height=65, width=144)

        self.topic = Entry()
        self.topic.place(x=145, y=0, width=706, height=65)

        self.btn_find_topic = Button(text='FIND', command=self.find_tests)
        self.btn_find_topic.place(x=0, y=485, height=65, width=144)



        self.btn_questions = Button(text='Вопросы', command=self.give_questions)
        self.btn_questions.place(x=0, y=0, height=65, width=144)
