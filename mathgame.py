import random
import tkinter as tk

class MathQuiz:
    def __init__(self):
        self.w = tk.Tk()
        self.w.config(bg="green")
        self.w.title("Math Quiz")

        self.timer_label = tk.Label(self.w, text="10.0", bg="white", width=10, font=("", 10, "bold"))
        self.timer_label.place(y=530, x=250)

        self.question_label = tk.Label(self.w, text="", bg="white", font=("", 10, "bold"), width=20, height=3)
        self.question_label.place(y=380, x=133)

        self.score_label = tk.Label(self.w, text="Score: 0", bg="white", font=("", 10, "bold"))
        self.score_label.place(y=322, x=290)

        self.answer_buttons = []
        for i in range(4):
            button = tk.Button(self.w, bg="white", relief="ridge", width=7, height=4, text="",
                               font=("", 10, "bold"), command=lambda i=i: self.check_answer(i))
            self.answer_buttons.append(button)

        self.place_answer_buttons()

        self.time_remaining = 10.0
        self.score = 0
        self.current_question = ""
        self.generate_question()
        self.update_timer()

    def place_answer_buttons(self):
        positions = [(100, 650), (400, 650), (100, 900), (400, 900)]
        for i, position in enumerate(positions):
            self.answer_buttons[i].place(y=position[1], x=position[0])

    def generate_question(self):
        num1 = random.randint(1, 20)
        num2 = random.randint(1, 20)
        self.current_question = f"{num1} + {num2}"
        self.question_label.config(text=self.current_question)
        correct_answer = num1 + num2
        answers = [correct_answer]
        while len(answers) < 4:
            random_answer = random.randint(2, 40)
            if random_answer != correct_answer and random_answer not in answers:
                answers.append(random_answer)
        random.shuffle(answers)
        for i in range(4):
            self.answer_buttons[i].config(text=answers[i])

    def check_answer(self, button_index):
        selected_answer = self.answer_buttons[button_index].cget("text")
        correct_answer = eval(self.current_question)
        if int(selected_answer) == correct_answer:
            self.score += 1
        self.generate_question()
        self.update_score()

    def update_score(self):
        self.score_label.config(text=f"Score: {self.score}")

    def update_timer(self):
        if self.time_remaining > 0:
            self.time_remaining -= 0.1
            self.timer_label.config(text=f"{self.time_remaining:.1f}")
            self.w.after(100, self.update_timer)
        else:
            self.show_result()

    def show_result(self):
        self.timer_label.config(text="Time's up!")
        self.question_label.config(text=f"Final Score: {self.score}/10")
        for button in self.answer_buttons:
            button.config(state=tk.DISABLED)

    def start(self):
        self.w.mainloop()


if __name__ == "__main__":
    quiz = MathQuiz()
    quiz.start()

