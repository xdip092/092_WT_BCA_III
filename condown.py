import tkinter as tk
from time import strftime

class FlipClock:
    def __init__(self, root):
        self.root = root
        self.root.title("Flip Clock")
        self.root.geometry("300x150")
        self.root.configure(bg="black")

        self.time_label = tk.Label(
            self.root, font=("Courier", 48), bg="black", fg="white"
        )
        self.time_label.pack(expand=True)

        self.update_time()

    def update_time(self):
        current_time = strftime("%H:%M:%S")
        self.time_label.config(text=current_time)
        self.root.after(1000, self.update_time)

if __name__ == "__main__":
    root = tk.Tk()
    clock = FlipClock(root)
    root.mainloop()