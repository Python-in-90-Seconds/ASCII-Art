from PIL import Image  # Importing the Python Imaging Library for image processing

# Characters used to represent different levels of brightness in the ASCII art
ASCII_CHARS = "@%#*+=-:. "  # From darkest to lightest

def resize_image(image, new_width=100):
    """
    Resizes the image while maintaining the aspect ratio.
    The height is scaled down further (by 1.65) to account for terminal character height differences.
    """
    width, height = image.size
    ratio = height / width / 1.65  # Adjusting for aspect ratio of characters
    new_height = int(new_width * ratio)
    return image.resize((new_width, new_height))  # Resized image returned

def grayify(image):
    """
    Converts the image to grayscale (L mode).
    This simplifies pixel values from RGB to single brightness levels.
    """
    return image.convert("L")  # L = 8-bit pixels, black and white

def pixels_to_ascii(image):
    """
    Maps grayscale pixel values to ASCII characters.
    """
    pixels = image.getdata()  # Get a flat list of all pixels
    ascii_str = ""
    for pixel in pixels:
        ascii_str += ASCII_CHARS[pixel // 25]  # Divide 0-255 range into 10 buckets
    return ascii_str

def main(image_path):
    """
    Orchestrates the image-to-ASCII conversion process:
    1. Open the image
    2. Resize it
    3. Convert to grayscale
    4. Convert pixels to ASCII characters
    5. Print the resulting ASCII art
    """
    image = Image.open(image_path)
    image = resize_image(image)
    image = grayify(image)
    ascii_str = pixels_to_ascii(image)

    img_width = image.width
    # Split the flat ASCII string into lines based on the image width
    ascii_img = "\n".join([ascii_str[i:(i+img_width)] for i in range(0, len(ascii_str), img_width)])
    
    print(ascii_img)  # Display the ASCII art

# Run the program on the specified image
main("imag.jpg")
