import tkinter as tk
from tkinter import ttk

class OnlineQuiz:
    def __init__(self, root):
        self.root = root
        self.root.title("Online Quiz")

        self.questions = [
            {
                "question": "What is the capital of France?",
                "options": ["Paris", "London", "Berlin", "Madrid"],
                "correct_answer": "Paris"
            },
            {
                "question": "Which planet is known as the Red Planet?",
                "options": ["Earth", "Mars", "Venus", "Jupiter"],
                "correct_answer": "Mars"
            },
            {
                "question": "How many continents are there?",
                "options": ["4", "5", "6", "7"],
                "correct_answer": "7"
            }
        ]

        self.current_question = 0
        self.score = 0

        self.create_question_frame()

    def create_question_frame(self):
        self.question_frame = ttk.Frame(self.root)
        self.question_frame.grid(row=0, column=0, padx=10, pady=10)

        question_data = self.questions[self.current_question]

        question_label = ttk.Label(self.question_frame, text=question_data["question"])
        question_label.grid(row=0, column=0, columnspan=2, padx=10, pady=10)

        self.selected_option = tk.StringVar()

        for idx, option in enumerate(question_data["options"]):
            option_radio = ttk.Radiobutton(
                self.question_frame,
                text=option,
                variable=self.selected_option,
                value=option
            )
            option_radio.grid(row=idx + 1, column=0, columnspan=2, padx=10, pady=5)

        submit_button = ttk.Button(self.question_frame, text="Submit", command=self.check_answer)
        submit_button.grid(row=len(question_data["options"]) + 1, column=0, columnspan=2, padx=10, pady=10)

    def check_answer(self):
        question_data = self.questions[self.current_question]
        selected_answer = self.selected_option.get()
        correct_answer = question_data["correct_answer"]

        if selected_answer == correct_answer:
            self.score += 1

        self.current_question += 1

        if self.current_question < len(self.questions):
            self.question_frame.destroy()
            self.create_question_frame()
        else:
            self.show_result()

    def show_result(self):
        result_frame = ttk.Frame(self.root)
        result_frame.grid(row=0, column=0, padx=10, pady=10)

        result_label = ttk.Label(result_frame, text=f"Quiz Completed! Your score is {self.score}/{len(self.questions)}")
        result_label.grid(row=0, column=0, columnspan=2, padx=10, pady=10)

if __name__ == "__main__":
    root = tk.Tk()
    app = OnlineQuiz(root)
    root.mainloop()