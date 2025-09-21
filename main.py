import tkinter as tk
from tkinter import messagebox, ttk
from ttkbootstrap import Style
from quiz import quiz

root = tk.Tk()
root.title("لعبة أسئلة في مجال الحاسب")
root.geometry("600x500")

style = Style(theme="darkly")  

style.configure("TLabel", font=("Cairo", 16))
style.configure("TButton", font=("Cairo", 14), foreground="white", background="#1E90FF")
style.map(
    "TButton",
    background=[("active", "#4682B4")],
)

title_label = tk.Label(
    root,
    text="✦ لعبة أسئلة في مجال الحاسب ✦",
    font=("Cairo", 22, "bold"),
    fg="#00BFFF",
    bg="#2E2E2E",
    anchor="center",
    justify="center"
)
title_label.pack(pady=15, fill="x")

qs_label = ttk.Label(
    root, 
    anchor="center",
    justify="center",
    wraplength=500,
    padding=10
)
qs_label.pack(pady=10, fill="x")

feedback_label = ttk.Label(
    root,
    anchor="center",
    justify="center",
    padding=10
)
feedback_label.pack(pady=10, fill="x")

score_label = ttk.Label(
    root, 
    text="النقاط: 0/{}".format(len(quiz)),
    anchor="center",
    justify="center",
    padding=10
)
score_label.pack(pady=10, fill="x")

next_btn = ttk.Button(
    root,
    text="التالي ➡",
    state="disabled"
)
next_btn.pack(pady=10)

choice_btns = []

current_question = 0
score = 0

def show_question():
    global choice_btns
    question = quiz[current_question]
    qs_label.config(text=question["question"])

    for btn in choice_btns:
        btn.pack_forget()
    choice_btns.clear()

    for i, choice in enumerate(question["choices"]):
        button = ttk.Button(
            root,
            text=choice,
            command=lambda i=i: check_answer(i)
        )
        button.pack(pady=5, fill="x", padx=100)
        choice_btns.append(button)

    feedback_label.config(text="")
    next_btn.config(state="disabled")

def check_answer(choice_index):
    global score
    question = quiz[current_question]
    if question["choices"][choice_index] == question["answer"]:
        feedback_label.config(text="✔ إجابة صحيحة", foreground="#00FF7F")
        score += 1
        score_label.config(text=f"النقاط: {score}/{len(quiz)}")
    else:
        feedback_label.config(text=f"✘ إجابة خاطئة (الصحيح: {question['answer']})", foreground="#FF4500")

    for btn in choice_btns:
        btn.config(state="disabled")

    next_btn.config(state="normal", command=next_question)

def next_question():
    global current_question
    current_question += 1
    if current_question < len(quiz):
        show_question()
    else:
        messagebox.showinfo(
            "الاختبار انتهى",
            f"لقد أنهيت جميع الأسئلة!\n\nنتيجتك النهائية: {score}/{len(quiz)}"
        )
        root.destroy()

show_question()
root.mainloop()
