import tkinter as tk
from PIL import Image, ImageTk
import random

class MovingSquareGame:
    def __init__(self, master):
        self.master = master
        self.master.title("Moving Square Game")
        self.master.geometry("1000x800")  # Adjusted window size for better visibility

        self.square_size_mouse = 300  #size mouse
        self.square_size_hammer = 100 #size hammer 
        self.square = None
        self.score = 0  # Initialize score

        # Load the mouse image
        mouse_image = Image.open("E:\Language\Python\Game\Mouse_smash_game\Chuot.jpg")  # Update the path to your mouse image
        mouse_image = mouse_image.resize((self.square_size_mouse, self.square_size_mouse))
        self.mouse_photo = ImageTk.PhotoImage(mouse_image)

        # Load the hammer image
        hammer_image = Image.open("E:\Language\Python\Game\Mouse_smash_game\Bua.jpg")  # Update the path to your hammer image
        hammer_image = hammer_image.resize((self.square_size_hammer, self.square_size_hammer))
        self.hammer_photo = ImageTk.PhotoImage(hammer_image)

        self.create_square()
        self.create_score_label()  # Create the score label

    def create_square(self):
        x = random.randint(0, 700)
        y = random.randint(0, 500)

        self.square = tk.Canvas(self.master, width=self.square_size_mouse, height=self.square_size_mouse, bg="white")
        self.square.place(x=x, y=y)

        # Create mouse image on the canvas
        self.square_image = self.square.create_image(0, 0, anchor=tk.NW, image=self.mouse_photo)

        # Bind the click event to the square
        self.square.bind("<Button-1>", self.on_square_click)

    def create_score_label(self):
        # Create a label to display the score
        self.score_label = tk.Label(self.master, text="Score: 0", font=("Arial", 18))
        self.score_label.place(x=20, y=20)  # Adjust the position as needed

    def update_score_label(self):
        # Update the score label text
        self.score_label.config(text=f"Score: {self.score}")

    def on_square_click(self, event):
        # Update score
        self.score += 1
        self.update_score_label()  # Update the displayed score

        # Destroy the current square
        self.square.destroy()

        # Create a new square at a random position
        self.create_square()

        # Animate hammer image at the click position
        self.animate_hammer(event.x_root, event.y_root)

    def animate_hammer(self, x, y):
        # Display hammer image at the click position
        hammer_label = tk.Label(self.master, image=self.hammer_photo)
        hammer_label.place(x=x - self.square_size_hammer // 2, y=y - self.square_size_hammer // 2)

        # Animate the hammer
        for i in range(30, -1, -1):
            hammer_label.place(x=x - self.square_size_hammer // 2, y=y - self.square_size_hammer // 2)
            self.master.update()
            self.master.after(1)

        # Remove the hammer image
        hammer_label.destroy()

if __name__ == "__main__":
    root = tk.Tk()
    game = MovingSquareGame(root)
    root.mainloop()
