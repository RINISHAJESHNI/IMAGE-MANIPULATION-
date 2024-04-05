import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk, ImageFilter
import numpy as np

class ImageManipulationApp:
    def __init__(self, master):
        self.master = master
        master.title("Image Manipulation App")

        # Create widgets
        self.label1 = tk.Label(master, text="Choose an operation:")
        self.label1.pack()

        self.operations = ["Grayscale", "Blur", "Sharpen", "Thresholding", "Color Space Conversion"]
        self.operation_var = tk.StringVar()
        self.operation_var.set(self.operations[0])
        self.operation_menu = tk.OptionMenu(master, self.operation_var, *self.operations)
        self.operation_menu.pack()

        self.upload_button = tk.Button(master, text="Upload Image", command=self.upload_image)
        self.upload_button.pack()

        self.apply_button = tk.Button(master, text="Apply", command=self.apply_operation)
        self.apply_button.pack()

        self.canvas = tk.Canvas(master, width=400, height=400)
        self.canvas.pack()

        # Initialize variables
        self.image = None
        self.image_tk = None
        self.result_image = None
        self.result_image_tk = None

    def upload_image(self):
        file_path = filedialog.askopenfilename()
        self.image = Image.open(file_path)
        self.image_tk = ImageTk.PhotoImage(self.image)
        self.canvas.create_image(0, 0, anchor="nw", image=self.image_tk)

    def apply_operation(self):
        if self.image is None:
            return

        operation = self.operation_var.get()
        if operation == "Grayscale":
            self.result_image = self.image.convert("L")
        elif operation == "Blur":
            self.result_image = self.image.filter(ImageFilter.GaussianBlur(radius=5))
        elif operation == "Sharpen":
            self.result_image = self.image.filter(ImageFilter.SHARPEN)
        elif operation == "Thresholding":
            # Convert image to grayscale
            gray_img = self.image.convert("L")
            # Thresholding
            threshold = 128
            self.result_image = gray_img.point(lambda p: 255 if p > threshold else 0, '1')
        elif operation == "Color Space Conversion":
            self.result_image = self.image.convert("HSV")  # Example: Convert to HSV color space

        self.result_image_tk = ImageTk.PhotoImage(self.result_image)
        self.canvas.create_image(0, 0, anchor="nw", image=self.result_image_tk)


root = tk.Tk()
app = ImageManipulationApp(root)
root.mainloop()
