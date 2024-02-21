import tkinter as tk
from tkinter import filedialog
from PIL import Image

def upload_image():
    global file_path
    file_path = filedialog.askopenfilename()
    if file_path:
        hidden_text = extract_hidden_text(file_path)
        if hidden_text:
            text_field.delete("1.0", tk.END)  # Clear previous text
            text_field.insert(tk.END, hidden_text)
            status_label.config(text="Hidden text extracted successfully.")
        else:
            status_label.config(text="No hidden text found in the image.")
    else:
        status_label.config(text="No image selected.")

def extract_hidden_text(image_path):
    try:
        image = Image.open(image_path)
        binary_text = ''
        for pixel in image.getdata():
            for channel in pixel:
                binary_text += str(channel & 1)  # Extract the least significant bit
                if binary_text.endswith('1111111111111110'):  # Null terminator indicating end of message
                    break
            else:
                continue
            break
        hidden_text = ''.join(chr(int(binary_text[i:i+8], 2)) for i in range(0, len(binary_text), 8))
        return hidden_text.rstrip('\x00')  # Remove null terminator and trailing null characters
    except Exception as e:
        print("Error:", e)
        return None

# Create main window
root = tk.Tk()
root.title("Extract Hidden Text from Image")

# Create GUI elements
upload_button = tk.Button(root, text="Upload Image", command=upload_image)
upload_button.pack(pady=10)

text_field = tk.Text(root, height=10, width=50)
text_field.pack(pady=10)

status_label = tk.Label(root, text="")
status_label.pack()

root.mainloop()
