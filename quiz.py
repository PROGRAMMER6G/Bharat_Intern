import tkinter as tk
from tkinter import messagebox

class QuizApp:
    def __init__(self, root):
        self.root = root
        self.score = 0
        self.current_question = 0

        self.questions = [
            {
                "question": "Which is the largest river in India?",
                "options": ["The Ganges", "Krishna", "Kavery", "Penna"],
                "correct_option": "The Ganges"
            },
            {
                "question": "Which is the longest river in the World?",
                "options": ["Amazon river", "Nile river", "Ganges river", "Indus river"],
                "correct_option": "Nile river"
            },
            {
                "question": "Which state is also known as the “Fruit Bowl” of India?",
                "options": ["Jammu and Kashmir", "Meghalaya", "Assam", "Himachal Pradesh"],
                "correct_option": "Himachal Pradesh"
            },
            {
                "question": "Which place in India is also known as the “Land of Rising Sun?",
                "options": ["Sikkim", "Arunachal Pradesh", "Karnataka", "Gujarat"],
                "correct_option": "Arunachal Pradesh"
            },
            {
                "question": "In terms of area Karnataka is the ______ largest State in India?",
                "options": ["Fifth", "Fourth", "Seventh", "Ninth"],
                "correct_option": "Seventh"
            },
            # Add more questions as needed
        ]

        self.question_label = tk.Label(root, text="")
        self.question_label.pack()
        root.title("Quiz")
        root.geometry("675x215")
        root.resizable(0,0)
        root.configure(bg="#E6E6FA")

        self.radio_var = tk.StringVar()
        self.option_buttons = []
        for i in range(4):
            option_button = tk.Radiobutton(root, text="",font=11,bg='#FFE5B4', variable=self.radio_var, value="", indicatoron=0)
            option_button.pack()
            self.option_buttons.append(option_button)

        self.submit_button = tk.Button(root, text="SUBMIT",font=21,bd=4,bg="light green", command=self.check_answer)
        self.submit_button.pack()

        self.load_question()

    def load_question(self):
        if self.current_question < len(self.questions):
            question_data = self.questions[self.current_question]
            self.question_label.config(text=question_data["question"],font=21,bg='#E6E6FA')
            options = question_data["options"]
            for i in range(4):
                self.option_buttons[i].config(text=options[i], value=options[i])
        else:
            messagebox.showinfo("Quiz Over", f"Quiz Over! Your score: {self.score}/{len(self.questions)}")
            self.root.destroy()

    def check_answer(self):
        user_answer = self.radio_var.get()
        correct_answer = self.questions[self.current_question]["correct_option"]
        if user_answer == correct_answer:
            self.score += 1
        self.current_question += 1
        self.radio_var.set(None)
        self.load_question()

root = tk.Tk()
app = QuizApp(root)
root.mainloop()
