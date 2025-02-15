import tkinter as tk
import random

def check_guess():
    try:
        guess = int(entry.get())
        if guess < number:
            result_label.config(text="Too low! Try again.", fg="red")
        elif guess > number:
            result_label.config(text="Too high! Try again.", fg="red")
        else:
            result_label.config(text=f"Correct! You guessed it in {attempts[0]} attempts.", fg="green")
            guess_button.config(state=tk.DISABLED)
    except ValueError:
        result_label.config(text="Please enter a valid number!", fg="red")
    
    attempts[0] += 1
    entry.delete(0, tk.END)

def reset_game():
    global number
    number = random.randint(1, 100)
    attempts[0] = 1
    result_label.config(text="Guess a number between 1 and 100", fg="black")
    guess_button.config(state=tk.NORMAL)
    entry.delete(0, tk.END)

# Initialize main window
root = tk.Tk()
root.title("Number Guessing Game")
root.geometry("300x200")

number = random.randint(1, 100)
attempts = [1]

# Widgets
label = tk.Label(root, text="Guess a number between 1 and 100")
label.pack(pady=10)

entry = tk.Entry(root)
entry.pack()

guess_button = tk.Button(root, text="Guess", command=check_guess)
guess_button.pack(pady=5)

result_label = tk.Label(root, text="")
result_label.pack()

reset_button = tk.Button(root, text="Reset Game", command=reset_game)
reset_button.pack(pady=5)

# Run the application
root.mainloop()
