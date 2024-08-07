import tkinter as tk
from tkinter import messagebox

class Dialog:
    def show_info(msg: str):
        messagebox.showinfo("Information", msg)

    def show_warning(msg: str):
        messagebox.showwarning("Warning", msg)

    def show_error(msg: str):
        messagebox.showerror("Error", msg)

    def ask_question(msg: str) -> str:
        response = messagebox.askquestion("Question", msg)
        return response

    def ask_ok_cancel(msg: str) -> bool:
        response = messagebox.askokcancel("Confirmation",msg)
        return response

    def ask_yes_no(msg: str) -> bool:
        response = messagebox.askyesno("Choose", msg)
        return response 

    def ask_retry_cancel(msg: str) -> bool:
        response = messagebox.askretrycancel("Retry", msg)
        return response