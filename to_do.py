import tkinter as tk
from tkinter import messagebox
import random
import webbrowser
import os


def add_task():
    task = task_entry.get()
    if task:
        task_listbox.insert(tk.END, task)
        task_entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Warning", "Task cannot be empty!")


def delete_task():
    try:
        selected_task = task_listbox.curselection()[0]
        task_listbox.delete(selected_task)
    except IndexError:
        messagebox.showwarning("Warning", "Please select a task to delete!")


def save_tasks():
    tasks = task_listbox.get(0, tk.END)
    try:
        with open("tasks.txt", "w", encoding="utf-8") as file:
            for task in tasks:
                file.write(task + "\n")
        messagebox.showinfo("Success", "Tasks saved successfully!")
    except Exception as e:
        messagebox.showerror("Error", f"Could not save tasks: {str(e)}")


def load_tasks():
    try:
        with open("tasks.txt", "r", encoding="utf-8") as file:
            for task in file.readlines():
                task_listbox.insert(tk.END, task.strip())
    except FileNotFoundError:
        pass


def motivate_user():
    messages = [
        "You're doing great! Keep going!",
        "Stay focused and finish strong!",
        "Every small step leads to success!",
        "Take a deep breath and keep moving forward!",
        "Hard work pays off. Stay dedicated!"
    ]
    messagebox.showinfo("Motivation", random.choice(messages))


def play_tamil_music():
    music_urls = [
        # Replace with actual Tamil song links (audio-only)
        "https://www.youtube.com/watch?v=music_audio_1",
        "https://www.youtube.com/watch?v=music_audio_2",
        "https://www.youtube.com/watch?v=music_audio_3"
    ]
    webbrowser.open(random.choice(music_urls))


def block_distracting_sites():
    blocklist = ["www.facebook.com", "www.instagram.com",
                 "www.netflix.com", "www.tiktok.com"]
    host_path = r"C:\Windows\System32\drivers\etc\hosts"  # Windows Hosts File Path
    redirect = "127.0.0.1"
    try:
        with open(host_path, "a") as file:
            for site in blocklist:
                file.write(f"{redirect} {site}\n")
        messagebox.showinfo(
            "Focus Mode", "Distracting sites blocked successfully!")
    except Exception as e:
        messagebox.showerror("Error", f"Could not block sites: {str(e)}")


def complete_task():
    try:
        selected_task = task_listbox.curselection()[0]
        task_listbox.delete(selected_task)
        messagebox.showinfo(
            "Task Completed", "Great job! Task completed successfully!")
    except IndexError:
        messagebox.showwarning("Warning", "Please select a task to complete!")


# GUI Setup
root = tk.Tk()
root.title("Productive Task Manager")
root.geometry("400x600")
root.config(bg="#f0f0f0")

# Title Label
title_label = tk.Label(root, text="Productive Task Manager",
                       font=("Arial", 18, "bold"), bg="#f0f0f0")
title_label.pack(pady=10)

# Task Entry
task_entry = tk.Entry(root, width=40)
task_entry.pack(pady=10)

# Buttons
add_button = tk.Button(root, text="Add Task",
                       command=add_task, bg="#4CAF50", fg="white")
add_button.pack(pady=5)

delete_button = tk.Button(root, text="Delete Task",
                          command=delete_task, bg="#FF5733", fg="white")
delete_button.pack(pady=5)

complete_button = tk.Button(
    root, text="Complete Task", command=complete_task, bg="#32CD32", fg="white")
complete_button.pack(pady=5)

save_button = tk.Button(root, text="Save Tasks",
                        command=save_tasks, bg="#008CBA", fg="white")
save_button.pack(pady=5)

motivate_button = tk.Button(
    root, text="Motivate Me!", command=motivate_user, bg="#FFD700", fg="black")
motivate_button.pack(pady=5)

music_button = tk.Button(root, text="Tamil Focus Music",
                         command=play_tamil_music, bg="#800080", fg="white")
music_button.pack(pady=5)

block_button = tk.Button(root, text="Start Work Mode",
                         command=block_distracting_sites, bg="#DC143C", fg="white")
block_button.pack(pady=5)

# Task Listbox
task_listbox = tk.Listbox(root, width=50, height=15)
task_listbox.pack(pady=10)

# Load Tasks on Startup
load_tasks()

root.mainloop()
