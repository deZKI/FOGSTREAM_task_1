from tkinter import Frame, Button, messagebox, Listbox, SINGLE, END, Text, Entry, Label

from PIL import Image, ImageTk

from Knowledge_tester.Core import Test


class Example(Frame):
    def __init__(self, parent):
        Frame.__init__(self, parent, background='white')
        self.parent = parent
        self.test = Test()
        self.create_topic_menu()

    def find_tests(self):
        topics = self.test.find_test(self.topic.get())
        if topics == 'Тесты не найдены!':
            self.topic.delete(0, END)
            self.topic.insert(0, topics)
            return
        self.create_test_menu()
        for i in topics:
            self.list_of_topics.insert(END, i)


    def give_question(self):
        self.number += 1
        self.number_of_question.delete('1.0', END)
        self.number_of_question.insert('1.0', f'Номер вопроса: {self.number} из {self.count}')
        print(self.list_of_answers.curselection())

        self.question_text.delete('1.0', END)
        self.list_of_answers.delete('0', END)

        try:
            question, answers = self.questions_answers.__next__()
        except StopIteration:
            self.img_label.destroy()
            self.create_end_menu()
        else:
            self.question_text.insert('1.0', question)
            for answer in answers:
                self.list_of_answers.insert(END, answer)
            if self.test.has_img == True:
                self.change_question_pic()

    def give_questions(self):
        self.questions_answers = self.test.give_test(int(self.list_of_topics.curselection()[0]) + 1)
        question, answers = self.questions_answers.__next__()
        self.number = 1
        self.count = self.test.count_of_questions
        self.create_question_menu()
        self.question_text.insert('1.0', question)
        for answer in answers:
            self.list_of_answers.insert(END, answer)
        if self.test.has_img == True:
            self.change_question_pic()


    def create_topic_menu(self):
        self.topic = Entry()
        self.topic.place(x=0, y=0, width=700, height=65)

        self.btn_find_topic = Button(text='Найти', command=self.find_tests)
        self.btn_find_topic.place(x=700, y=0, height=65, width=150)

    def create_test_menu(self):
        self.btn_questions = Button(text='Подтвердить', command=self.give_questions)
        self.btn_questions.place(x=0, y=0, height=65, width=144)
        self.list_of_topics = Listbox(selectmode=SINGLE, font=('Arial', 15))
        self.list_of_topics.place(x=144, y=0, height=330, width=706)
        self.topic.destroy()

    def create_question_menu(self):
        self.btn_find_topic.destroy()
        self.btn_questions.destroy()
        self.list_of_topics.destroy()
        self.number_of_question = Text(font=('Arial', 30))
        self.number_of_question.insert('1.0', f'Номер вопроса: {self.number} из {self.count}')
        self.number_of_question.place(x=20, y=0, width=810, height=50)

        self.question_text = Text(font=('Arial', 20))
        self.question_text.place(x=20, y=50, width=810, height=50)

        self.img_label = Label()
        self.img_label.place(x=20, y=90, width=810, height=400)

        self.list_of_answers = Listbox(selectmode=SINGLE, font=('Arial', 14))
        self.list_of_answers.place(x=20, y=500, width=810, height=100)

        self.btn_accept = Button(text='Подтвердить', command=self.give_question)
        self.btn_accept.place(x=20, y=600, width=810, height=50)

    def change_question_pic(self):
        img = ImageTk.PhotoImage(
            Image.open('/Users/kirill201/PycharmProjects/FOGSTREAM_task_1/Knowledge_tester/img/1.png'))
        self.img_label.configure(image=img)
        self.img_label.image = img

    def create_end_menu(self):
        self.list_of_answers.destroy()
        self.btn_accept.destroy()
        self.number_of_question.destroy()
        self.question_text.destroy()

        msgbox = messagebox.askquestion('Поздравляю', '''Вы успешно прошли тест!\n
                                                      Для получения результата оплатите подписку\n
                                                      \nНачать заново''')
        if msgbox == 'yes':
            self.create_topic_menu()
        else:
            self.parent.destroy()
        # self.end_text = Text(font=('Arial', 20))
        # self.end_text.place(x=20, y=65, width=810, height=65)
        # self.end_text.insert('1.0', 'Вы успешно прошли тест!\nДля получения результата оплатите подписку')
        #
        # self.btn_restart = Button(text='restart', command=self.create_topic_menu)
        # self.btn_restart.place(x=20, y=461, width=810, height=90)



