from tkinter import *
import tkinter as tk
from tkinter import filedialog
import pytesseract
from PIL import Image, ImageTk

root = tk.Tk()
root.geometry("400x500")

root.title("Image Text Reader")



def open_file():
    # use filedialog to open the file
    file_path = filedialog.askopenfilename()
    # open the image using PIL Image
    image = Image.open(file_path)
    # create a Tkinter PhotoImage object from the PIL image
    photo = ImageTk.PhotoImage(image)
    # display the image in a label
    label_image.config(image=photo)
    label_image.image = photo
    pytesseract.pytesseract.tesseract_cmd=r'C:\Program Files\Tesseract-OCR\tesseract.exe'
    # read text from the image using pytesseract OCR
    text = pytesseract.image_to_string(image)
    # display the text in a text box
    text_box.delete('1.0', tk.END)
    text_box.insert(tk.END, text)

# create a label to display the image
label_image = tk.Label(root)
label_image.pack()

# create a button to open the image file


# create a text box to display the text from the image

text_box = tk.Text(root)
text_box.pack()
button_open = tk.Button(root, text="Open Image", command=open_file)
button_open.pack()
# run the main loop
root.mainloop()
root.mainloop()