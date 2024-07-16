import tkinter as tk

class DraggableWidget:
    def __init__(self, master, widget, x, y):
        self.master = master
        self.widget = widget
        self.widget.place(x=x, y=y)
        
        self.widget.bind("<Button-1>", self.on_click)
        self.widget.bind("<B1-Motion>", self.on_drag)
        self.widget.bind("<ButtonRelease-1>", self.on_release)
        
        self.drag_data = {"x": 0, "y": 0}
    
    def on_click(self, event):
        self.drag_data["x"] = event.x
        self.drag_data["y"] = event.y
    
    def on_drag(self, event):
        dx = event.x - self.drag_data["x"]
        dy = event.y - self.drag_data["y"]
        
        x = self.widget.winfo_x() + dx
        y = self.widget.winfo_y() + dy
        
        self.widget.place(x=x, y=y)
    
    def on_release(self, event):
        self.drag_data["x"] = 0
        self.drag_data["y"] = 0
