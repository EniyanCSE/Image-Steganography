import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk

def upload_image():
    global file_path
    file_path = filedialog.askopenfilename()
    if file_path:
        image = Image.open(file_path)
        image.thumbnail((300, 300))  # Resize image to fit in the GUI
        photo = ImageTk.PhotoImage(image)
        canvas.create_image(0, 0, anchor=tk.NW, image=photo)
        canvas.image = photo

def steganography():
    text_to_hide = text_field.get("1.0", "end-1c")
    if file_path:
        destination_path = filedialog.asksaveasfilename(defaultextension='.png')
        if destination_path:
            if hide_text_in_image(file_path, text_to_hide, destination_path):
                status_label.config(text="Steganography completed. Image saved as {}".format(destination_path))
            else:
                status_label.config(text="Steganography failed.")
        else:
            status_label.config(text="Steganography canceled.")
    else:
        status_label.config(text="Please upload an image first.")

def hide_text_in_image(image_path, text_to_hide, destination_path):
    try:
        image = Image.open(image_path)
        binary_text = ''.join(format(ord(char), '08b') for char in text_to_hide)
        binary_text += '1111111111111110'  # Adding null terminator
        data_index = 0
        pixels = list(image.getdata())
        for i in range(len(pixels)):
            pixel = list(pixels[i])
            for j in range(3):  # Loop through RGB channels
                if data_index < len(binary_text):
                    pixel[j] &= 0b11111110  # Clear the least significant bit
                    pixel[j] |= int(binary_text[data_index])
                    data_index += 1
            pixels[i] = tuple(pixel)
            if data_index >= len(binary_text):
                break
        image.putdata(pixels)
        image.save(destination_path)
        return True
    except Exception as e:
        print("Error:", e)
        return False


# Create main window
root = tk.Tk()
root.title("Image Steganography")

# Create GUI elements
upload_button = tk.Button(root, text="Upload Image", command=upload_image)
upload_button.pack(pady=10)

canvas = tk.Canvas(root, width=300, height=300)
canvas.pack()

text_field = tk.Text(root, height=4, width=50)
text_field.pack(pady=10)

steganography_button = tk.Button(root, text="Perform Steganography", command=steganography)
steganography_button.pack(pady=5)

status_label = tk.Label(root, text="")
status_label.pack()

root.mainloop()
