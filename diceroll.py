import random
import tkinter as tk
from PIL import Image, ImageTk

# create a dictionary to map dice results to image file names
dice_images = {
    1: "dice-1.png",
    2: "dice-2.png",
    3: "dice-3.png",
    4: "dice-4.png",
    5: "dice-5.png",
    6: "dice-6.png",
}

# create a function to roll the dice and display the result


def roll_dice():
    global dice_photo  # declare a global variable to hold the photo object
    result = random.randint(1, 6)
    result_label.config(text=f"You rolled a {result}")
    image_path = dice_images[result]
    image = Image.open(image_path)
    image = image.resize((100, 100))  # resize the image to 100x100 pixels
    dice_photo = ImageTk.PhotoImage(image)
    dice_label.config(image=dice_photo)


# create the main window and set its properties
root = tk.Tk()
root.title("Dice Rolling Simulator")
root.geometry("400x400")

# create a label to display the result of the dice roll
result_label = tk.Label(root, text="", font=("Arial", 20))
result_label.pack(pady=10)

# create a label to display the dice image
dice_photo = None  # initialize the photo variable
dice_label = tk.Label(root, image=dice_photo)
dice_label.pack(pady=20)

# create a button to roll the dice
roll_button = tk.Button(root, text="Roll the Dice",
                        font=("Arial", 16), command=roll_dice)
roll_button.pack(pady=10)

# create a button to quit the program
quit_button = tk.Button(root, text="Quit", font=(
    "Arial", 16), command=root.quit)
quit_button.pack()

# run the main loop of the program
root.mainloop()
