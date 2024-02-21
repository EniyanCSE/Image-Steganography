# Image Steganography Tool

This tool provides functionality to hide and extract text messages within digital images using steganographic techniques. It consists of two Python scripts: `encrypt.py` for hiding text in images and `decrypt.py` for extracting hidden text from images.

## Encrypt (encrypt.py)

This script allows users to hide text messages within digital images. Users can upload an image, input a text message, and perform encryption to embed the text covertly within the image. The encrypted image can then be saved to a specified location.

## Decrypt (decrypt.py)

This script enables users to extract hidden text messages from steganographed images. Users can upload a steganographed image, and the script will extract any hidden text messages and display them for the user to read.

## How to Use

1. **Encrypting Text into Image (encrypt.py):**
   - Run the `encrypt.py` script.
   - Upload an image using the "Upload Image" button.
   - Enter the text message you wish to hide.
   - Click on "Perform Steganography" to embed the text into the image.
   - Save the steganographed image to a desired location.

2. **Extracting Hidden Text from Image (decrypt.py):**
   - Run the `decrypt.py` script.
   - Upload a steganographed image using the "Upload Image" button.
   - The hidden text message will be extracted and displayed in the text field.

## Requirements

- Python 3.x
- tkinter (for GUI)
- Pillow (Python Imaging Library)
