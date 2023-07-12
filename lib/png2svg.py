
import aspose.words as aw
from PIL import Image

def png2svg(input_file, output_file):
    """Convert PNG to SVG
    
    Convert PNG file to SVG file.
    
    Args:
        - input_file (string): input png file path
        - output_file (string): output svg file path
    
    Returns:
        - None
    """
    
    doc = aw.Document()
    builder = aw.DocumentBuilder(doc)
    shape = builder.insert_image(input_file)
    save_opt = aw.saving.ImageSaveOptions(aw.SaveFormat.SVG)
    shape.get_shape_renderer().save(output_file, save_opt)


