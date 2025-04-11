import tkinter as tk
from tkinter import ttk

class ScrollableFrame(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent)

        # Create a canvas
        self.canvas = tk.Canvas(self)
        self.scrollbar = ttk.Scrollbar(self, orient="vertical", command=self.canvas.yview)
        self.scrollable_frame = ttk.Frame(self.canvas)

        # Configure the canvas
        self.scrollable_frame.bind(
            "<Configure>",
            lambda e: self.canvas.configure(scrollregion=self.canvas.bbox("all"))
        )

        # Create window in canvas
        self.canvas.create_window((0, 0), window=self.scrollable_frame, anchor="nw")

        # Pack the canvas and scrollbar
        self.canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        self.scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        # Bind the scrollbar to the canvas
        self.canvas.configure(yscrollcommand=self.scrollbar.set)

# Usage example
root = tk.Tk()
root.geometry("300x200")

scrollable_frame = ScrollableFrame(root)
scrollable_frame.pack(fill=tk.BOTH, expand=True)

# Add content to the scrollable frame
for i in range(50):
    ttk.Label(scrollable_frame.scrollable_frame, text=f"Label {i+1}").pack()

root.mainloop()