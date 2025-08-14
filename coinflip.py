import tkinter as tk
import random
import time

def flip_coin():
    start_time = time.time()
    def update():
        nonlocal start_time
        rand_int = random.randint(1, 20)
        if rand_int % 2 == 0:
            result = "Heads"
        else:
            result = "Tails"

        label.config(text=f"Flipping... {result}")

        if time.time() - start_time < 2:  # keep flipping for 2 sec
            root.after(100, update)  # schedule next flip
        else:
            label.config(text=f"🎯 Final result: {result}")

    update()

# Tkinter setup
root = tk.Tk()
root.title("Coin Flip Game")
root.geometry("300x150")

label = tk.Label(root, text="Click 'Flip' to start", font=("Arial", 14))
label.pack(pady=20)

flip_button = tk.Button(root, text="Flip Coin", font=("Arial", 12), command=flip_coin)
flip_button.pack()

root.mainloop()
