import tkinter as tk
from components.draggable_widget import DraggableWidget
from components.model import NeuralNetwork

def main():
    root = tk.Tk()
    root.geometry("960x640")
    root.title("DragNN")

    layers_frame = tk.Frame(root, width=200, height=600, bg="#303030")
    layers_frame.pack(side="left", fill="y")

    build_frame = tk.Frame(root, width=400, height=600, bg="#191919")
    build_frame.pack(side="right", fill="both", expand=True)

    layers = [
            "Dense Layer",
            "Conv2D Layer",
            "Conv3D Layer",
            "Transposed Conv2D Layer",
            "Transposed Conv3D Layer",
            "Activation Layer",
            "MaxPool2D Layer",
            "AvgPool2D Layer",
            "MaxPool3D Layer",
            "AvgPool3D Layer",
            "Flatten Layer",
            "Dropout Layer",
            "Dropout2D Layer",
            "Dropout3D Layer",
            "BatchNorm2D Layer",
            "BatchNorm3D Layer"
        ]
    
    for layer in layers:
        label = tk.Label(layers_frame, text=layer, bg="#dbdbdb", width=10, height=2)
        DraggableWidget(layers_frame, label, 50, 50)
        label.pack(fill='x',pady=5)

        #button = tk.Button(layers_frame, text=layer,height=3 ,foreground='#dbdbdb',bg='#3f3f3f')
        #button.pack(fill="x", pady=5)
        
    root.mainloop()



if __name__ == "__main__":
    main()