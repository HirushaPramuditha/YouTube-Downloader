import tkinter as tk
from tkinter import *
from pytube import YouTube
from tkinter import messagebox, filedialog


def SetWidgets():
    link_label = Label(root,
                       text=" Video URL       :",
                       bg="#ffd166")
    link_label.grid(row=1,
                    column=0,
                    pady=5,
                    padx=5)

    root.link_text = Entry(root,
                           width=55,
                           textvariable=video_Link)
    root.link_text.grid(row=1,
                        column=1,
                        pady=5,
                        padx=5,
                        columnspan=2)

    location_label = Label(root,
                           text=" Location         :",
                           bg="#ffd166")
    location_label.grid(row=2,
                        column=0,
                        pady=5,
                        padx=5)

    root.location_text = Entry(root,
                               width=40,
                               textvariable=download_path)
    root.location_text.grid(row=2,
                            column=1,
                            pady=5,
                            padx=5)

    browse_btn = Button(root,
                        text="Browse",
                        command=Browse,
                        width=10,
                        bg="#e1e1e1")
    browse_btn.grid(row=2,
                    column=2,
                    pady=1,
                    padx=1)

    download_btn = Button(root,
                          text="Download",
                          command=Download,
                          width=20,
                          bg="#e74c3c",
                          fg="#ffffff")
    download_btn.grid(row=3,
                      column=1,
                      pady=3,
                      padx=3)


def Browse():
    download_directory = filedialog.askdirectory(
        initialdir="YOUR DIRECTORY PATH")

    download_path.set(download_directory)


def Download():

    youtube_link = video_Link.get()
    download_folder = download_path.get()

    get_video = YouTube(youtube_link)
    video = get_video.streams.get_highest_resolution()

    video.download(download_folder)

    messagebox.showinfo("Success!",
                        "Downloaded and saved in\n"
                        + download_folder)


root = tk.Tk()

root.geometry("600x200")
root.resizable(False, False)
root.title("YouTube Downloader")
root.config(background="#ecf0f1")
root.iconbitmap('.\\icon.ico')

video_Link = StringVar()
download_path = StringVar()

SetWidgets()

root.mainloop()
