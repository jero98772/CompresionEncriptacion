from PIL import Image

def read_image_file(image_path):
    """Reads an image file and returns its size and raw binary data."""
    try:
        with Image.open(image_path) as img:
            img.show()  # Display the image
            img_data = img.tobytes()  # Get raw binary image data
            return img.size, img_data
    except FileNotFoundError:
        print(f"The image file at {image_path} was not found.")
        return None, None
        
def readtxtstr(name):
	"""
	readtxtstr(name) , return txt content as string
	"""
	content = ""
	with open(name, 'r') as file:
		for i in file.readlines():
			content += str(i).replace("\n","")
	return content

def read_binary_file(file_path):
    """Reads a binary file and returns the binary data."""
    try:
        with open(file_path, 'rb') as file:
            binary_data = file.read()
        return binary_data
    except FileNotFoundError:
        print(f"The file at {file_path} was not found.")
        return None