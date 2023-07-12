
from PIL import Image

def png2ico(input_file, output_file):
    """Convert PNG to ICO
    
    Convert PNG file to ICO file.
    
    Args:
        - input_file (string): input png file path
        - output_file (string): output ico file path
    
    Returns:
        - None
    """
    
    image = Image.open(input_file)
    image.save(output_file)

