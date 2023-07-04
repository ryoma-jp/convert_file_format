
from PIL import Image
import cv2

def mp42gif(input_file, output_file):
    """Convert MP4 to GIF
    
    Convert MP4 file to GIF file.
    
    Args:
        - input_file (string): input mp4 file path
        - output_file (string): output gif file path
    
    Returns:
        - None
    """
    
    # --- Video to Frames ---
    cap = cv2.VideoCapture(input_file)
    if (not cap.isOpened()):
        return None, None
    
    frame_data = []
    frame_rate = cap.get(cv2.CAP_PROP_FPS)
    
    while (True):
        ret, frame = cap.read()
        if (ret):
            frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            frame_pillow = Image.fromarray(frame_rgb)
            frame_data.append(frame_pillow)
        else:
            break
    
    print('[Video file info]')
    print(f'  - frame rate: {frame_rate}')
    print(f'  - frame num: {len(frame_data)}')
    print(f'  - duration of video file: {frame_rate * len(frame_data):.02f}[sec]')
    
    # --- Frames to GIF ---
    duration = int(1000.0 / frame_rate)
    frame_data[0].save(output_file, save_all=True, append_images=frame_data[1:], duration=duration, loop=0)

