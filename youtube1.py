from pytubefix import YouTube
import tkinter as tk
from tkinter import filedialog

def download_video(url, save_path):
    try:
        print("Started download...")
        yt = YouTube(url)
        stream = yt.streams.filter(progressive=True, file_extension="mp4").get_highest_resolution()
        stream.download(output_path=save_path)
        print("Video downloaded successfully!")
    except Exception as e:
        print("Error:", e)

def open_file_dialog():
    folder = filedialog.askdirectory()
    return folder

if __name__ == "__main__":
    root = tk.Tk()
    root.withdraw()

    video_url = input("Please enter a YouTube url: ")
    save_dir = open_file_dialog()

    if save_dir:
        download_video(video_url, save_dir)