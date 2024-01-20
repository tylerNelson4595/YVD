import customtkinter as ctk
from tkinter import ttk
from pytube import YouTube
import os

# create a root window
root = ctk.CTk()
ctk.set_appearance_mode("System")
ctk.set_default_color_theme("blue")

# title of window
root.title("Youtube Downloader!")

# fix minimum and max width of window in the app
root.geometry("720x480")
root.minsize(720, 480)
root.maxsize(1080, 720)

# create a frame to hold the content
# create a root variable with the ctk frame class pass it the root variable
content_frame = ctk.CTkFrame(root)
# lock the content in the frame and adding padding
content_frame.pack(fill=ctk.BOTH, expand=True, padx=10, pady=10)

# create a label and the entry widget for the video url
url_label = ctk.CTkLabel(content_frame, text="Enter the youtubeurl here: ")
entry_url = ctk.CTkEntry(content_frame, width=400, height=40)
url_label.pack(pady=(10, 5))
entry_url.pack(pady=(10, 5))

# to start the app
root.mainloop()