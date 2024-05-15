import tkinter as tk
from tkinter import filedialog
import pytesseract
from PIL import Image

# Create a tkinter window
window = tk.Tk()
window.title("Extract Text from Image")

# Define a function to extract text from an image file
def extract_text():
    # Ask the user to select an image file
    filepath = filedialog.askopenfilename(filetypes=[("Image Files", "*.jpg;*.jpeg;*.png;*.bmp")])
    if not filepath:
        return  # User cancelled the dialog

    # Open the image file
    image = Image.open(filepath)

    # Extract text from the image
    text = pytesseract.image_to_string(image)

    # Display the extracted text in a text box
    text_box.delete("1.0", "end")
    text_box.insert("1.0", text)

# Create a button to trigger text extraction
extract_button = tk.Button(window, text="Extract Text", command=extract_text)
extract_button.pack(pady=10)

# Create a text box to display the extracted text
text_box = tk.Text(window, height=10, width=50)
text_box.pack()

# Start the tkinter event loop
window.mainloop()
