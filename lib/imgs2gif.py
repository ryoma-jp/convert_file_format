
from pathlib import Path
from PIL import Image
import cv2

def imgs2gif(input_dir, output_file):
    """Convert Images to GIF
    
    Convert Image files to GIF file.
    
    Args:
        - input_dir (string): input image directory path
        - output_file (string): output gif file path
    
    Returns:
        - None
    """
    
    # --- Load Image File List ---
    with open(Path(input_dir, 'image_list.txt')) as f:
        image_list = f.read().splitlines()

    print(image_list)

    frame_data = []
    for image in image_list:
        frame = Image.open(Path(input_dir, image))
        frame_data.append(frame)

    # --- Frames to GIF ---
    duration = int(1000.0 / 15.0)
    frame_data[0].save(output_file, save_all=True, append_images=frame_data[1:], duration=duration, loop=0)

#    cap = cv2.VideoCapture(input_file)
#    if (not cap.isOpened()):
#        return None, None
#    
#    frame_data = []
#    frame_rate = cap.get(cv2.CAP_PROP_FPS)
#    
#    while (True):
#        ret, frame = cap.read()
#        if (ret):
#            frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
#            frame_pillow = Image.fromarray(frame_rgb)
#            frame_data.append(frame_pillow)
#        else:
#            break
#    
#    print('[Video file info]')
#    print(f'  - frame rate: {frame_rate}')
#    print(f'  - frame num: {len(frame_data)}')
#    print(f'  - duration of video file: {frame_rate * len(frame_data):.02f}[sec]')
#    
#    # --- Frames to GIF ---
#    duration = int(1000.0 / frame_rate)
#    frame_data[0].save(output_file, save_all=True, append_images=frame_data[1:], duration=duration, loop=0)

