
from svglib.svglib import svg2rlg
from reportlab.graphics import renderPDF, renderPM

def svg2png(input_file, output_file):
    """Convert SVG to PNG
    
    Convert SVG file to PNG file.
    
    Args:
        - input_file (string): input svg file path
        - output_file (string): output png file path
    
    Returns:
        - None
    """
    
    drawing = svg2rlg(input_file)
    renderPM.drawToFile(drawing, output_file, fmt='PNG', dpi=128)

