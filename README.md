# ✍️ Handwritten Digit Recognition (CNN + GUI)

### 🚀 Day 13 of 30: Machine Learning Projects Challenge

**Goal:** Build a Computer Vision system that can read human handwriting (Digits 0-9) and create an app to test it in real-time.
**The Dataset:** The famous **MNIST** dataset (60,000 training images of handwritten digits).

---

## 🧠 The Model: Convolutional Neural Network (CNN)
Unlike standard Machine Learning (SVM/Random Forest), I used **Deep Learning** to achieve higher accuracy (~99%).
* **Input:** 28x28 Grayscale images.
* **Architecture:**
    * 2x Convolutional Layers (Conv2D) to detect edges and curves.
    * Max Pooling to reduce dimensionality.
    * Dropout layers to prevent overfitting.
    * Dense (Fully Connected) output layer for the 10 digits.
* **Framework:** TensorFlow/Keras.

---

## 🎨 The Application (GUI)
I built a desktop application using **Tkinter** that allows users to draw digits on a canvas.
* **Real-time Preprocessing:** The app automatically captures the drawing, resizes it to 28x28, converts it to grayscale, and inverts the colors (White on Black) to match the MNIST format before feeding it to the AI.

---

## 🛠️ Tech Stack
* **Python**
* **TensorFlow / Keras** (Deep Learning)
* **Tkinter** (GUI App)
* **NumPy** (Data Processing)
* **Matplotlib** (Visualization)

---

## ⚙️ How to Run
1.  **Clone the repository:**
    ```bash
    git clone [https://github.com/TomarBondhuRashed/digit-recognition.git](https://github.com/TomarBondhuRashed/digit-recognition.git)
    ```
2.  **Install dependencies:**
    ```bash
    pip install tensorflow numpy matplotlib pillow
    ```
3.  **Run the GUI App:**
    ```bash
    python app.py
    ```
    *(Draw a number on the popup window to see the prediction!)*

---

## 🤝 Connect
Follow my 30-day coding journey!
* **LinkedIn:** [Your Profile Link]
* **GitHub:** [TomarBondhuRashed](https://github.com/TomarBondhuRashed)
