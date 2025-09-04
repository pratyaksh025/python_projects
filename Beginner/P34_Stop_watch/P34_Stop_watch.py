import tkinter as tk
import time

class Stopwatch:
    def __init__(self, root):
        self.root = root
        self.root.title("Stopwatch ⏱️")

        self.running = False
        self.paused = False
        self.start_time = 0
        self.elapsed_time = 0

        # Label to show time
        self.label = tk.Label(root, text="0.00", font=("Arial", 40))
        self.label.pack(pady=30)

        # Buttons
        self.start_btn = tk.Button(root, text="Start", width=10, command=self.start)
        self.start_btn.pack(side="left", padx=5)

        self.pause_btn = tk.Button(root, text="Pause", width=10, command=self.pause)
        self.pause_btn.pack(side="left", padx=5)

        self.resume_btn = tk.Button(root, text="Resume", width=10, command=self.resume)
        self.resume_btn.pack(side="left", padx=5)

        self.reset_btn = tk.Button(root, text="Reset", width=10, command=self.reset)
        self.reset_btn.pack(side="left", padx=5)

        self.update_clock()

    def update_clock(self):
        if self.running and not self.paused:
            current_time = self.elapsed_time + (time.time() - self.start_time)
            self.label.config(text=f"{current_time:.2f}")
        self.root.after(10, self.update_clock)  # update every 0.1s

    def start(self):
        if not self.running:
            self.start_time = time.time()
            self.running = True
            self.paused = False

    def pause(self):
        if self.running and not self.paused:
            self.elapsed_time += time.time() - self.start_time
            self.paused = True

    def resume(self):
        if self.running and self.paused:
            self.start_time = time.time()
            self.paused = False

    def reset(self):
        self.running = False
        self.paused = False
        self.start_time = 0
        self.elapsed_time = 0
        self.label.config(text="0.00")

root = tk.Tk()
app = Stopwatch(root)
root.mainloop()
