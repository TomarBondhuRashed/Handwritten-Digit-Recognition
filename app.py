import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageDraw
import numpy as np
import threading
import sys

# Check Python version
if sys.version_info >= (3, 14):
    raise RuntimeError(
        "TensorFlow is not yet compatible with Python 3.14+. "
        "Please use Python 3.10, 3.9, or 3.8 for this application."
    )

try:
    from tensorflow.keras.models import load_model
except ImportError:
    raise ImportError(
        "TensorFlow is not installed or not compatible with your Python version. "
        "Install it with: pip install tensorflow (on Python 3.10 or lower). "
        "Also install pillow: pip install pillow"
    )

# Load the trained Keras model
model = load_model('bestmodel.keras')

class DigitRecognizerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Handwritten Digit Recognizer")
        
        # Canvas size
        self.canvas_size = 280
        self.canvas = tk.Canvas(root, width=self.canvas_size, height=self.canvas_size, bg='white')
        self.canvas.pack()
        
        # PIL image for drawing
        self.image = Image.new("L", (self.canvas_size, self.canvas_size), 255)  # White background
        self.draw = ImageDraw.Draw(self.image)
        
        # Prediction label
        self.prediction_label = tk.Label(root, text="Draw a digit", font=("Arial", 16))
        self.prediction_label.pack()
        
        # Clear button
        self.clear_button = tk.Button(root, text="Clear", command=self.clear_canvas)
        self.clear_button.pack()
        
        # Drawing variables
        self.last_x, self.last_y = None, None
        self.drawing = False
        
        # Bind mouse events
        self.canvas.bind("<Button-1>", self.start_draw)
        self.canvas.bind("<B1-Motion>", self.draw_line)
        self.canvas.bind("<ButtonRelease-1>", self.stop_draw)
        
        # Prediction thread
        self.predict_thread = None
        
    def start_draw(self, event):
        self.drawing = True
        self.last_x, self.last_y = event.x, event.y
        
    def draw_line(self, event):
        if self.drawing:
            x, y = event.x, event.y
            if self.last_x and self.last_y:
                # Draw on canvas
                self.canvas.create_line(self.last_x, self.last_y, x, y, width=20, fill='black', capstyle=tk.ROUND, smooth=tk.TRUE)
                # Draw on PIL image
                self.draw.line([self.last_x, self.last_y, x, y], fill=0, width=20)
            self.last_x, self.last_y = x, y
            # Predict in background
            self.predict_digit_async()
    
    def stop_draw(self, event):
        self.drawing = False
        self.last_x, self.last_y = None, None
    
    def clear_canvas(self):
        self.canvas.delete("all")
        self.image = Image.new("L", (self.canvas_size, self.canvas_size), 255)
        self.draw = ImageDraw.Draw(self.image)
        self.prediction_label.config(text="Draw a digit")
    
    def predict_digit_async(self):
        if self.predict_thread and self.predict_thread.is_alive():
            return  # Skip if already predicting
        self.predict_thread = threading.Thread(target=self.predict_digit)
        self.predict_thread.start()
    
    def predict_digit(self):
        try:
            # Resize to 28x28
            img_resized = self.image.resize((28, 28), Image.LANCZOS)
            img_array = np.array(img_resized).astype('float32') / 255.0
            img_array = 1.0 - img_array  # Invert: white digit on black
            img_array = img_array.reshape(1, 28, 28, 1)
            
            pred = model.predict(img_array, verbose=0)
            digit = np.argmax(pred)
            confidence = float(np.max(pred))
            
            # Update label on main thread
            self.root.after(0, lambda: self.prediction_label.config(text=f"Prediction: {digit} ({confidence:.2f})"))
        except Exception as e:
            self.root.after(0, lambda: self.prediction_label.config(text=f"Error: {str(e)}"))

if __name__ == "__main__":
    root = tk.Tk()
    app = DigitRecognizerApp(root)
    root.mainloop()
