import os
from moviepy.editor import VideoFileClip
from tqdm import tqdm

def find_mp4_videos(directory):
    """Traverses the given directory and subdirectories to find all MP4 files."""
    mp4_files = []
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith('.mp4'):
                full_path = os.path.join(root, file)
                mp4_files.append(full_path)
    return mp4_files

def get_total_playtime(mp4_files):
    """Calculates the total playtime of all MP4 files provided."""
    total_duration = 0
    for video_file in tqdm(mp4_files, desc="Calculating video lengths"):
        try:
            clip = VideoFileClip(video_file)
            total_duration += clip.duration
            clip.close()
        except Exception as e:
            print(f"Error processing file {video_file}: {e}")
    return total_duration

def format_duration(seconds):
    """Formats seconds into hours, minutes, and seconds."""
    hours = seconds // 3600
    minutes = (seconds % 3600) // 60
    seconds = seconds % 60
    return f"{int(hours)}h {int(minutes)}m {int(seconds)}s"

def main(directory):
    mp4_files = find_mp4_videos(directory)
    total_playtime = get_total_playtime(mp4_files)
    formatted_time = format_duration(total_playtime)
    return formatted_time

if __name__ == "__main__":
    directory = input("Enter the directory path: ")
    total_time = main(directory)
    print(f"The total playtime of all MP4 files is: {total_time}.")