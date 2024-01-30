
import os
import asyncio
import ffmpeg

def mp4_h265toh264(input_file, output_file):
    """Convert H.265 MP4 to H.264 MP4
    
    Convert H.265 MP4 file to H.264 MP4 file.
    
    Args:
        - input_file (string): input mp4(H.265) file path
        - output_file (string): output mp4(H.264) file path
    
    Returns:
        - None
    """
    
    # --- Check input file ---
    if (not os.path.exists(input_file)):
        print(f'[ERROR] {input_file} does not exist.')
        return None
    
    # --- Check output file ---
    if (os.path.exists(output_file)):
        print(f'[ERROR] {output_file} already exists.')
        return None
    
    # --- Convert H.265 MP4 to H.264 MP4 ---
    ffmpeg.input(input_file).output(output_file, vcodec='libx264').overwrite_output().run()
    
    return None

