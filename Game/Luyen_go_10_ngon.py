import random
import string
import tkinter as tk
from PIL import Image, ImageTk

# Function to choose a random word
def choose_word():
    return ''.join(random.choices(string.ascii_letters, k=5))

# Function to check the entered word and update score
def check_word(event=None):
    global score, time_left, timer
    
    if time_left > 0:
        entered_word = entry.get()
        current_word = display_label.cget("text")
        
        if entered_word == current_word:
            display_label.config(text=choose_word())
            result_label.config(text="Correct", fg="green")
            score += 1
            
            # Reset the timer when a correct word is entered
            time_left = 10  # Reset the time limit to 10 seconds
            update_time()   # Restart the countdown timer
            
        else:
            if entered_word == "":
                result_label.config(text="Please enter a word", fg="red")
            else:
                result_label.config(text="Incorrect, try again", fg="red")

        entry.delete(0, tk.END)
        score_label.config(text=f"Score: {score}")
    else:
        result_label.config(text="Time's up!", fg="blue")
        check_button.config(text="Play Again", state=tk.NORMAL, command=reset_game)

def reset_game():
    global score, time_left
    score = 0
    time_left = 10
    score_label.config(text=f"Score: {score}")
    display_label.config(text=choose_word())
    result_label.config(text="")
    check_button.config(text="Check", state=tk.NORMAL)
    update_time()  # Restart the countdown timer

def update_time():
    global time_left, timer
    time_left -= 1
    time_label.config(text=f"Time Left: {time_left} seconds")

    if time_left == 0:
        root.after_cancel(timer)
    else:
        timer = root.after(1000, update_time)

root = tk.Tk()
root.title("Word Entry Simulation")

score = 0
time_left = 10

# Load the image
background_image = Image.open("path/to/your/image.jpg")  # Replace with your image file path
window_width, window_height = 800, 500
background_image = background_image.resize((window_width, window_height))
background_photo = ImageTk.PhotoImage(background_image)

# Create a Canvas to place the background image
canvas = tk.Canvas(root, width=window_width, height=window_height)
canvas.place(x=0, y=0, relwidth=1, relheight=1)

# Place the background image on the Canvas at the bottom
canvas.create_image(0, 0, anchor=tk.NW, image=background_photo)

# Other widgets
display_label = tk.Label(root, text=choose_word(), font=("Open Sans", 40), justify='center')
display_label.pack(padx=20, pady=(80, 20), anchor='center')

entry = tk.Entry(root, width=30, font=("Open Sans", 20))
entry.pack(padx=20, pady=10, anchor='center')
entry.bind("<Return>", check_word) 

check_button = tk.Button(root, text="check", command=check_word, font=("Open Sans", 30))
check_button.pack(padx=20, pady=10, anchor='center')

result_label = tk.Label(root, text="", font=("Open Sans", 25))
result_label.pack(padx=20, pady=10, anchor='center')

score_label = tk.Label(root, text=f"Score: {score}", font=("Open Sans", 20))
score_label.pack(padx=20, pady=10, anchor='center')

time_label = tk.Label(root, text=f"Time Left: {time_left} seconds", font=("Open Sans", 20))
time_label.pack(padx=20, pady=10, anchor='center')

# Begin the countdown
update_time()

root.geometry("800x500")
root.mainloop()
