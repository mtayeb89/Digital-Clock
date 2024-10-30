import tkinter as tk
from time import strftime


class DigitalClock:
    def __init__(self):
        # Create the main window
        self.window = tk.Tk()
        self.window.title("Digital Clock")

        # Configure window size and position
        self.window.geometry("400x200")
        self.window.configure(bg='black')

        # Create label for the clock
        self.label = tk.Label(
            self.window,
            font=('Arial', 50, 'bold'),
            background='black',
            foreground='cyan'
        )

        # Center the label
        self.label.pack(anchor='center', pady=20)

        # Create date label
        self.date_label = tk.Label(
            self.window,
            font=('Arial', 20),
            background='black',
            foreground='cyan'
        )
        self.date_label.pack(anchor='center')

        # Initialize the clock update
        self.update_clock()

    def update_clock(self):
        """Update the clock every second"""
        # Get current time
        time_string = strftime("%H:%M:%S")
        date_string = strftime("%B %d, %Y")

        # Update labels
        self.label.config(text=time_string)
        self.date_label.config(text=date_string)

        # Schedule the next update
        self.window.after(1000, self.update_clock)

    def run(self):
        """Start the clock application"""
        self.window.mainloop()


# Create and run the clock
if __name__ == "__main__":
    clock = DigitalClock()
    clock.run()